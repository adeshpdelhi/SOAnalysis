fout = open('out_comments.txt','w')
from xml.dom import minidom
xmldoc = minidom.parse('comments.xml')
rowlist = xmldoc.getElementsByTagName('row')
print(len(rowlist))
for s in rowlist:
    fout.write(s.attributes['Body'].value+'\n')
fout.close()