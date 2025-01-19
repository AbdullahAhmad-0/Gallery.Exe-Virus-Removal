import os
import csv

def process_directory(root_dir):
    records = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".exe"):
                file_path = os.path.join(dirpath, filename)
                file_status = "processed"

                try:
                    file_size = os.path.getsize(file_path)
                except FileNotFoundError:
                    file_status = "skipped (file not found)"
                    print(f"Skipped: {filename} - {file_status}")
                    records.append({
                        'File Path': dirpath,
                        'File Name': filename,
                        'Size (bytes)': 'N/A',
                        'ICO File Delete': 'N/A',
                        'Status': file_status
                    })
                    continue  # Skip this file and continue with the next one
                
                if file_size < 1 * 1024 * 1024:  # Less than 1MB
                    g_filename = 'g' + filename
                    g_file_path = os.path.join(dirpath, g_filename)

                    if os.path.exists(g_file_path):
                        try:
                            # Delete the original file
                            os.remove(file_path)
                        except FileNotFoundError:
                            file_status = "skipped (original file not found)"
                            print(f"Skipped: {filename} - {file_status}")
                            records.append({
                                'File Path': dirpath,
                                'File Name': filename,
                                'Size (bytes)': file_size,
                                'ICO File Delete': 'N/A',
                                'Status': file_status
                            })
                            continue  # Skip if the file was already deleted

                        # Rename g-prefixed file
                        new_file_path = os.path.join(dirpath, filename)
                        os.rename(g_file_path, new_file_path)

                        # Handle .ico file
                        ico_filename = 'g' + os.path.splitext(filename)[0] + ".ico"
                        ico_file_path = os.path.join(dirpath, ico_filename)
                        ico_status = "not present"

                        if os.path.exists(ico_file_path):
                            try:
                                os.remove(ico_file_path)
                                ico_status = "present and deleted"
                            except Exception as e:
                                ico_status = f"error while deleting: {str(e)}"

                        # Record this change
                        print(f"Processed: {filename} - Renamed g-prefixed file and checked .ico")
                        records.append({
                            'File Path': dirpath,
                            'File Name': filename,
                            'Size (bytes)': file_size,
                            'ICO File Delete': ico_status,
                            'Status': "processed"
                        })
                    else:
                        print(f"Processed: {filename} - No g-prefixed file found")

    # Save the records to a CSV file
    output_csv = os.path.join(root_dir, 'file_changes_log.csv')
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['File Path', 'File Name', 'Size (bytes)', 'ICO File Delete', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)

    print(f"Processing complete. Log saved to {output_csv}")

# Example usage
if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to scan: ")
    process_directory(directory_to_check)
