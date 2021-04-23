import os 
import shutil 
import time 
path = ""
days = 30
seconds = time.time()-(60*60*24*30)

if os.path.exists(path):
    for folder,file,rootfolder in os.walk(path):
        if seconds>folder_age(folder):
            remove_folder(folder)
        if seconds>folder_age(file):
            remove_file(file)
        if seconds>folder_age(rootfolder):
            remove_file(rootfolder)
else :
    for folder in folder:
      folder_path = os.path.join(rootfolder,folder)
      if seconds>folder_age(rootfolder):
          remove_folder(rootfolder)
def remove_folder(path):
    if not shutil.rmtree(path):
        print("{path}isremovedsuccesfully")
    else :
        print("Unable to delete the file")

def remove_file(path):
    if not os.remove(path):
       print("{path}isremovedsuccesfully")
    else :
        print("Unable to delete the file")

def folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime 