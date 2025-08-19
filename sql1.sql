create database db;


import os

def move_files_with_keyword(source_folder, destination_folder, keyword):
    # Make sure destination exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)

        # Only process .txt files
        if os.path.isfile(source_file_path) and filename.endswith('.txt'):
            with open(source_file_path, 'r') as file:
                content = file.read()
                count = content.lower().count(keyword.lower())

                # If keyword is found, move file and report count
                if count > 0:
                    destination_file_path = os.path.join(destination_folder, filename)
                    # Move the file to destination using os.rename
                    os.rename(source_file_path, destination_file_path)
                    print(f"FileName: {filename}  TotalCount: {count}")

# Example usage
source_folder = 'C:/Source'        # Make sure this folder exists with .txt files
destination_folder = 'C:/Destination'  # This will be created if it doesn't exist
keyword = 'v2etechnologies'

move_files_with_keyword(source_folder, destination_folder, keyword)

