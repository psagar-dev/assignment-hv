# Backup Script Guide

#### Q4. In DevOps, performing regular backups of important files is crucial:

## Requirements

- Implement a Python script called `backup.py` that takes a source directory and a destination directory as command-line arguments.
- The script should copy all files from the source directory to the destination directory.
- Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
- Handle errors gracefully, such as when the source directory or destination directory does not exist.

## Sample Command

```sh
python backup.py /path/to/source /path/to/destination
```

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.

---
## Overview
This script helps in backing up files from a source directory to a destination directory. If a file with the same name already exists in the destination, a timestamp is appended to ensure uniqueness.

## Prerequisites
- Python installed (version 3.x recommended)
- Basic understanding of command-line usage

## Steps to Use

### 1. Open a Terminal
Navigate to the directory where `backup.py` is saved.

```sh
cd /path/to/your/script
```

### 4. Run the Script
Use the following command to run the script, replacing `/source_path` and `/destination_path` with the actual paths:

```sh
python backup.py /source_path /destination_path
```

### 5. Verify the Backup
Check the destination directory to ensure the files are copied correctly. If a file with the same name exists, a timestamped version will be created.

## Error Handling
- If the source directory does not exist, an error message is displayed.
- If the destination directory does not exist, it is created automatically.
- If a file already exists in the destination, it is renamed with a timestamp.