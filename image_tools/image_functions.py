from os import listdir

#get list of png and jpg files in folder
def get_image_list(foldername):
    imagelist=[x for x in listdir(foldername) if x[-4:]==(".png" or ".jpg")]
    return(imagelist)


from PIL import Image

def downsize(img):
    #downsize screenshot into 16 by 9 pixcls
    bigpic=Image.open(img)
    downsized=bigpic.resize((16,9))
    return downsized


colour=tuple[int,int,int]
#theory only, dont want to do it one by one irl
#find the difference between a single pixel for pic 1 and pic 2
def pixeldifference(p1: colour, p2: colour) -> colour:
    r1,g1,b1=p1
    r2,g2,b2=p2
    r,g,b=abs(r1-r2),abs(g1-g2),abs(b1-b2)
    return (r,g,b)


from itertools import product
from PIL import Image, ImageChops

def difference (img1: Image.Image, img2: Image.Image) -> float:
    #find diff btwn two images,
    #average the difference for all 16 x 9 pixels
    diff = ImageChops.difference(img1,img2) 
    #returns abs val. of diff btwn all pixels

    total=0
    width,height=diff.size
    for w,h in product(range(width),range(height)):
        #product(A,B) returns same as ((x,y) for x in A for y in B)
        r, g, b, _ = diff.getpixel((w,h))
        total+=(r+g+b)/3

    average_diff=total/(width*height)
    normalized_diff=average_diff/255
    return round(normalized_diff,3)

def difference2 (img1: Image.Image, img2: Image.Image) -> float:
    #find diff btwn two images,
    #average the difference for all 16 x 9 pixels
    diff = ImageChops.difference(img1,img2) 
    #returns abs val. of diff btwn all pixels

    total=0
    width,height=diff.size
    for w,h in product(range(width),range(height)):
        #product(A,B) returns same as ((x,y) for x in A for y in B)
        r, g, b = diff.getpixel((w,h))
        total+=(r+g+b)/3

    average_diff=total/(width*height)
    normalized_diff=average_diff/255
    return round(normalized_diff,3)