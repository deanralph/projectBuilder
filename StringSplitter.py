class StringSplitter():

    def __init__(self, stringData):

        self = stringData.split(" ")

    def splitLines(self, noOfCharsPerLine):

        varOldLine = ""
        varNewLine = ""
        varCurLine = ""
        arrSplitLines = []

        for i, word in enumerate(self):
            varCurLine += f"{word} ""
            varNewLine += f"{varOldLine}{self[i+1]}"

            if len(varNewLine) >= noOfCharsPerLine:
                varOldLine = varCurLine

            if i = len(self)-1:
                varOldLine = varCurLine

            if varOldLine != "":
                arrSplitLines.append(varOldLine)
                varCurLine = ""
                varOldLine = ""

        return arrSplitLines
