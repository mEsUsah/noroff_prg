import argparse
import os
from PIL import Image
import imagehash
from glob import glob

## add argument definitions
parser = argparse.ArgumentParser()
parser.add_argument('-d','--directory', 
                    help="Directory to scan", 
                    required=True,
                    nargs=1)

parser.add_argument('-f','--file', 
                    help="File to find", 
                    required=True,
                    nargs=1)


def find_duplicates(dir):
    # Move into selected directory
    os.chdir(dir)

    dir_files = dict()
    duplicate_files = dict()

    # Loop over all .jpg images in directory
    for glob_file in glob("*.jpg"):
        hash = str(imagehash.average_hash(Image.open(glob_file)))

        # Check for duplicate in dictionary of unique files
        if hash in dir_files:
            # Create set in duplicate list if this is the first duplicate found
            if hash not in duplicate_files:
                duplicate_files[hash] = set()

            # Add filename to set containing filename of duplicates
            duplicate_files[hash].add(dir_files[hash]) # Will not be added if already in set
            duplicate_files[hash].add(glob_file)  # Add file to set
        
        # If not a duplicate, add to dictionary of unique files.
        else:
            dir_files[hash] = glob_file

    # Return to original directory
    os.chdir("..")
    return duplicate_files


def save_matches(duplicate_files:dict, log_file:str):
    file = open(log_file,'w')
    for duplicate_hash, duplicate_files in duplicate_files.items():
        file.write(f'{duplicate_hash}:\n')

        for duplicate_file in duplicate_files:
            file.write(f'- {duplicate_file}\n')
        
    file.close()


def task(dir, file):
    '''
    Write a Python script that accepts the following command line arguments: 
    - folder to be scanned 
    - file name.

    The folder to be scanned needs to be an image folder that the user wants to scan. 
    The file name will be the filename and path where the end user wants to save the results.

    The image folder will need to be scanned, and the images hashed and compared. 
    If a matching hash is found, it must be saved to the text file. 
    The format to save the results in would be the filename, hash.
    '''
    
    duplicate_files = find_duplicates(dir)

    if len(duplicate_files) > 0:
        print(f"Duplicates found! Saving to file ({file})...")
        save_matches(duplicate_files, file)
    else:
        print("No Duplicates found...")

        
if __name__ == '__main__':
    args = parser.parse_args()
    task(args.directory[0], args.file[0])