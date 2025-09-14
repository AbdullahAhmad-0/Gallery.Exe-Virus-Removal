import csv
import os
import subprocess
import sys
import platform

def remove_attributes(file_path):
    if not os.path.exists(file_path):
        print(f"[SKIPPED] File not found: {file_path}")
        return

    try:
        # Use subprocess without shell=True for safety
        subprocess.run(['attrib', '-H', '-S', file_path], check=True, shell=False)
        print(f"[FIXED] {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to update attributes: {file_path} -> {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error with file: {file_path} -> {e}")

def process_csv(csv_path):
    if not os.path.exists(csv_path):
        print(f"[ERROR] CSV file not found: {csv_path}")
        return

    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Using comma as delimiter

        for row in reader:
            status = row.get("Status", "").strip().lower()
            if status == "processed":
                file_dir = row.get("File Path", "").strip()
                file_name = row.get("File Name", "").strip()

                if file_dir and file_name and file_name.lower() != 'n/a':
                    full_path = os.path.join(file_dir, file_name)
                    remove_attributes(full_path)
                else:
                    print(f"[SKIPPED] Incomplete path in row: {row}")

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("[ERROR] This script only works on Windows.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python unhide_processed_files.py <path_to_csv>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    process_csv(csv_file_path)
