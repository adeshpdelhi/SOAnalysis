#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math
from textblob import TextBlob as tb

def tf(word, blob):
	return blob.words.count(word) / float(len(blob.words))

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
	return math.log(float(len(bloblist)) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)


document2 = tb("""Python, from the Greek word , is a genus of
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
recognised.[2] A member of this genus, P. reticulatus, is among the longest
snakes known.""")

import glob
import re
import collections
import operator

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
lmtzr = WordNetLemmatizer()

stops = set(stopwords.words("english"))

def fix_line(line):
	line = line.lower()
	line = re.sub(r"[^ a-zA-Z\n]"," ",line)
	line = line.replace("\n"," ")
	words = line.split(" ")
	words = [w for w in words if not w in stops]
	line = ""
	for word in words:
		if(len(word)>0):
			noun_lmtzr = lmtzr.lemmatize(word,'n').encode('ascii')
			verb_lmtzr = lmtzr.lemmatize(word,'v').encode('ascii')
			if(len(word)!= len(noun_lmtzr)):
				line = line + " "+ noun_lmtzr
			else:
				line = line + " "+ verb_lmtzr
	return line

bloblist = [tb(fix_line("Abstract class	Interface Abstract class can have abstract and non-abstract methods. Interface can have only abstract methods. Since Java 8, it can have default and static methods also. Abstract class doesn't support multiple inheritance.	Interface supports multiple inheritance. Abstract class can have final, non-final, static and non-static variables.	Interface has only static and final variables. 4) Abstract class can provide the implementation of interface.	Interface can't provide the implementation of abstract class. The abstract keyword is used to declare abstract class.	The interface keyword is used to declare interface."))]

fin = open('out_posts_20000.txt', "r")
for line in fin:
	line = fix_line(line)
	bloblist = bloblist + [tb(line)]
fin.close()

# bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
	print("Top words in document {}".format(i + 1))
	scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	for word, score in sorted_words[:10]:
		print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))