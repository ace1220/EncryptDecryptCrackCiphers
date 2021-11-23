##English Checker Program
##english2.txt is a dictionary of words, this must be located in the same directory/ folder as this program.

class EnglishChecker:
    def __init__(self,text):
        self.text=text
        a = open("english2.txt", "r")
        with open("english2.txt", "r") as dict:
            a = dict.read().splitlines()
        self.dictionary=a

    ##makes text lowercase with all spaces retained
    def processTextLCaWS(self):
        text=self.text.lower()
        processedText = ""
        for character in text:
            if character.isalpha() == True:
                processedText+=character
            elif character.isspace() == True:
                processedText+=character
        return processedText

    ##BF = Brute Force
    def englishcheckerBF(self):
        wordlist=self.processTextLCaWS().split()
        point=0
        totalwords = len(wordlist)
        for word in wordlist:
            for line in self.dictionary:
                if word == line:
                    point+=1
                    break
        if (point/totalwords)>0.90:     #Over 90% of text is English 
            #Program runs fast providing it doesn't print the outcomes
            return True
        else:
            return False

'''
#example:
text1 = "her last smile to me wasn't a sunset. it was an eclipse, the last eclipse, noon dying away to darkness where there would be no dawn."
pieceOfText=EnglishChecker(text1)
print(pieceOfText.englishcheckerBF())
'''
