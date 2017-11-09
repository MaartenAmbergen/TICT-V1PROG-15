import xmltodict

def processXML(filenaam):
    with open(filenaam) as myXMLFile:
        filestring= myXMLFile.read()
        xmldictionary=xmltodict.parse(filestring)
        return xmldictionary

artikelendict=processXML('pe10_1.xml')
artikelen=artikelendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])