import sys, os
from xml.etree.ElementTree import ElementTree

engResxTree = ElementTree()
engResxTree.parse(sys.argv[1])

targetResxTree = ElementTree()
targetResxTree.parse(sys.argv[2])

tList = list()
for data in targetResxTree.getroot().findall('data'):
    tList.append(data.get('name'))

# result file get generated under the same folder where the english file is present
outfile = open(os.path.dirname(sys.argv[2]) + '\\result.txt', 'w')

for data in engResxTree.getroot().findall('data'):
    name = data.get('name')
    if(name not in tList):
        comment = data.find('comment')
        if comment is not None:
            commentText = (str(comment.text)).lower()
            if('unused' not in commentText and 'english only' not in commentText and 'do not translate' not in commentText):
                outfile.writelines(name)
                outfile.writelines('\n')
                outfile.writelines(commentText)
                outfile.writelines('\n')
                outfile.writelines('\n')
        else:
            outfile.writelines(name)
            outfile.writelines('\n')
            outfile.writelines('\n')

outfile.close()