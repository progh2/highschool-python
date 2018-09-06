import xml.etree.ElementTree as ET
import codecs

f = codecs.open('movie.xml', encoding="UTF-8")
str = f.read()

tree = ET.ElementTree(ET.fromstring(str))
root = tree.getroot()

print(root.tag)

for child in root:
    print("tag : " + child.tag + " : " + child.text)