import os

# Path to folder containing text files
folder = "E:/v2e/Source"

# Dictionary to store filename: word_count
result = {}

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Split by whitespace to count words
            word_count = len(content.split())
            result[filename] = word_count

# Print result
for name, count in result.items():
    print(f"{name}: {count} words")
