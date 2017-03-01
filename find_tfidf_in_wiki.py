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


def get_weighted_dictionary(answer):
	global bloblist
	print ("Building dictionary")
	bloblist = [tb(fix_line(answer))] + bloblist
	weighted_dictionary = compute_weighted_dictionary(bloblist)
	print ("Dictionary built")

bloblist = []
fin = open('out_posts_20000.txt', "r")
# fin = open('SO500Q.txt', "r")
for line in fin:
	line = fix_line(line)
	bloblist = bloblist + [tb(line)]
fin.close()

print ("Import finished")

def compute_weighted_dictionary(bloblist):
	weighted_dictionary = {}
	# bloblist = [document1, document2, document3]
	for i, blob in enumerate(bloblist):
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:10]:
			print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
			weighted_dictionary[word] = round(score, 5)
		break
	print weighted_dictionary
	return weighted_dictionary

if __name__ == "__main__":
	answer = [tb(fix_line("Encapsulation is a strategy used as part of abstraction. Encapsulation refers to the state of objects - objects encapsulate their state and hide it from the outside; outside users of the class interact with it through its methods, but cannot access the classes state directly. So the class abstracts away the implementation details related to its state.Abstraction is a more generic term, it can also be achieved by (amongst others) subclassing. For example, the interface List in the standard library is an abstraction for a sequence of items, indexed by their position, concrete examples of a List are an ArrayList or a LinkedList. Code that interacts with a List abstracts over the detail of which kind of a list it is using.Abstraction is often not possible without hiding underlying state by encapsulation - if a class exposes its internal state, it can't change its inner workings, and thus cannot be abstracted.Abstraction is the concept of describing something in simpler terms, i.e abstracting away the details, in order to focus on what is important (This is also seen in abstract art, for example, where the artist focuses on the building blocks of images, such as colour or shapes). The same idea translates to OOP by using an inheritance hierarchy, where more abstract concepts are at the top and more concrete ideas, at the bottom, build upon their abstractions. At its most abstract level there is no implementation details at all and perhaps very few commonalities, which are added as the abstraction decreases.As an example, at the top might be an interface with a single method, then the next level, provides several abstract classes, which may or may not fill in some of the details about the top level, but branches by adding their own abstract methods, then for each of these abstract classes are concrete classes providing implementations of all the remaining methods.Encapsulation is a technique. It may or may not be for aiding in abstraction, but it is certainly about information hiding and/or organisation. It demands data and functions be grouped in some way - of course good OOP practice demands that they should be grouped by abstraction. However, there are other uses which just aid in maintainability etc."))]
	get_weighted_dictionary(answer)

