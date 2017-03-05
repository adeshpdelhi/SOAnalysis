import sys
from nltk.corpus import stopwords
stops = set(stopwords.words("english"))


answers = ["NullPointerExceptions are exceptions that occur when you try to use a reference that points to no location in memory (null) as though it were referencing an object Calling a method on a null reference or trying to access a field of a null reference will trigger a NullPointerException memory null unallocated"]

min_len=3
sentences=[]
with open( 'answer.txt', 'r' ) as f:
    lines = f.readlines()

for line in lines:
	tokens = line.split(' ')
	temp_tokens = []
	for t in tokens:
		if(len(t)>=min_len):
			temp_tokens = temp_tokens + [t]
	temp_tokens = [w for w in temp_tokens if not w in stops]
	sentences = sentences + [temp_tokens]

#print sentences


num_features = 30    # Word vector dimensionality                      
min_word_count = 1   # Minimum word count                        
num_workers = 2      # Number of threads to run in parallel
context = 5          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

from gensim.models import word2vec
print "Training model..."
model = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

model.init_sims(replace=True)

model_name = "Samplemodel"
model.save(model_name)
x=model.most_similar(positive=['null'])

y=[]
print '..........'
for i in x:
	y=y+[i[1]];

print y;

