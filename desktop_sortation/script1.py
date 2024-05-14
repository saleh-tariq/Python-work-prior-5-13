# DESKTOP CLEANER
from pathlib import Path
# find way to detect desktop path
# identify file types
# create folders for each file placement
# move objects into folders based on file type


# file = Path('new_file.py')
# folder = Path('new_folder')

# VVV Makes a file
# file.touch()

# VVV Makes a folder
# folder.mkdir()

# new_file = folder / 'whatever.py'
# new_file.touch()

# file.write_text('print("hello world!")')

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

# READING FILES IN A DIRECTORY
# my_folder = Path('new_folder')
# for path in my_folder.iterdir():
#     print(path.name)


# READING ALL FILES INCLUDING NESTED
# current_folder = Path('.')

# for path in current_folder.glob('**/*'):
#     print(path.name)

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

# DELETING BY TYPE IN A DIR
# my_folder = Path('new_folder')
# for path in my_folder.iterdir():
#     if 'txt' in path.name:
#         path.unlink()
