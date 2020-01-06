class StringSplitter():

    def __init__(self, stringData):

        self = stringData.split(" ")

    def splitLines(self, noOfCharsPerLine):

        varOldLine = ""
        varNewLine = ""
        varCurLine = ""
        arrSplitLines = []

        for i, word in enumerate(self):
            varCurLine += f"{word} "
            if i != len(varList)-1:
                varNewLine += f"{varOldLine}{self[i+1]}"

            if len(varNewLine) >= noOfCharsPerLine:
                varOldLine = varCurLine
                varNewLine = ""

            if i == len(self)-1:
                varOldLine = varCurLine

            if varOldLine != "":
                arrSplitLines.append(varOldLine)
                varCurLine = ""
                varOldLine = ""

        return arrSplitLines
