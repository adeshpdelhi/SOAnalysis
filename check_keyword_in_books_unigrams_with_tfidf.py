import find_tfidf_in_wiki

import sys

fin1 = open('core_java1.txt','r')
fin2 = open('core_java2.txt','r')

# keywords = ["unallocated", "memory", "access", "null", "pointer", "exception"]

answers = ["Encapsulation is a strategy used as part of abstraction\n Encapsulation refers to the state of objects - objects encapsulate their state and hide it from the outside; outside users of the class interact with it through its methods, but cannot access the classes state directly\n So the class abstracts away the implementation details related to its state\n Abstraction is a more generic term, it can also be achieved by (amongst others) subclassing\n For example, the interface List in the standard library is an abstraction for a sequence of items, indexed by their position, concrete examples of a List are an ArrayList or a LinkedList\n Code that interacts with a List abstracts over the detail of which kind of a list it is using\n Abstraction is often not possible without hiding underlying state by encapsulation - if a class exposes its internal state, it can't change its inner workings, and thus cannot be abstracted\n Abstraction is the concept of describing something in simpler terms, i\ne abstracting away the details, in order to focus on what is important (This is also seen in abstract art, for example, where the artist focuses on the building blocks of images, such as colour or shapes)\n The same idea translates to OOP by using an inheritance hierarchy, where more abstract concepts are at the top and more concrete ideas, at the bottom, build upon their abstractions\n At its most abstract level there is no implementation details at all and perhaps very few commonalities, which are added as the abstraction decreases\n As an example, at the top might be an interface with a single method, then the next level, provides several abstract classes, which may or may not fill in some of the details about the top level, but branches by adding their own abstract methods, then for each of these abstract classes are concrete classes providing implementations of all the remaining methods\n Encapsulation is a technique\n It may or may not be for aiding in abstraction, but it is certainly about information hiding and/or organisation\n It demands data and functions be grouped in some way - of course good OOP practice demands that they should be grouped by abstraction\n However, there are other uses which just aid in maintainability etc\n Abstraction is the process of refining away all the unneeded/unimportant attributes of an object and keep only the characteristics best suitable for your domain\n E\ng\n for a person: you decide to keep first and last name and SSN\n Age, height, weight etc are ignored as irrelevant\n Abstraction is where your design starts\n Encapsulation is the next step where it recognizes operations suitable on the attributes you accepted to keep during the abstraction process\n It is the association of the data with the operation that act upon them\n I\ne\n data and methods are bundled together\n Abstraction is used to show important and relevant data to user\n best real world example In a mobile phone, you see their different types of functionalities as camera, mp3 player, calling function, recording function, multimedia etc\n It is abstraction, because you are seeing only relevant information instead of their internal engineering\n Encapsulation is hiding unnecessary data in a capsule or unit\n Abstraction is showing essential feature of an object\n Encapsulation is used to hide its member from outside class and interface\nUsing access modifiers provided in c#\nlike public,private,protected etc\n   Abstraction is a very general term, and abstraction in software is not limited to object-oriented languages\n A dictionary definition: the act of considering something as a general quality or characteristic, apart from concrete realities, specific objects, or actual instances\n Assembly language can be thought of as an abstraction of machine code -- assembly expresses the essential details and structure of the machine code, but frees you from having to think about the opcodes used, the layout of the code in memory, making jumps go to the right address, etc\n Your operating system's API is an abstraction of the underlying machine\n Your compiler provides a layer of abstraction which shields you from the details of assembly language\n The TCP/IP stack built into your operating system abstracts away the details of transmitting bits over a network\n If you go down all the way to the raw silicon, the people who designed your CPU did so using circuit diagrams written in terms of diodes and transistors, which are abstractions of how electrons travel through semiconductor crystals\n In software, everything is an abstraction\n We build programs which simulate or model some aspect of reality, but by necessity our models always abstract away some details of the real thing\n We build layer on layer on layer of abstractions, because it is the only way we get anything done\n (Imagine you were trying to make, say, a sudoku solver, and you had to design it using only semiconductor crystals\n OK, I need a piece of N-type silicon here\n\n\n)In comparison, encapsulation is a very specific and limited term\n Some of the other answers to this question have already given good definitions for it\n In Object oriented programming, we have something called classes\n What are they for? They are to store some state and to store some methods to change that state i\ne\n, they are encapsulating state and its methods\n It(class) does not care about the visibility of its own or of its contents\n If we choose to hide the state or some methods, it is information hiding\n Now, take the scenario of an inheritance\n We have a base class and a couple of derived (inherited) classes\n So, what is the base class doing here? It is abstracting out some things from the derived classes\n   Encapsulation - the process of hiding components of the class to prevent direct access from the outside\n It is achieved by using private modifier to prevent direct access to some class members (data field or method) from other classes or objects meanwhile providing access to these private members by public members (Interface)\n That make the class members protected as human organs hidden/encapsulated under the skin or some shield\n  Abstraction - A principle must be followed in writing OOP program that say you must include in the class only components that are interesting in the task of the program\n For example: the object student has a lot of characters as a human: name, age, weight, hair color, eye color, etc\n But, when you create a class in OOP to work with students you should include only those characters that really matter for student database: name, age, specialty, level, marks \n\n\n etc\n in C++ you can create abstract class by using the modifier virtual with any methods in the class and that will make it unusable in direct but you can derive other classes from it and create implementation for its members with adding required members based on the task\n  Abstraction:  Technical Definition :- Abstraction is a concept to hide unnecessary details(complex or simple) and only show the essential features of the object\n There is no implementaion here its just an concept  What it means practically:- When i say my company needs some medium/device so that employees can connect to customer \n This is the purest form of abstaction(like interface in java) as that device/medium can be phone or internet or skype or in person or email etc\n I am not going into nitty gritty of device/medium  Even when i say my company needs some medium/device so that employees can connect to customer through voice call\n Then also i am talking abstract but at bit lower level as device/medium can be phone or skype or something else etc  Now when i say my company needs some phone so that employees can connect to customer through voice call\n Then also i am talking abstract but at bit lower level as phone can be of any company like iphone or samsung or nokia etc  Encapsulation:- Its basically about hiding the state(information) of object with the help of modifiers like private,public,protected etc\n we expose the state thru public methods only if require\n  What it means practically:- Now when i say my company needs some iphone so that employees can connect to customer through voice call\nNow i am talking about some concrete object(like iphone)\n Even though i am not going into nitty gritty of iphone here too but iphone has some state/concrecrete info/implementation associated with it where device/medium does not have\n When i say concrete object, actually it means any object which has some(not complete like java abstract class) implementation/info associated with it\n  So iphone actually used here encapsulation as strategy to hide its state/information and expose only the ones which it think should be exposed\n So both abstraction and encapsulation hides some unnecessary details but abstraction at the concept level and encapsulation actually at implementation level"]

s1 = fin1.readlines()
s2 = fin2.readlines()

import re
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

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
	temp_tokens = [w for w in find_tfidf_in_wiki.fix_line(answers[i]).split(" ") if not w in stops]
	keywords = keywords + temp_tokens

keywords = set(keywords)
print keywords

keywords_found = []

theshold1 = 100

max1 = -1
max1i = -1

for i in range(len(s1)):
	s1[i] = find_tfidf_in_wiki.fix_line(s1[i])

weighted_dictionary = find_tfidf_in_wiki.get_weighted_dictionary(answers[0])

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
			if(word in keywords and word in weighted_dictionary):
				counter = counter + weighted_dictionary[word]
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