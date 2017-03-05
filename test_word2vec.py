from gensim import models
from gensim.models import Word2Vec

model = Word2Vec.load("SO3826Qmodel")

print "similarity = .. "
w='exceptions'
print model.most_similar(positive=[w])