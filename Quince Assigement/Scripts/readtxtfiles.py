import os

def read_txt_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as txt_file:
                    content = txt_file.read()
                    print(f"Content of {file_path}:\n{content}\n")

if __name__ == "__main__":
    directory_path = "/path/to/your/directory"  # Replace with the path to your directory
    read_txt_files(directory_path)




#Make sure to replace "/path/to/your/directory" with the actual path to the directory containing your *.txt files. This script uses os.walk to traverse through all directories and subdirectories, and for each file found with a .txt extension, it reads and prints the content.