import glob
import re
import collections
import operator

global_vocabulary_dict = {}

from nltk.corpus import stopwords
stops = set(stopwords.words("english"))

for filename in glob.glob('out_posts_20000.txt'):
	fin = open(filename, "r")
	for line in fin:
		line = line.lower()
		line = re.sub(r"[^ a-zA-Z\n]"," ",line)
		line = line.replace("\n"," ")
		words = line.split(" ")
		words = [w for w in words if not w in stops]
		for word in words:
			if word not in global_vocabulary_dict:
				global_vocabulary_dict[word] = 1
			else:
				global_vocabulary_dict[word] +=1
	fin.close()

# print collections.OrderedDict(sorted(global_vocabulary_dict.items()))
print sorted(global_vocabulary_dict.items(), key=operator.itemgetter(1))