from datetime import datetime, date
from zipfile import ZipFile
import shutil
import os

#### Important note! ####
# Create the following files in the directory you run the script:
# - test.txt
# - test.png

def create_dir(dirname: str):
    if not os.path.exists(os.path.join(os.getcwd(), dirname)):
        os.mkdir(dirname)


def copy_files(files: tuple, to_dir: str):
    for file in files:
        from_path = os.path.join(os.getcwd(), file)
        to_path = os.path.join(os.path.join(os.getcwd(),to_dir,file))
        
        shutil.copy(from_path, to_path)


def rename_dir_files(dir: str):
    files_in_dir = os.listdir(os.path.join(os.getcwd(), dir))

    for file in files_in_dir:
        complete_filepath = os.path.join(os.getcwd(),dir, file)

        filename_parts = file.split(".")
        file_stats = os.stat(complete_filepath)
        file_created = str(datetime.fromtimestamp(file_stats.st_ctime))
        filename_parts.insert(-2,file_created[:10])
        new_filename = ".".join(filename_parts)
        new_complete_filepath = os.path.join(os.getcwd(), dir, new_filename)

        os.rename(complete_filepath, new_complete_filepath)


def list_dir(dir):
    for item in os.listdir(dir):
        path = os.path.join(os.getcwd(), dir, item)
        print(path)


def archive_dir(dir):
    today = str(date.today())
    filename = ".".join([dir, today, 'zip'])
    with ZipFile(filename, 'w') as zipfile:
        files_in_dir = os.listdir(dir)
        os.chdir(dir)
        for file in files_in_dir:
            zipfile.write(file)
    

if __name__ == '__main__':
    # Ask the user for the name of a new directory.
    new_dirname = input('Please enter a dir name: ')
    
    # Create the directory in the same path as the script.
    create_dir(new_dirname)

    # Copy all of the files from your pre-created directory to the new directory.
    files = ('test.txt', 'test.png')
    copy_files(files, new_dirname)

    # Rename each newly created file by appending the original file’s 
    # creation date to the file name (before the file extension). 
    # This may require dusting off your string manipulation skills.
    rename_dir_files(new_dirname)

    # Display the list of newly created files to the user by reading the contents 
    # of the new directory.
    list_dir(new_dirname)


    # Create a new zip file named according to today’s date and add the contents 
    # of the entire (new) directory to the zip file.
    archive_dir(new_dirname)






