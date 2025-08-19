import mysql.connetor

def view(set_list):
    for i in range(len(set_list)):
        print(i,".",set_list[i])
set_list=["TO create account","TO deposit amount","TO withdrawal", "TO view balance",'TO quit']
view(set_list)

import os

# Base folder
base = "E:/v2e"
source = os.path.join(base, "Source")
destination = os.path.join(base, "Destination")

# Create folders
os.makedirs(source, exist_ok=True)
os.makedirs(destination, exist_ok=True)

# Create 10 text files
for i in range(1, 11):
    file_path = os.path.join(source, f"file{i}.txt")
    with open(file_path, "w") as f:
        if i % 2 == 0:  # Add word in 5 files
            f.write("This file contains V2eTechnologies. V2eTechnologies is great.\n")
        else:
            f.write("This is just a normal file.\n")

# Move files containing 'V2eTechnologies' (manual copy + delete)
for file in os.listdir(source):
    file_path = os.path.join(source, file)
    with open(file_path, "r") as f:
        content = f.read()
        count = content.count("V2eTechnologies")
        if count > 0:
            # Write into destination (copy)
            dest_path = os.path.join(destination, file)
            with open(dest_path, "w") as new_file:
                new_file.write(content)

            # Delete original (simulate move)
            os.remove(file_path)

            print(f"{file} -> contains 'V2eTechnologies' {count} times")


# Function to read the file and separate vowels and non-vowels
def separate_vowels_and_non_vowels(file_path):
    vowels = "aeiouAEIOU"
    vowels_list = []
    non_vowels_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line_vowels = [char for char in line if char in vowels]
            if line_vowels:
                vowels_list.extend(line_vowels)
                # Remove vowels from line
                modified_line = ''.join([char for char in line if char not in vowels])
                non_vowels_list.append(modified_line)
    
    print("Vowels List:", vowels_list)
    print("Non-Vowels List:", non_vowels_list)

# Example usage
file_path = 'example.txt'  # Replace with your file path
separate_vowels_and_non_vowels(file_path)


import os

# Function to count files and subfolders in each folder
def folder_structure_to_dict(source_folder):
    result = {}
    
    for root, dirs, files in os.walk(source_folder):
        folder_name = os.path.relpath(root, source_folder)
        sub_folders = len(dirs)
        file_count = len(files)
        
        result[folder_name] = {"folders": sub_folders, "files": file_count}
    
    return result

# Example usage
source_folder = 'C:/source'  # Replace with your folder path
folder_structure = folder_structure_to_dict(source_folder)
print(folder_structure)


from collections import defaultdict

# Function to create a dictionary with word counts
def word_count(file_path):
    word_dict = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_dict[word.lower()] += 1
    
    # Convert defaultdict to normal dict for printing
    print(dict(word_dict))

# Example usage
file_path = 'example.txt'  # Replace with your file path
word_count(file_path)


import os
import shutil

# Function to move files containing "v2etechnologies" to destination folder
def move_files_with_keyword(source_folder, destination_folder, keyword):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_count = 0
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                count = content.lower().count(keyword.lower())
                total_count += count

                if count > 0:
                    # Move the file to the destination folder
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"File '{filename}' moved with {count} occurrences of '{keyword}'")

    print(f"Total occurrences of '{keyword}':", total_count)

# Example usage
source_folder = 'C:/Source'  # Replace with your folder path
destination_folder = 'C:/Destination'  # Replace with your destination folder
keyword = 'v2etechnologies'
move_files_with_keyword(source_folder, destination_folder, keyword)
