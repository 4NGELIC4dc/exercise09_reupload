class Letter:
    def __init__(self, letterFrom, letterTo):
        self._text=[]
        self._from=letterFrom
        self._to=letterTo
    def addLine(self, line):
        self._text.append(line)
    def getText(self):
        content="Dear "+self._to+":\n\n"
        for line in self._text:
            content+=line+"\n"
        content+="\n"
        content+="Sincerely, \n\n"+self._from
        return content
def main():
    myLetter=Letter("Mary", "John")
    myLetter.addLine("I am sorry we must part.")
    myLetter.addLine("I wish you all the best.")
    print(myLetter.getText())
main()