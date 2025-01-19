# Gallery.exe Virus Removal and Cleanup Tool

## Overview

The `Gallery.exe Virus Removal and Cleanup Tool` is a script designed to handle and remove the effects of the `Gallery.exe` virus. This virus converts regular `.exe` files into smaller-sized `.exe` files and renames them with a `g-` prefix (e.g., `gexample.exe`). The virus hides the original `.exe` files and replaces them with these smaller files. 

This tool scans the specified directory, identifies the infected `.exe` files, restores the original files, and deletes any associated `g-` prefixed `.exe` and `.ico` files.

## Features

- Scans directories recursively for `.exe` files infected by the `Gallery.exe` virus.
- Checks for `.exe` files smaller than 1MB (a typical behavior of the virus).
- Renames the `g-` prefixed files (e.g., `gexample.exe`) to restore the original file.
- Deletes any associated `g-` prefixed `.ico` files.
- Logs all actions in a CSV file, including the path, filename, file size, and status of any deletions or renaming.
- Provides error handling for missing or inaccessible files.

## How It Works

1. The script recursively searches the directory and its subdirectories for `.exe` files.
2. It checks if the file size is smaller than 1MB, which is a characteristic of the infected files.
3. If a `g-` prefixed `.exe` file (e.g., `gexample.exe`) is found:
   - It deletes the original file (if any).
   - Renames the `g-` prefixed file to the original filename.
4. It looks for an associated `.ico` file (e.g., `gexample.ico`) and deletes it if found.
5. All actions are logged to a CSV file named `file_changes_log.csv` for later review.

## Installation

1. Clone the repository to your local machine.

   git clone https://github.com/yourusername/gallery-exe-virus-removal.git
   cd gallery-exe-virus-removal

2. Ensure you have Python installed (Python 3.x is recommended). You can download Python from [here](https://www.python.org/downloads/).

3. Install any necessary dependencies (if applicable).

   pip install -r requirements.txt

4. You can now run the script with the following command:

   python gallery_exe_removal.py

## Usage

To use the tool, provide the path of the directory you want to scan when prompted:

Enter the directory path to scan:

The script will process the files, restore any hidden `.exe` files, and log the actions to a CSV file (`file_changes_log.csv`).

## Notes

- Always make sure to back up your important files before running any cleanup scripts.
- The script does not attempt to delete files that are already missing but logs such events in the CSV.
- If any issues arise during execution (such as missing permissions or corrupted files), the script will log the errors for further investigation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
