import os

folder_path = "files"
os.makedirs(folder_path, exist_ok=True)

existing_files = os.listdir(folder_path)
highest_number = 0

for file in existing_files:
    if file.startswith("testFile_") and file.endswith(".txt"):
        try:
            number = int(file.replace("testFile_", "").replace(".txt", ""))
            highest_number = max(highest_number, number)
        except ValueError:
            continue

print("Enter the number of files you want to be created: ")
amt = int(input("Number of files: "))

for i in range(amt):
    file_name = f"testFile_{highest_number + i + 1}.txt"
    file_path = os.path.join(folder_path, file_name)
    open(file_path, "a")

print(f"{amt} files created in {folder_path} directory.")