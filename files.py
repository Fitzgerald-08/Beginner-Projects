#!/bin/python3 

from pathlib import Path
import sys 

# This script is used merely for practicing scripting abilities such as
# Reading/Writing to files and how to avoid losing data.

# Libraries I have planned on using:
# --> pathlib (currently using)
# --> shutil
# --> sys (currently using)

# Change the path to whatever is desired
p = Path.home()

dirs = []
files = []

for file in p.iterdir():
    if file.is_dir():
        dirs.append(file.name)
    if file.is_file():
        files.append(file.name)

# Add the contents of both lists to one list, which is going to be saved
# to a file.

dir_contents = dirs + files

if 0 == len(dirs) == len(files):
    print("[!] No directories nor files have been found...") 
    sys.exit(1)
else:
    if len(dirs) == 0:
        print("[!] No directories have been found...")
    else:
        print("+ DIRECTOIRES FOUND:")
        for d in dirs:
            print(d)

    if len(files) == 0:
        print("\n[!] No files have been found...")
    else:
        print("\n+ FILES FOUND:")
        for f in files:
            print(f)

        answer = ""
        while answer != "n" or answer != "y":
            answer = input("Would you like to save this information to a file? [y/n]")
            if answer == "y":
                print("[+] Saving to file...")

                new_file = Path.cwd() / "data_files.txt"
                new_file.touch(mode=0o640)

                for line in dir_contents:
                    file_contents = new_file.read_text()
                    new_file.write_text(f"{file_contents}{line}\n")

                sys.exit(0)
            elif answer == "n":
                print("Exiting script...")
                sys.exit(0)
            else:
                print("[!] Fatal: No valid answer was detected")
