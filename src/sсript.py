import os
import hashlib
import csv
import sys

def md5_file(path, chunk_size=8192):
    # md5 for a single file
    md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            md5.update(chunk)
    return md5.hexdigest()

def scan_files(root):
    rows = []
    global_md5 = hashlib.md5()

    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            path = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(path)
                file_md5 = md5_file(path)

                with open(path, "rb") as infile:
                    for chunk in iter(lambda: infile.read(8192), b""):
                        global_md5.update(chunk)

                rows.append([
                    os.path.relpath(path, root),  # relative path
                    f,
                    round(size / (1024*1024), 3),  # mb, here u can change to other size units
                    file_md5
                ])
            except (FileNotFoundError, PermissionError):
                continue

    return rows, global_md5.hexdigest()

def save_to_csv(rows, out_file="files_report.csv", total_md5=None):
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Путь", "Имя файла", "Размер (МБ)", "MD5"])
        writer.writerows(rows)

    if total_md5:
        with open("total_md5.txt", "w", encoding="utf-8") as f:
            f.write(total_md5)