#Dependencies
import os
import shutil

#Main
def dir_files(dir_path):
    try:
        files = []

        for ( root, _, filenames ) in os.walk(dir_path):
            files.extend(filenames)

            break

        return None, files
    except:
        return "Unable to get directory files.", False

def recursive_dir_files(dir_path):
    try:
        files = []

        for root, directories, filenames in os.walk(dir_path): 
            for filename in filenames:  
                files.append(os.path.join(root, filename))

        return None, files
    except:
        return "Unable to recursive in the directory.", False

def read_file(file_path):
    try:
        file = open(file_path, "r")

        return None, file.read()
    except:
        return "Unable to find/read the file.", False

def write_file(file_path, content):
    try:
        file = open(file_path, "w")
        file.write(content)
        file.close()
    except:
        return "Unable to write the file.", False

    return None, True

def remove_file(file_path):
    try:
        os.remove(file_path)

        return None, True
    except:
        return "Unable to remove the file.", False

def remove_dir(dir_path):
    try:
        shutil.rmtree(dir_path)

        return None, True
    except:
        return "Unable to remove the directory.", False

def rename_file(file_path, new_name):
    try:
        os.rename(file_path, new_name)

        return None, True
    except:
        return "Unable to rename the file.", False

def copy_file(file_path, new_path):
    try:
        shutil.copy(file_path, new_path)

        return None, True
    except:
        return "Unable to copy the file.", False

def file_exists(file_path):
    try:
        return os.path.isfile(file_path), True
    except:
        return "File does not exist.", False

def dir_exists(dir_path):
    try:
        return os.path.isdir(dir_path), True
    except:
        return "Directory does not exist.", False
