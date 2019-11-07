import re
import csv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from nltk.corpus import stopwords
from datetime import datetime

# nltk.download('stopwords')
BLACKLIST = stopwords.words("german")
BLACKLIST.extend(["mal","ok","schon",":d","grad","hast","halt","2","geht","jo","!","ned","3","grade","bisschen","mehr","1","eigtl","is","vll","kannst","mach","immer","ganz","ab","kommt","nochmal","richtig","5","erstmal","nix","jez","gemacht","gehen","macht","geh","hey","kommen","jop",";d","gibt","haste","gar","ziemlich wäre","4","10","au","-","willst","warum","nem","gesagt","n","okay","wegen"])

mask = np.array(Image.open("mask-zerg.png"))

messages = csv.reader(open("chat.csv", "r"))
next(messages)

# Count words
worddict = {}
for message in messages:
    for word in message[4].split():
        if not word in BLACKLIST:
            if word in worddict:
                worddict[word] += 1
            else:
                worddict[word] = 1

wordcloud = WordCloud(max_words = 10000, mask = mask, background_color = "white", contour_width = 1, contour_color = 'black')
wordcloud.generate_from_frequencies(frequencies = worddict)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
