# Functions used with dump
def getDataFromFile(url) :
    with open(r"" + url + "", "r+", encoding="utf8") as file:
        data = file.read(999999999)
    return data

def writeDataToFile(url, data) :
    with open(url, 'w', encoding="utf8") as file:
        file.write(data)

# Create website dump
import urllib.request, urllib.error, urllib.parse
url = 'https://github.com/Demomaker/WebsiteDifferenceDetector'
response = urllib.request.urlopen(url)
dumpContent = response.read().decode('UTF-8')
dumpFileName = 'websiteDump.html'
writeDataToFile(dumpFileName, dumpContent)

# Functions used with index
def createIndex(indexData) :
    writeDataToFile('index.html', indexData)

def insertStyleSheet(data, styleSheetFileName, insertSheetsPosition):
    return data[insertSheetsPosition:] + '\n<link rel="stylesheet" href="' + scriptFileName + '">' + data[:insertSheetsPosition] 


def insertScript(data, scriptFileName, insertScriptsPosition):
    return data[insertScriptsPosition:] + '\n<script src="' + scriptFileName + '"></script>' + data[:insertScriptsPosition] 

def getFormatted(data):
    modifiedData = data
    insertScriptsPosition = modifiedData.find('</body>')
    insertSheetsPosition = modifiedData.find('</head>')
    modifiedData = insertStyleSheet(modifiedData, 'index.css', insertSheetsPosition)
    modifiedData = insertScript(modifiedData, 'index.js', insertScriptsPosition)
    modifiedData = insertScript(modifiedData, 'differences.js', insertScriptsPosition)
    return modifiedData

# Create website index
dump = getDataFromFile(dumpFileName)
formattedDump = getFormatted(dump)
createIndex(formattedDump)