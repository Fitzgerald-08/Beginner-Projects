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
p = Path("/home")

# Show the results of the file scanning
def show_results(dirs, files, dir_contents):
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


def main():
    # Pass both lists and their addition to the show_results function
    dirs = []
    files = []

    # Attempt to read the contents of the a directory
    try:
        for file in p.iterdir():
            if file.is_dir():
                dirs.append(file.name)
            if file.is_file():
                files.append(file.name)
    # If permissions are not enough, catch the exception
    except PermissionError as e:
        print(f"An error has occured...\n{e}")
        sys.exit(1)
    # If the directory is correctly read, print a message to let the user know it
    else:
        print("[+] Directories read correctly")

    # Ask the user what to do with the data, either save the the results to
    # a file or directly view them
    results = ""
    while True:
        results = input("[V]iew results\n[S]ave to file\ninput: ").lower()

        if results == "s":

            # Input the name for the file to store results
            file_name = input("Introduce file name: ")
            file_path = p / f"{file_name}.txt"
            Path.touch(file_path, mode=0o644)  # Create a file with appropiate permissions

            # Fill the file with the results
            results = dirs + files
            with file_path.open(mode="a") as f:
                for entry in results:
                    f.write(f"{entry}\n")

            # Exit successfully
            sys.exit(0)
        elif results == "v":
            dir_contents = dirs + files
            show_results(dirs, files, dir_contents)
            sys.exit(0)
        else:  # As long as the input is not S/V keep going the while loop
            print("[!] Input error. Specify S/V")


if __name__ == "__main__":
    main()
