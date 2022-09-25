#exif_info.py


from PIL import Image, ExifTags
from pprint import pprint

def misc_info(path):
    img = Image.open(path)
    exif = {
    ExifTags.TAGS[k]: v
    for k , v in img._getexif().items()
    if k in ExifTags.TAGS
    }

    if exif:
        return(exif)
    else:
        print("No data")