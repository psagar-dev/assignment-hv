import os
import shutil
import sys
import datetime

def backup_files(source_dir, destination_dir):
    """Back up files from source_dir to destination_dir, ensuring unique filenames."""
    # Check if source directory exists
    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist or is not a directory.")
        sys.exit(1)
    
    # Check if destination directory exists; if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        if os.path.isfile(source_file):
            if os.path.exists(destination_file):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}")
            
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")
    
    print("Backup completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /source_path /destination_path")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    
    backup_files(source_directory, destination_directory)