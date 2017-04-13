# import compute_tfidf

import sys

fin1 = open('core_java1.txt','r')
fin2 = open('core_java2.txt','r')

# keywords = ["unallocated", "memory", "access", "null", "pointer", "exception"]

# answers = ["Encapsulation is a strategy used as part of abstraction\n Encapsulation refers to the state of objects - objects encapsulate their state and hide it from the outside; outside users of the class interact with it through its methods, but cannot access the classes state directly\n So the class abstracts away the implementation details related to its state\n Abstraction is a more generic term, it can also be achieved by (amongst others) subclassing\n For example, the interface List in the standard library is an abstraction for a sequence of items, indexed by their position, concrete examples of a List are an ArrayList or a LinkedList\n Code that interacts with a List abstracts over the detail of which kind of a list it is using\n Abstraction is often not possible without hiding underlying state by encapsulation - if a class exposes its internal state, it can't change its inner workings, and thus cannot be abstracted\n Abstraction is the concept of describing something in simpler terms, i\ne abstracting away the details, in order to focus on what is important (This is also seen in abstract art, for example, where the artist focuses on the building blocks of images, such as colour or shapes)\n The same idea translates to OOP by using an inheritance hierarchy, where more abstract concepts are at the top and more concrete ideas, at the bottom, build upon their abstractions\n At its most abstract level there is no implementation details at all and perhaps very few commonalities, which are added as the abstraction decreases\n As an example, at the top might be an interface with a single method, then the next level, provides several abstract classes, which may or may not fill in some of the details about the top level, but branches by adding their own abstract methods, then for each of these abstract classes are concrete classes providing implementations of all the remaining methods\n Encapsulation is a technique\n It may or may not be for aiding in abstraction, but it is certainly about information hiding and/or organisation\n It demands data and functions be grouped in some way - of course good OOP practice demands that they should be grouped by abstraction\n However, there are other uses which just aid in maintainability etc\n"]

# answers = ["Abstract class can have abstract and non-abstract methods.	Interface can have only abstract methods. Since Java 8, it can have default and static methods also. Abstract class doesn't support multiple inheritance.	Interface supports multiple inheritance. Abstract class can have final, non-final, static and non-static variables.	Interface has only static and final variables. Abstract class can provide the implementation of interface.	Interface can't provide the implementation of abstract class. The abstract keyword is used to declare abstract class. The interface keyword is used to declare interface. Methods of a Java interface are implicitly abstract and cannot have implementations. A Java abstract class can have instance methods that implements a default behaviour. Variables declared in a Java interface are by default final. An abstract class may contain non-final variables. Members of a Java interface are public by default. A Java abstract class can have the usual flavours of class members like private, protected, etc. A Java interface should be implemented using keyword “implements”; A Java abstract class should be extended using keyword “extends”. An interface can extend another Java interface only, an abstract class can extend another Java class and implement multiple Java interfaces. A Java class can implement multiple interfaces but it can extend only one abstract class."]

answers = [" Constructor in java is a special type of method that is used to initialize the object. Java constructor is invoked at the time of object creation. It constructs the values ie provides data for the object that is why it is known as constructor. Constructor name must be same as its class name. Constructor must have no explicit return type"]

# answers = ["Inheritance in java is a mechanism in which one object acquires all the properties and behaviors of parent object. The idea behind inheritance in java is that you can create new classes that are built upon existing classes. When you inherit from an existing class, you can reuse methods and fields of parent class, and you can add new methods and fields also. Inheritance represents the IS-A relationship, also known as parent-child relationship. Why use inheritance? For Method Overriding (so runtime polymorphism can be achieved). For Code Reusability. Keyword extends. Types single multilevel hierarchical multiple hybrid"]

# answers = ["Nested classes represent a special type of relationship that is it can access all the members (data members and methods) of outer class including private. Nested classes are used to develop more readable and maintainable code because it logically group classes and interfaces in one place only. Code Optimization: It requires less code to write."]

s1 = fin1.readlines()
s2 = fin2.readlines()
fin1.close()
fin2.close()

# import re
# from nltk.stem.wordnet import WordNetLemmatizer
# lmtzr = WordNetLemmatizer()

# def fix_line(line):
# 	line = line.lower()
# 	line = re.sub(r"[^ a-zA-Z\n]"," ",line)
# 	line = line.replace("\n"," ")
# 	words = line.split(" ")
# 	words = [w for w in words if not w in stops]
# 	line = ""
# 	for word in words:
# 		if(len(word)>0):
# 			noun_lmtzr = lmtzr.lemmatize(word,'n').encode('ascii')
# 			verb_lmtzr = lmtzr.lemmatize(word,'v').encode('ascii')
# 			if(len(word)!= len(noun_lmtzr)):
# 				line = line + " "+ noun_lmtzr
# 			else:
# 				line = line + " "+ verb_lmtzr
# 	return line

# import string
# s1 = string.replace(s1, '\n', '')
# s2 = string.replace(s2, '\n', '')

from nltk.corpus import stopwords
stops = set(stopwords.words("english"))
keywords = []

for i in range(len(answers)):
	temp_tokens = [w for w in compute_tfidf.fix_line(answers[i]).split(" ") if not w in stops]
	keywords = keywords + temp_tokens

keywords = set(keywords)
print keywords


for i in range(len(s1)):
	s1[i] = compute_tfidf.fix_line(s1[i])

weighted_dictionary = compute_tfidf.get_weighted_dictionary(compute_tfidf.fix_line(answers[0]))

def convertToDictionary(items):
	counts = dict()
	for i in items:
		counts[i] = counts.get(i, 0) + 1
	return counts


keywords_found = []
keywords_found_total = []

window_size = 3
threshold_minimum_score_to_qualify_as_match = 1.5

max1 = -1
max1i = -1

total_matches = 0

sentences = answers[0].split(".")
for s in range(len(sentences)):
	sentences[s] = compute_tfidf.fix_line(sentences[s])

maxes = []
keywords_found_combined_sentences = []

for sentence_iter in range(len(sentences)):
	########Modification for sentence level
	sentence_keywords = sentences[sentence_iter].split(" ")
	sentence_keywords = set(sentence_keywords)
	sentence_keywords = keywords.intersection(sentence_keywords)
	print sentence_iter,sentences[sentence_iter]
	print sentence_keywords
	###########Modification end
	max1 = -1
	for i in range(len(s1)):
		if(i%1000 == 0):
			print i
			sys.stdout.flush()
		counter = 0
		keywords_found_temp = []
		for j in range(window_size):
			if(i+j>=len(s1)):
				break
			for word in s1[i+j].split(" "):
				if(word in sentence_keywords and word in weighted_dictionary):
					counter = counter + weighted_dictionary[word]
					keywords_found_temp = keywords_found_temp + [word]
		if(counter > max1):
			max1i = i
			keywords_found = keywords_found_temp
		max1 = max(max1, counter)
		if(counter>threshold_minimum_score_to_qualify_as_match):
			total_matches+=1
			keywords_found_total = keywords_found_total + keywords_found_temp
	maxes.append(max1)
	keywords_found_combined_sentences = keywords_found_combined_sentences + keywords_found

print maxes
print sum(maxes)
print convertToDictionary(keywords_found_combined_sentences)
print total_matches
print convertToDictionary(keywords_found_total)