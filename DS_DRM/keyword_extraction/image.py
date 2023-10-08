from PIL import Image
import docx2txt
import pytesseract
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS


keywords = []
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
file = 'Shakespeare_trial_1916.jpg'
img1 = np.array(Image.open(file))
text = pytesseract.image_to_string(img1)
total_words = text.split()
total_word_length = len(total_words)

import yake
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

language = "en"

deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = int(total_word_length*0.15)
text_keywords = []
kw_extractor = yake.KeywordExtractor(stopwords = stop_words, n=1, top = numOfKeywords )
keywords = kw_extractor.extract_keywords(text)
for kw in keywords:
  text_keywords.append(kw[0])

print(text_keywords)


# path = "files"
# dir_list = os.listdir(path)
# # print(len(dir_list))
# for file in dir_list:
#     filename = file.split(".")
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

