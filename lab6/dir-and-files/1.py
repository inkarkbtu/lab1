import os

def write_list_to_file(list_items, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True) 
    with open(file_path, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")
# 1
def list_dir_files(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    all_items = os.listdir(path)
    dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All Items:", all_items)

# 2
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3
def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

# 4
def count_lines(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return
    
    with open(file_path, 'r') as file:
        print("Number of lines:", len(file.readlines()))

# 5
def write_list_to_file(list_items, file_path):
    with open(file_path, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")

# 6
def generate_26_files(directory):
    os.makedirs(directory, exist_ok=True)
    for i in range(65, 91):  
        with open(os.path.join(directory, f"{chr(i)}.txt"), 'w') as file:
            file.write(chr(i))

# 7
def copy_file(source_path, destination_path):
    if not os.path.exists(source_path):
        print("Source file does not exist.")
        return
    
    with open(source_path, 'r') as source, open(destination_path, 'w') as dest:
        dest.write(source.read())

# 8
def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not a file.")


path = "/Users/fargofargo/Documents/new folder/labs"
txt = "/Users/fargofargo/Documents/new folder/labs/a.txt"
txt2 = "/Users/fargofargo/Documents/new folder/labs/Q.txt"


list_dir_files(path)
check_access(path)
test_path_details(txt)
count_lines(txt)
write_list_to_file(["Hello", "World"], txt2)
generate_26_files("/Users/fargofargo/Documents/new folder/labs/Alphabet")
copy_file(txt, txt2)
delete_file(txt2)