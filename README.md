# FFS (folders file scanner)

A small Python utility to scan a project directory, generate a CSV report with file sizes and MD5 checksums, and compute a stable overall MD5 for the project.

## Features

- Recursively scan all files in a directory
- CSV report (`files_report.csv`) with:
  - Relative path
  - File name
  - Size in MB
  - MD5 checksum
- Stable overall MD5 (`total_md5.txt`) of all file contents

## Requirements

- Python 3.7+

## Usage

```bash
python scan.py /path/to/folder
