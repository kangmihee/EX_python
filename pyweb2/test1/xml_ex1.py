# XML 문서 처리

import xml.etree.ElementTree as etree

xmlfile = etree.parse("../testdata/my.xml")
print(xmlfile)
etree.dump(xmlfile)

print()
root = xmlfile.getroot()
print(root.tag) # items

print(root[0].tag)
print(root[0][0].tag)
print(root[0][1].tag)
print(root[0][0].attrib)
print(root[0][0].attrib.keys())
print(root[0][0].attrib.values())
print(root[0][2].attrib.get("kor"))

print()
myname = root.find("item").find("name").text
print(myname)

