# Run this file only when you are absolutely sure

from os import system
from WebsiteData import main_pages, Main_Folders

for folder in Main_Folders:
    # run this command to check the files to be deleted
    # system(f'find ./{folder} -name "*.html" -type f')

    # run this command to delete the files after checking
    system(f'find ./{folder} -name "*.html" -type f -delete')

for page in main_pages:
    # run this command to check the files to be deleted
    # system(f'ls ./{page}')

    # run this command to delete the files after checking
    system(f'rm ./{page}')