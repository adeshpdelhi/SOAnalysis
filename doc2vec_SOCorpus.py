from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
fin = open('out_posts_20000.txt', 'r')

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
			noun_lmtzr = lmtzr.lemmatize(word,'n')
			verb_lmtzr = lmtzr.lemmatize(word,'v')
			if(len(word)!= len(noun_lmtzr)):
				line = line + " "+ noun_lmtzr
			else:
				line = line + " "+ verb_lmtzr
	return line

from gensim.models.doc2vec import LabeledSentence
label = 0
min_len = 3
sentences = []
for line in fin:
	# line = fix_line(line)
	label = label + 1
	sentences = sentences + [LabeledSentence(words=line.split(" "), tags = [u"SENT_"+str(label)])]
	# tokens = line.split(' ')
	# temp_tokens = []
	# for t in tokens:
	# 	if(len(t)>=min_len):
	# 		temp_tokens = temp_tokens + [t]
	# temp_tokens = [w for w in temp_tokens if not w in stops]
	# sentences = sentences + [temp_tokens]
# fin.close()

answer = "Encapsulation is a strategy used as part of abstraction. Encapsulation refers to the state of objects - objects encapsulate their state and hide it from the outside; outside users of the class interact with it through its methods, but cannot access the classes state directly. So the class abstracts away the implementation details related to its state. Abstraction is a more generic term, it can also be achieved by (amongst others) subclassing. For example, the interface List in the standard library is an abstraction for a sequence of items, indexed by their position, concrete examples of a List are an ArrayList or a LinkedList. Code that interacts with a List abstracts over the detail of which kind of a list it is using. Abstraction is often not possible without hiding underlying state by encapsulation - if a class exposes its internal state, it can't change its inner workings, and thus cannot be abstracted."
# sentences = sentences + [LabeledSentence(words=fix_line(answer).split(" "), tags = [u"ANSWER"])]
sentences = sentences + [LabeledSentence(words=answer.split(" "), tags = [u"ANSWER"])]

# Import the built-in logging module and configure it so that Word2Vec 
# creates nice output messages
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)

# Set values for various parameters
num_features = 500    # Word vector dimensionality                      
min_word_count = 100   # Minimum word count                        
num_workers = 4      # Number of threads to run in parallel
context = 15          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
from gensim.models import doc2vec
print "Training model..."
model = doc2vec.Doc2Vec(workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling) #, alpha = 0.025, min_alpha = 0.025
model.build_vocab(sentences)
for epoch in range(3):
    model.train(sentences)
    model.alpha -= 0.002  # decrease the learning rate
    model.min_alpha = model.alpha  # fix the learning rate, no decay

model.docvecs.most_similar("ANSWER");	

# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
model_name = "SO20000QDoc2Vecmodel"
model.save(model_name)