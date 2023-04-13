from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = "Natural Language Processing with Python provides a practical introduction to programming for language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more. The online version of the book has been been updated for Python 3 and NLTK 3. "
words = ["program", "programer", "programs", "programming", "programers"]
choice= int(input("Enter your choosen number:"))
choice_1 = word_tokenize
choice_2 = sent_tokenize
choice_3 = "original_text"
if choice == 1:
   print(word_tokenize(text))
elif choice == 2:
   print(sent_tokenize(text))
elif choice == 3:
   print(text)
    

         


