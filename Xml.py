
from xml.etree.ElementTree import ElementTree

# s = [['test', '4', 5.0], [4], ['Deba']] 
# print(s[0])

tree = ElementTree()
tree.parse('C:\\Users\\bss\\Downloads\\BondResources.hu.resx')


# tree.parse('C:\\Users\\bss\\Downloads\\sample.xml')
root = tree.getroot()

for data in root.findall('data'):
    comment = data.find('comment')
    if comment is not None:
        com = str(comment.text)
        if(com == 'Unused.' or com == 'English only.' or 'Do not translate' in com):
            root.remove(data)

tree.write('C:\\Users\\bss\\Downloads\\BondResources.hu_modified.resx', encoding="UTF-8", xml_declaration=True)

