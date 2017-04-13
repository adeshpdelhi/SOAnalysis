import sys

fin1 = open('core_java1.txt','r')
fin2 = open('core_java2.txt','r')

# keywords = ["unallocated", "memory", "access", "null", "pointer", "exception"]

answers = ["NullPointerExceptions are exceptions that occur when you try to use a reference that points to no location in memory (null) as though it were referencing an object Calling a method on a null reference or trying to access a field of a null reference will trigger a NullPointerException memory null unallocated"]

s1 = fin1.readlines()
s2 = fin2.readlines()

import re
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

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

# import string
# s1 = string.replace(s1, '\n', '')
# s2 = string.replace(s2, '\n', '')

from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
keywords = []

for i in range(len(answers)):
	temp_tokens = [w for w in fix_line(answers[i]).split(" ") if not w in stops]
	keywords = keywords + temp_tokens

keywords = set(keywords)
print keywords

keywords_found = []

theshold1 = 50
theshold2 = 100

max1 = -1
max1i = -1
max2 = -1

for i in range(len(s1)):
	s1[i] = fix_line(s1[i])

for i in range(len(s1)):
	if(i%1000 == 0):
		print i
		sys.stdout.flush()
	counter = 0
	keywords_found_temp = []
	for j in range(theshold1):
		if(i+j>=len(s1)):
			break
		for word in s1[i+j].split(" "):
			if(word in keywords):
				counter = counter + 1
				keywords_found_temp = keywords_found_temp + [word]
	if(counter > max1):
		max1i = i
		keywords_found = keywords_found_temp
	max1 = max(max1, counter)

print max1
print "Index " + str(max1i)
print keywords_found
fin1.close()
fin2.close()