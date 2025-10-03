from src.sсript import scan_files, save_to_csv
import sys


if len(sys.argv) < 2:
    print("try: python scan.py /path/to/folder") 
    sys.exit(1)

target_dir = sys.argv[1]
rows, total_md5 = scan_files(target_dir)
save_to_csv(rows, "files_report.csv", total_md5)

print(f"dir: {target_dir}")
print(f"data saved to files_report.csv")
print(f"total md5: total_md5.txt")
