import os
import shutil
import time

def backupFiles():
    deleted_files= 0
    deleted folders= 0

    path= '/Practice'

    days= 30

    seconds = time.time()- (days*24*60*60)

    if os.path.exists(path):
        for folders, files, root_folders in os.walk(path):
            
            if seconds>= get_file_or_folder_age(root_folder):
                
                remove_folder(root_folder)
                deleted_folders_count+=1
