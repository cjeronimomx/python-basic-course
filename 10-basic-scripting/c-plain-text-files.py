import os
# WRITE FILES
file = open("my_file.txt", "w") # r=read, w=write, a=append
file.write("Your content file goes here")
file.write("\n")
file.write("More text")
file.close()

# This is best practice because close file automatically
if os.path.exists('/Users/cjeronimo/Code/NT/python-basic-course/10-basic-scripting'):
    with open("other_file.txt", "w") as file:
        file.write("Your text goes here")

# READ FILES
try:
    with open("my_file.txt", "r") as file:
        print(file.read())
        """
        content = file.readlines() # You can pass a number o bytes
        for line in content:
            print(line)
        """
except FileNotFoundError as ex:
    print(ex.strerror)


try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError as ex:
    print(ex.strerror)


"""
# Get current directory - pwd
print(os.getcwd())

# List files and directories - ls
print(os.listdir())
print(os.listdir("/Users/cjeronimo"))

# Move a file to an other path
os.rename()
# shutil.move()

# Remove a file
os.unlink(path=)

# Remove a folder
os.rmdir(path=)

# Remove remove files and directories recursive
import shutil
shutil.rmtree(path=)

# Iterate a directory
for folder, subfolders, files in os.walk(os.getcwd()):
    print(f"Looking in folder: {folder}")

    for subfolder in subfolders:
        print(f"\t Subfolder: {subfolder}")
    for fille in files:
        print(f"\t File: {fille}")
"""