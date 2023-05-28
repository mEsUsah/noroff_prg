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


def save_matches(match_dict, log_file):
    file = open(log_file,'w')
    for item, hash in match_dict.items():
        file.write(f'{hash}: {item} \n')
    
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
    
    os.chdir(dir)

    dir_files = dict()
    for glob_file in glob("*.jpg"):
        hash = str(imagehash.average_hash(Image.open(glob_file)))
        dir_files[glob_file] = hash
    
    matching_hashes = dict()

    for dir_file, dir_file_hash in dir_files.items():
        for scan_file, scan_file_hash in dir_files.items():
            if dir_file != scan_file:
                if dir_file_hash == scan_file_hash:
                    matching_hashes[scan_file] = scan_file_hash

    if len(matching_hashes) > 0:
        print("Matches found! Saving to file...")
        save_matches(matching_hashes, file)
    else:
        print("No matches found...")

        

    

if __name__ == '__main__':
    args = parser.parse_args()
    task(args.directory[0], args.file[0])