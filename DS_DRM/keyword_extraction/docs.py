import yake
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))
import aspose.words as aw
import os

doc = aw.Document("VillaGarden_pghistory.doc")
print(doc)
doc.save("doc-to-text.txt")

f = open("doc-to-text.txt", "r")
text = f.read()
f.close()
total_words = text.split()
total_word_length = len(total_words)
numOfKeywords = int(total_word_length*0.10)
kw_extractor = yake.KeywordExtractor(stopwords = stop_words, n=1, top=numOfKeywords)
keywords = kw_extractor.extract_keywords(text)
for kw in keywords:
  print(kw)

os.remove("doc-to-text.txt")