import requests
from bs4 import BeautifulSoup
import argparse


sites = ["www.tutorialspoint.com", "www.wikipedia.com", "stackoverflow.com", "javatpoint.com", "quora.com"]
for i in range(len(sites)):
	sites[i] = "site:"+sites[i]

questions = ["","null pointer exception", "anonymous inner class", "javafx", "inheritance", "static class",
"interface vs abstract class" ]

for question in questions:
	print question
	for i in range(len(sites)):
		try:
			r = requests.get('http://www.google.com/search',
			                 params={'q':question+' '+sites[i]
			                 # ,"tbs":"li:1"
			                         }
			                )

			soup = BeautifulSoup(r.text)
			count = soup.find('div',{'id':'resultStats'}).text.split('About ')[1].split(' results')[0]
			print sites[i].split("site:")[1]+' '+count
		except:
			pass
	print '\n'