import glob
from pathlib import Path

"""
*: Matches any string of characters, including an empty string.
?: Matches any single character.
[ ]: Matches any character inside the brackets.
[! ]: Matches any character not inside the brackets.
**: Perform a recursive search that includes all subdirectories.
"""

data_repo = '../../data_repo/'

files = glob.glob(f'{data_repo}my_folder/*')
print(files)

# Find Files Recursively with glob
files = glob.glob(f'{data_repo}my_folder/**/*.txt', recursive=True)
# recursive=True, is necessary to tell glob to search for the pattern recursively.
print(files)

# pathlib
path = Path(f'{data_repo}my_folder')  # creating a path object
print(path.name)  # accessing the name of the file
print(path.parent)  # accessing the directory of the file
new_path = path / 'my_file.txt'  # joining paths
print(new_path)  # printing the new path
if new_path.exists():
    print('The path exists.')
    content = new_path.read_text()  # reading the file
    print(content)
    new_path.write_text('Hello, World!')
else:
    print('The path does not exist.')

# creating multiple directories
new_path = path / 'new_folder/sub_folder'  # Or path / 'new_folder' / 'sub_folder'
new_path.mkdir(parents=True, exist_ok=True)

# create a symbolic link using pathlib (on Windows, you need to run the script as an administrator)
# symlink_path = Path(f'{data_repo}/my_folder/symlink')
# symlink_path.symlink_to(path)
