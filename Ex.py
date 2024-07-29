import os
import shutil

def smart_dock_and_extract(source_path, destination_path):
    try:
        # Check if the source path exists
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source path {source_path} does not exist.")
        
        # Create the destination path if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Perform data integrity check (example: check file size or hash)
        source_size = sum(os.path.getsize(f) for f in os.listdir(source_path) if os.path.isfile(f))
        print(f"Source data size: {source_size} bytes")
        
        # Transfer data
        for file_name in os.listdir(source_path):
            full_file_name = os.path.join(source_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, destination_path)
        
        # Verify data integrity post-transfer (example: check file size or hash)
        dest_size = sum(os.path.getsize(os.path.join(destination_path, f)) for f in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, f)))
        print(f"Destination data size: {dest_size} bytes")
        
        if source_size != dest_size:
            raise ValueError("Data integrity check failed: Source and destination sizes do not match.")
        
        print("Data extracted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_path = '/path/to/source'
destination_path = '/path/to/destination'
smart_dock_and_extract(source_path, destination_path)
