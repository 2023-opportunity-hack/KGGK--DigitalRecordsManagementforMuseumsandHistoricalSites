from PIL import Image
from PIL.ExifTags import TAGS
import os

path = "files"
dir_list = os.listdir(path)
# print(len(dir_list))
for file in dir_list:
    filename = file.split(".")
    image_metadata = {}
    image_metadata['filename'] = filename
    if(filename.pop() == 'jpg'):
        image = Image.open('files/'+file)
        exifdata = image.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            if(tag == 'DateTime'):
                image_metadata['DateTime'] = exifdata[306]
            if(tag=='ImageDescription'):
                image_metadata['description'] = exifdata[270]
    print(image_metadata)