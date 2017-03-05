from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
import re
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
fin = open('SO3826Q.txt', 'r')
min_len = 3
sentences = []

for line in fin:
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
	temp_tokens = [w for w in temp_tokens if not w in stops]
	sentences = sentences + [temp_tokens]
print sentences

fin.close()

# Import the built-in logging module and configure it so that Word2Vec 
# creates nice output messages
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)

# Set values for various parameters
num_features = 300    # Word vector dimensionality                      
min_word_count = 200   # Minimum word count                        
num_workers = 2      # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

# Initialize and train the model (this will take some time)
from gensim.models import word2vec
print "Training model..."
model = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

# If you don't plan to train the model any further, calling 
# init_sims will make the model much more memory-efficient.
model.init_sims(replace=True)

# It can be helpful to create a meaningful model name and 
# save the model for later use. You can load it later using Word2Vec.load()
print "similarity = .. "
print model.similarity('java', 'class')
model_name = "SO3826Qmodel"
model.save(model_name)


