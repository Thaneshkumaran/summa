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
