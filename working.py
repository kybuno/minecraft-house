from os import listdir
#from os.path import isfile, join

def get_image_list(foldername):

    #foldername=input("input target folder name: ")
    #foldername="test-images"
    #filelist= [f for f in listdir(foldername) if isfile(join(foldername, f))]

    imagelist=[x for x in listdir(foldername) if x[-4:]==(".png" or ".jpg")]
    #png or jpg files only!

    #print(listdir(foldername))
    return(imagelist)

