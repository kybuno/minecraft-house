import os
from os import listdir
from os.path import join

def rename_files(folder,newname):
    x=1
    for f in listdir(folder):
        old_filepath=join(folder,f)
        extension=f.split(".")[-1]
        new_filepath=f"{join(folder,newname)}_{x}.{extension}"

        os.rename(old_filepath,new_filepath)
        print(new_filepath)
        x+=1

folder=input("please enter the name of the folder containing files to be renamed: ")
newname=input("please enter the new name you would like for the files: ")

rename_files(folder,newname)