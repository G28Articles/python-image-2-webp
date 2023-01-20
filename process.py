import os
from PIL import Image

path = "./images/"
width = 1200

try:
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            print("lendo arquivo " + filename)
            im = Image.open(os.path.join(path, filename))
            aspect_ratio = im.height / im.width
            height = int(width * aspect_ratio)
            im = im.resize((width, height), Image.ANTIALIAS)
            im.save(os.path.join(path, filename + "_resized.png"))
            im2 = Image.open(os.path.join(path, filename + "_resized.png"))
            im2.save(os.path.join(path, filename.replace(".png", ".webp")), "webp")
        print("Images converted to WebP successfully!")
except Exception as error:
    print(error.args)
