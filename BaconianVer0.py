##Baconian Cipher
##using only i and u (if statement will be needed for j and v)
import random
import string 

class Baconian:
    def __init__(self, text):
        self.text = list(text)
        self.ABvalues = {"a":"aaaaa","b":"aaaab","c":"aaaba","d":"aaabb","e":"aabaa","f":"aabab",
            "g":"aabba","h":"aabbb","i":"abaaa","k":"abaab","l":"ababa","m":"ababb",
            "n":"abbaa","o":"abbab","p":"abbba","q":"abbbb","r":"baaaa","s":"baaab",
            "t":"baaba","u":"baabb","w":"babaa","x":"babab","y":"babba","z":"babbb"}
        self.ABkeys = {}
        for key, value in (self.ABvalues).items():
            self.ABkeys[value] = key

##Encryption Algorithms

    def makingAB(self):    
        ABstring = []
        letter = self.text
        for character in range(len(letter)):
            if letter[character].isalpha():
                ##print(letter[i])          ##03/02/2020
                ##print(type(letter[i]))
                if str(letter[character]) == "v":
                    changeto="u"
                    ABstring += self.ABvalues[changeto]
                elif str(letter[character]) == "j":
                    changeto="i"
                    ABstring += self.ABvalues[changeto]
                else:
                    ABstring += self.ABvalues[letter[character]]
            else:
                ABstring += character
        return ABstring
        #print(ABvalues[letter])

    #a is lowercase, b is capital 

    def randtext(self,ABnfive):           
        randomtext=str("")                       
        for aOrB in ABnfive:
            if aOrB =="a":
                loweralpha=string.ascii_lowercase
                randomletter = random.choice(loweralpha)
                randomtext += randomletter
            else:
                upperalpha=string.ascii_uppercase
                randomletter = random.choice(upperalpha)
                randomtext += randomletter
        return randomtext

    def BaconianCipherEncryption(self):
        encyptedText = self.makingAB()
        return self.randtext(encyptedText)

##Decryption Algorithms

    def analyseFiveLetters(self):
        upperAndLower = []
        for char in (self.text):
            if char.isalpha():
                if char.islower():
                    upperAndLower.append("a")
                elif char.isupper():
                    upperAndLower.append("b")
        return upperAndLower
    
    def listOfAB(self,upperAndLower):
        listOfFive = []
        for n in range (int((len(upperAndLower))/5)):
            fiveLetters = []
            fiveLetters.append(upperAndLower[5*n])
            fiveLetters.append(upperAndLower[5*n+1])
            fiveLetters.append(upperAndLower[5*n+2])
            fiveLetters.append(upperAndLower[5*n+3])
            fiveLetters.append(upperAndLower[5*n+4])
            listOfFive.append("".join(fiveLetters))
        return listOfFive

    def comparison(self,listOfFive):
        listOfDecryption=[]
        for ABcode in listOfFive:       ##goes through ab list from input
            for ABalpha in (self.ABkeys).keys():    ##ABalpha is a key in thhe ABKEys
                if ABcode==ABalpha:
                    listOfDecryption.append(self.ABkeys[ABalpha])
        decrypted="".join(listOfDecryption)
        return decrypted

    def BaconianCipherDecryption(self):
        baconianObject = Baconian(self.text)  ##returns with B
        a=baconianObject.analyseFiveLetters()
        b=baconianObject.listOfAB(a)
        return baconianObject.comparison(b)

'''
#example:
def TestDecrypt():
    bacTest = Baconian("aaaBB")
    print(bacTest.BaconianCipherDecryption())
TestDecrypt()
'''