from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
fin = open('out_posts_20000.txt', 'r')
min_len = 3
sentences = []

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

for line in fin:
	line = fix_line(line)
	sentences = sentences + [line.split(" ")]
	# tokens = line.split(' ')
	# temp_tokens = []
	# for t in tokens:
	# 	if(len(t)>=min_len):
	# 		temp_tokens = temp_tokens + [t]
	# temp_tokens = [w for w in temp_tokens if not w in stops]
	# sentences = sentences + [temp_tokens]
# fin.close()

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
model_name = "SO20000Qmodel"
model.save(model_name)