import glob
import numpy as np
import os
from PIL import Image
import sys



def preprocess(src_folder = "png_files/", dest_folder = "thesis_processed_imgs/"):
    if not os.path.isdir(dest_folder):
        os.mkdir(dest_folder)
        print("[INFO]", dest_folder,"created")


    def add_borders(im):
        old_size = im.size
        new_size = (1024, 1024)
        new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
        new_im.paste(im, (int((new_size[0]-old_size[0])/2),int((new_size[1]-old_size[1])/2)))
        return new_im


    paths = glob.glob(src_folder+"*2D*.png")
    if len(paths) == 0:
        print("[ERROR]", src_folder, "is empty." )
        print(len(paths))
        return 0

    for path in paths:
        print(path)
        fname = path.split("/")[-1][:-4]
        im = Image.open(path)
        im = add_borders(im)
        im.save(dest_folder + f"{fname}.png")


    paths = glob.glob(src_folder + "*3D*.png")
    for path in paths:
        print(path)
        fname = path.split("/")[-1][:-4]
        try:
            im = Image.open(path)
            width, height = im.size
            im1 = im.crop((0, 0, width/2, height)).rotate(180)
            im2 = im.crop((width/2, 0, width, height))
            im1 = add_borders(im1)
            im2 = add_borders(im2)
            im1.save(dest_folder + f"{fname}_left.png")
            im2.save(dest_folder + f"{fname}_right.png")
        except:
            print("[WARNING] problem with ", path)


if __name__ == '__main__':
    if sys.argv == 0:
        preprocess()
    else:
        preprocess(sys.argv[1],sys.argv[2])
    print("[SUCCESS] preprocess done")
