import os
from PIL import Image

path = "./images/"
width = 1200
extension = ".png"

def convert_to_webp():
    try:
        for filename in os.listdir(path):
            if filename.endswith(extension):
                print("lendo arquivo " + filename)
                im = Image.open(os.path.join(path, filename))
                aspect_ratio = im.height / im.width
                height = int(width * aspect_ratio)
                im = im.resize((width, height), Image.LANCZOS)
                im.save(os.path.join(path, filename + "_resized" + extension))
                im2 = Image.open(os.path.join(path, filename + "_resized" + extension))
                im2.save(os.path.join(path, filename.replace(extension, ".webp")), "webp")
            print("Images converted to WebP successfully!")
    except Exception as error:
        print(error.args)


if __name__ == "__main__":
    convert_to_webp()