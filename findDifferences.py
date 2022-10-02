def getDataFromFile(url) :
    with open(r"" + url + "", "r+", encoding="utf8") as file:
        data = file.read(999999999)
    return data

def writeDataToFile(url, data) :
    with open(outputFile, 'w', encoding="utf8") as file:
        file.write(data)

def putIntoJavascriptFile(url, data) :
    dataInJavascriptVariable = "const differences = `" + data + "`"
    writeDataToFile(dataInJavascriptVariable)

data = getDataFromFile('difflog.txt')
putIntoJavascriptFile('differences.js', data)