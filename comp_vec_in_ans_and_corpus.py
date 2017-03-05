import sys
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import re
import math
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
stops = set(stopwords.words("english"))
model_corpus = Word2Vec.load("SO3826Qmodel")

answers = ["NullPointerExceptions are exceptions that occur when you try to use a reference that points to no location in memory (null) as though it were referencing an object Calling a method on a null reference or trying to access a field of a null reference will trigger a NullPointerException memory null unallocated"]

min_len=3
sentences=[]
with open( 'answer.txt', 'r' ) as f:
    lines = f.readlines()
words_answer=[]
for line in lines:
	tokens = line.split(' ')
	temp_tokens = []
	for t in tokens:
		if(len(t)>=min_len):
			noun_lmtzr = lmtzr.lemmatize(t,'n').encode('ascii')
			verb_lmtzr = lmtzr.lemmatize(t,'v').encode('ascii')
			if(len(t)!= len(noun_lmtzr)):
				temp_tokens = temp_tokens + [noun_lmtzr]
			else:
				temp_tokens = temp_tokens + [verb_lmtzr]
			words_answer=words_answer+[t]
	temp_tokens = [w for w in temp_tokens if not w in stops]
	sentences = sentences + [temp_tokens]

#print sentences


num_features = 30    # Word vector dimensionality                      
min_word_count = 1   # Minimum word count                        
num_workers = 2      # Number of threads to run in parallel
context = 4          # Context window size                                                                                  
downsampling = 1e-3   # Downsample setting for frequent words

from gensim.models import word2vec
print "Training model..."
model_answer = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

model_answer.init_sims(replace=True)
model_name = "Answermodel"
model_answer.save(model_name)
#x=model_answer.most_similar(positive=['null'])
#print x

squared_sum=0;
dist=[]
key_words_in_answers=[val for val in words_answer if not val in stops]
for word in key_words_in_answers:
	if(model_corpus.most_similar(positive=[word]) != None and model_answer.most_similar(positive=[word]) != None):
		x=model_corpus.most_similar(positive=[word])
		y=model_answer.most_similar(positive=[word])


		x_word=[]
		y_word=[]

		for i in x:
			x_word=x_word+[i[0]]
		for i in y:
			y_word=y_word+[i[0]]

		common_words = [val for val in x_word if val in y_word]

		for w in common_words:
			v1=v2=0
			for a in x:
				if(a[0][0].lower() == w.lower()):
					v1=a[0][1]
					break;
			for b in y:
				if(b[0][0].lower == w.lower()):
					v2=b[0][1]
					break;

			squared_sum=v1^2+v2^2

		euclidean_distance=math.sqrt(squared_sum)
		print word
		print "./."
		print euclidean_distance
		dist=dist+[euclidean_distance];

print dist




