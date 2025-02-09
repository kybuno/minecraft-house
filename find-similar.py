#i want to find groups of similar images in python!
#maybe with a UI someday?

#returns a list of image pairs sorted by similarity! 
# lowest number means closest similarity

from PIL import Image
from image_functions import get_image_list, downsize, difference
from os.path import join
from itertools import combinations
import time

start_time=time.time()
#downsize images
foldername=input("enter folder name here: ")
image_list=get_image_list(foldername)
similarity=[]

for img1, img2 in (combinations(image_list, 2)):
    img1_d=downsize(join(foldername,img1))
    img2_d=downsize(join(foldername,img2))

    diff=difference(img1_d,img2_d)
    similarity.append((diff,img1,img2))

similarity.sort(key=lambda x: x[0], reverse=True)
print(similarity)
end_time=time.time()
time_taken=end_time-start_time
print(f"Time taken: {time_taken:.2f} seconds")