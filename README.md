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

## Background

A while ago, I noticed strange behavior on my PC. My files, especially executable files (`.exe`), were behaving abnormally. After further investigation, I discovered that the `Gallery.exe` virus had infected my system. The virus was renaming my `.exe` files and replacing them with smaller, g-prefixed versions (e.g., `gexample.exe`). These g-prefixed files were fake versions that were created by the virus to replace the original files, and it was also hiding my actual executable files.

The virus also seemed to add `.ico` files (e.g., `gexample.ico`), which I later realized were part of its operations. The whole situation was frustrating and confusing, as I couldn't easily recover my original files, and I couldn't run many of my programs because they had been replaced by these `g-` prefixed files.

After several attempts to manually fix this issue, I realized that I needed an automated solution to restore my system and get rid of the virus's impact on my files. So after installing new window, I created a Python script that would:

1. Search for all `.exe` files affected by the virus (i.e., smaller-sized files with `g-` prefix).
2. Restore the original file by renaming the g-prefixed files.
3. Remove any associated `.ico` files related to the virus.

This script worked effectively in cleaning my system and allowed me to restore my files, but I soon realized that others could be facing the same issue. I decided to make this tool publicly available to help others who might be dealing with the same problem. By sharing this script, I hope to help people remove the `Gallery.exe` virus and recover their systems without having to deal with the confusion and time-consuming manual process.

This tool is now open-source and available for anyone to use and modify. It scans a directory, processes the files, restores the original `.exe` files, and removes the malicious `g-` prefixed files and related `.ico` files, all while logging the process in a CSV for transparency.

If you've encountered similar issues or suspect that your system has been infected, this script can help you clean up the virus and restore your files quickly.

Stay safe, and always make sure to back up your important files regularly.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
