# Functions used with dump
def getDataFromFile(url) :
    with open(r"" + url + "", "r+", encoding="utf8") as file:
        data = file.read(999999999)
    return data

def writeDataToFile(url, data) :
    with open(outputFile, 'w', encoding="utf8") as file:
        file.write(data)

# Create website dump
import urllib.request, urllib.error, urllib.parse
url = 'https://github.com/Demomaker/WebsiteDifferenceDetector'
response = urllib.request.urlopen(url)
dumpContent = response.read().decode('UTF-8')
dumpFileName = 'websiteDump.html'
writeDataToFile(dumpFileName, webContent)

# Functions used with index
def createIndex(indexData) :
    writeDataToFile('index.html', indexData)

def insertStyleSheet(styleSheetFileName, insertSheetsPosition):
    data = data[insertSheetsPosition:] + '\n<link rel="stylesheet" href="' + scriptFileName + '">' + data[:insertSheetsPosition] 


def insertScript(scriptFileName, insertScriptsPosition):
    data = data[insertScriptsPosition:] + '\n<script src="' + scriptFileName + '"></script>' + data[:insertScriptsPosition] 

def getFormatted(data):
    insertScriptsPosition = data.find('</body>')
    insertSheetsPosition = data.find('</head>')
    insertStyleSheet('index.css', insertSheetsPosition)
    insertScript('index.js', insertScriptsPosition)
    insertScript('differences.js', insertScriptsPosition)

# Create website index
dump = getDataFromFile(dumpFileName)
formattedDump = getFormatted(dump)
createIndex(formattedDump)