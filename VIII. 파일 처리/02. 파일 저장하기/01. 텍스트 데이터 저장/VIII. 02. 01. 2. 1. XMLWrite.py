import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring, dump

root = Element('movie')
title = SubElement(root, "title")
title.text = "트랜스포머"
genre = SubElement(root, "genre")
genre.text = "SF"
rating = SubElement(root, "rating")
rating.text = "8"

ET.ElementTree(root).write("movie.xml", encoding="UTF-8", xml_declaration=True)