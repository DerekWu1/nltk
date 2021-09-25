from nltk.tokenize import word_tokenize
import numpy as np

import pandas as pd
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown

brown.words()

1+1

print("Hello world!")

sample_text = "Hello there, how are you doing today? The weather is great and Python is awesome."

print(sent_tokenize(sample_text))

print(word_tokenize(sample_text))


sample_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(sample_sentence)

print(stop_words)

filtered_sentence = []

#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)

p#rint(filtered_sentence)

# list comprehension is a better pythonic way 

filtered_sentence = [w for w in words if not w in stop_words]

filtered_sentence

print(filtered_sentence)


###############################################################

######### Stemming, for two words that mean the same thing ####

###############################################################

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly","pythonista"]

for w in example_words:
    print(ps.stem(w))

stemmed = [print(ps.stem(w)) for w in example_words]

new_text = "It is very important to be pythonly while you are pythoning with python. All Pythoners have pythoned in a pythonic fashion."
words = word_tokenize(new_text)

stemmed2 = [print(ps.stem(w)) for w in words]

###############################################################

######### Stemming, for two words that mean the same thing ####

###############################################################

