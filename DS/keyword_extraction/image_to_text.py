from PIL import Image
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
filename = 'Shakespeare_trial_1916.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

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
numOfKeywords = 20

kw_extractor = yake.KeywordExtractor(stopwords = stop_words, n=1)
keywords = kw_extractor.extract_keywords(text)
for kw in keywords:
  print(kw[0])