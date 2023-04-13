import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
ss = SnowballStemmer(language= "english")
fhand = pd.read_csv("C:/Users/DELL/Desktop/smartwatches.csv",nrows = 10)
print(fhand)
print(word_tokenize(fhand))
for i in fhand:
    print(ss.stem(fhand)) 
for j in range(1):
    text_tokens = word_tokenize(fhand)
file_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(file_without_sw)        


