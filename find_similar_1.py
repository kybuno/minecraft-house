#choose one target image. 
#moves images in the folder that are similar to that image, into a new folder! yipee

from PIL import Image
from image_functions import get_image_list, downsize, difference, difference2
from os.path import join
from itertools import combinations
import time, os, shutil

start_time=time.time()
#downsize images
foldername=input("enter folder name here: ")
image_list=get_image_list(foldername)
similar_list=[]

target_img=input("enter name of target image: ")
target_d=downsize(join(foldername,target_img))

for img2 in image_list:
    img2_d=downsize(join(foldername,img2))

    if target_d.size != img2_d.size:
        print(f"Resizing images: {target_d.size} vs {img2_d.size}")
        img2_d = img2_d.resize(target_d.size)  # Resize img2 to match img1's size

    # Check if the modes match
    if target_d.mode != img2_d.mode:
        print(f"Converting image modes: {target_d.mode} vs {img2_d.mode}")
        img2_d = img2_d.convert(target_d.mode)

    if target_d.mode=="RGB":
        diff=difference2(target_d,img2_d)
    else:
        diff=difference(target_d,img2_d)
    if diff<0.15:
        similar_list.append(img2)

if len(similar_list)>0:
    new_folder=input("enter name of new folder to move similar images to: ")
    new_folder_path=join(foldername,new_folder)
    os.makedirs(new_folder_path,exist_ok=True)

    for img in similar_list:
        img_path=join(foldername,img)
        shutil.move(img_path, os.path.join(new_folder_path, os.path.basename(img_path)))
        
print(similar_list)
end_time=time.time()
time_taken=end_time-start_time
print(f"Time taken: {time_taken:.2f} seconds")