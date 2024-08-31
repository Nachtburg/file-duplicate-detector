# File Duplicate Finder

File Duplicate Finder is a Python tool designed to help identify and remove duplicate files from a directory. It utilizes multi-threading to enhance performance and provides real-time progress updates. The tool also logs any errors and maintains lists of kept and removed files.

## Features

- **Progress Tracking**: Displays progress updates during the file scanning process.
- **Multi-threading**: Accelerates file processing through concurrent execution.
- **Flexible Directory Search**: Allows specifying which storage or directory to scan, including deep subdirectory search.
- **Hash-based Duplicate Detection**: Identifies duplicates based on file content rather than file names.
- **Error Logging**: Logs any errors encountered during the scanning process.
- **File Listing**: Saves lists of kept and removed files to separate text files.

## Requirements

- Python 3.x
- `tqdm` for progress tracking (listed in `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nachtburg/file-duplicate-detector.git
   ```

2. Navigate to the project directory:
   ```bash
   cd file-duplicate-detector
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script and follow the prompts to scan for duplicates:

```bash
python file_duplicate_detector.py
```

### Usage Example

Run the script with the following commands:

```bash
Enter the directory to scan for duplicates: /path/to/your/directory
Enter the number of threads to use (e.g., 4): 4
Keep the original files? (yes/no): yes
```

### Output Example

After the script finishes, you might see the following messages:

```
Scanning for duplicates...
Duplicate files detected. Removing duplicates...
Duplicate removal complete. Check kept_files.txt and removed_files.txt for details.
Errors have been logged to errors.log
```

- `kept_files.txt`: List of kept files
- `removed_files.txt`: List of removed files
- `errors.log`: Log of errors encountered during the scan

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Error Logging

If any errors occur during the file scanning process, they will be logged in the `errors.log` file. This file will contain the path of the file that caused the error and a description of the issue.