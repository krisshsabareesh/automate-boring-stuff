#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, shutil

def selective(folder):

     folder = os.path.abspath(folder) # make sure folder is absolute

     #####  Walk the entire folder tree and compress the files in each folder.
     for foldername, subfolders, filenames in os.walk(folder):
           for filename in filenames:
               if filename.endswith('.zip'):
                 print('This is %s Inside %s...' % (filename, foldername))
                 if not os.path.exists(foldername + '/' + filename): 
                   shutil.copy(foldername + '/' + filename, folder)
     print('Done.')


selective('.')
