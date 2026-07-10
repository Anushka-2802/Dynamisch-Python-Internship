import os

def current_dir():
    """Display current working directory"""
    print("Current working directory",os.getcwd())
    

def create_dir(demo):
    """Create a single folder"""
    if not os.path.exists(demo):
        os.mkdir(demo)
        print(f"{demo} directory created")
    else:
        print(f"Directory already exist")

    
def create_nested_directories(path): 
    """Create nested directories""" 
    if not os.path.exists(path):
        os.makedirs(path) 
        print(f"{path} created successfully") 
    else: 
        print(f"{path} already exists")
    
def list_files(): 
    """Display files and folders"""
    print("\nList of files and directories")
    print(os.listdir())


def rename_file(old_name, new_name): 
    """Rename existing file""" 
    if os.path.exists(old_name): 
        os.rename(old_name, new_name) 
        print(f"{old_name} renamed to {new_name}") 
    else:
        print(f"{old_name} does not exist")

def check_path(path): 
    """Check file or directory""" 
    print("\nPath Checking") 
    print("Exists:", os.path.exists(path)) 
    print("Is File:", os.path.isfile(path)) 
    print("Is Directory:", os.path.isdir(path))

def remove_file(file_name): 
    """Remove file""" 
    if os.path.exists(file_name): 
        os.remove(file_name) 
        print(f"{file_name} removed successfully") 
    else: print(f"{file_name} does not exist")

def remove_directory(folder_name): 
    """Remove empty directory""" 
    if os.path.exists(folder_name): 
        os.rmdir(folder_name) 
        print(f"{folder_name} removed successfully") 
    else: 
        print(f"{folder_name} does not exist")

current_dir()
create_dir("Demo_dir")  
create_nested_directories("Dynamisch_Internship\Demo_dir")  
list_files()
rename_file("Demo_dir","Demo")
check_path("Demo")
remove_file("demo.txt")
remove_directory("Demo")
