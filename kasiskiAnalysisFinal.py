##Cracking Vigenere Cipher: Kasiski Analysis
##Will not accept keys that are 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

import EnglishCheckerFinal as EC
import VigenereV2 as VC

import string
import itertools

class VigenereCrack:
    def __init__(self, ciphertext):
        self.ciphertext=ciphertext
        textNS=""
        self.spaceindex=[]
        for single in range(0,len(self.ciphertext)):
            character=self.ciphertext[single]
            if character.isalpha():   ##will return true or false
                textNS+=character       ##adds any character that is an alphabetical character to a new string
            elif character.isspace():   ##will return true or false
                self.spaceindex.append(single)    ##adds the index of all the spaces to a list
        self.textNS=textNS.lower()      ##makes every letter in the text lowercase with no special characters
        #To be used in multiples or whatever it is called now
        self.possibleKeyLength=[]

        self.threelist = []

        self.listOfFactors=[]
        ##used in factorsList
        self.differences = []
        self.occurdict={}
        ##used in likely keys
        self.likelyKeyNum=[]
        #used in VCCFreqA
        self.keyProbably=True       ##True is just a placeholder
        self.possibleKeyList=True
        self.decryptedText = "not found"        ##Set to this value by default

    def getMultipleIndexes(self,searchElement):
        indexesList = []
        indexPosition = 0
        while True:
            try:
                indexPosition=self.textNS.index(searchElement, indexPosition)
                indexesList.append(indexPosition)
                indexPosition+=1
            except ValueError as e:
                break
        return indexesList

    def repeatedThrees(self):  ##looks at three characters and compares them to every other three and records the index of repeated keys
        incrementfromzero=0
        incrementfromthree=3
        threedict = {}

        for number in range(0,(len(self.textNS)-2)):
            three=self.textNS[incrementfromzero:incrementfromthree]
            if three in threedict.keys():  ##if three is already in the dictionary
                self.threelist.append(three)  ##appends three if it is repeated
                threedict[three]+=1     ##this tells how many occurances there are
            else:
                threedict[three]=1  ##adds it to the dictionary if its not there
            incrementfromzero+=1       ##runs after the if statement
            incrementfromthree+=1
        return self.threelist

    ##This returns all the differences between every group of 3
    def differenceBetweenGroups(self):
        for stringOfThree in self.threelist:
            templistOfPos=self.getMultipleIndexes(stringOfThree)
            ##print(templistOfPos) ##e.g. output: [53,89]
            for posNumber in range(0,(len(templistOfPos)-1)):
                ##print(templistOfPos[posNumber+1]-(templistOfPos[posNumber])) ##e.g. output: 36, 420
                self.differences.append(templistOfPos[posNumber+1]-(templistOfPos[posNumber]))
        return self.differences
            
    #This is finding factors that could possibly be the key
    def factor(self,x,min_factor):
        ##x is fac from the for loop in factorsList
        for i in range(1, x + 1):
            if x % i == 0:
               if i<=min_factor:
                  self.listOfFactors.append(i)
        return self.listOfFactors
    
    def factorsList(self):
        factors_factor=[]
        ##print("Min Value: ",min(self.differences)) ##This value is the minimum number produced from the differences between groups of threes
        for fac in self.differences:
            templist=self.factor(fac,min(self.differences))
            for num in templist:
                factors_factor.append(num)
        ##every occurance of factors up to the min factor

        for fac in factors_factor:
            if fac not in self.occurdict.keys():
                self.occurdict[fac]=factors_factor.count(fac)
        if 1 in self.occurdict.keys():
            self.occurdict[1]=0 
            ##removes 1 character shifts as they are caesar cipher and commonly disrupt the most common factor

    def likelyKeys(self):       ##creating a list of likely keys
        likelyKeyList=[]
        highest = max(self.occurdict.values())  ##upperbound for values
        lower = highest-1000                    ##lowerbound for values
        for num in self.occurdict:
            if (self.occurdict[num] <=highest) and (self.occurdict[num]>lower):
                ##print(num,self.occurdict[num])        ##prints the ones that satisfy the range
                likelyKeyList.append(num)
        likelyKeyList=sorted(likelyKeyList)     ##sorts them in numerical order
        likelyKeyList=likelyKeyList[::-1]       ##highest key returned is the most likely key but will have several in this list
        self.likelyKeyNum=likelyKeyList[0]      ##Will return higheset one
        return self.likelyKeyNum

    def VCCFreqA(self):                #Vigenere Cipher Cracking Frequency Analysis
        sixMostFrequentLetters=["e","t","a","o","i","n"]
        listOfStrings=[]
        mightBeKey=[]
        ##creating lists of letters for every letter of the key length
        for magnitude in range(0,self.likelyKeyNum):
            mightBeKey.append([])
            listOfStrings.append([])
        listTextNS=list(self.textNS)
        for letterpos in range(0,len(self.textNS)):
            listNum=letterpos%self.likelyKeyNum
            listOfStrings[listNum].append(listTextNS[letterpos])
        listOfDict=[]
        for lists in listOfStrings:
            dictOfAlpha = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,
                    "g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
                    "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,
                    "t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
            for letter in lists:
                dictOfAlpha[letter]+=1
                mostCommonLetter=max(dictOfAlpha, key=dictOfAlpha.get)
            for popularLetter in sixMostFrequentLetters:
                tempkey=chr((ord(mostCommonLetter)-ord(popularLetter))+97)
                if tempkey in string.ascii_lowercase:
                    mightBeKey[listOfStrings.index(lists)].append(tempkey)             ##This makes a 2d array e.g. possiblekey=[[first letter of key],[second letter of key],...]
        self.keyProbably=mightBeKey
        return self.keyProbably

    def keyCompile(self):
        def finished(variables, arr):       ##arr = array
            return variables[0] == len(arr[0])
        def updateVariables(variables, arr):
            carry1 = True
            currIndex = len(variables) - 1
            while carry1:
                variables[currIndex] = variables[currIndex] + 1
                if variables[currIndex] == len(arr[currIndex]) and currIndex != 0:
                    variables[currIndex] = 0
                    currIndex = currIndex - 1
                else:
                    carry1 = False
            pass
        ##      [[possible 1st letters of key],[possible 2nd letters of key],...]
        ##arr= [["a", "d", "e"], ["h", "i"], ["q", "w", "e"]]   ##=self.keyProbably
        possibleKeys = []
        variables = []
        for i in self.keyProbably:     
            variables.append(0)
        possibleKeys = []
        while not finished(variables, self.keyProbably):
            key = ""
            for i in range(len(self.keyProbably)):
                key += self.keyProbably[i][variables[i]]
            updateVariables(variables, self.keyProbably)
            possibleKeys.append(key)
        self.possibleKeyList=possibleKeys     

    def keyCracking(self):  ##Trying possible keys
        decryptedText=""
        n=0
        for key in self.possibleKeyList:
            n+=1
            vigeneretest=VC.Vigenere(key,self.ciphertext)
            VDtest = vigeneretest.VigenereCipherDecryption()
            test = EC.EnglishChecker(VDtest)
            check=test.englishcheckerBF()
            if check:
                self.decryptedText=VDtest
                break
        return self.decryptedText
        
    ##This module should work but there is something wrong with my Vigenere decryption program

    def VCCrack(self):
        ##print(self.textNS)
        self.repeatedThrees()
        self.differenceBetweenGroups()
        self.factorsList()
        self.likelyKeys()
        self.VCCFreqA()
        self.keyCompile()
        answer=self.keyCracking()
        return answer

'''
#example:
##key = abcd
text2 = "Io ob cbuh, iu'u d lppj suquy, bpg a dtrwegg oog. L wbu d rfxrlvvloocuy xjr lpuw hju ldfcos jp kesqln, b rkimqvoqjhr xjr lpuw hju lnugjrjvb io euing, dne c sofv zhp nrsu jls tqxl jp d mbzlmvo-vedwuiua srjurn. Xjhn J gvcbrhd gtrm ujdt qtlspp, rvft whf huoov zamn, eeuyheo vzo hwq-tpyhrt, K eedcpe na fovpwrz'u potv zaovhd ncq. Lven rbp ziuj pe bpg fmgz wjvk mf cfrpuv tig zosng tp Kqdjc, zhfth I kqlnff whf Drmccb mbhla. J yrrlgg at c juotxnogu, a toxghnhr, bpg a dqxnuguffkwes. K zat ekajphd pp whsgh cppwiogqtt, dhaugq, sucebff, dne uwasxhd. J yhnu vr wbt. L rbp lnuq whf gqena juou. Dne K vusxlvff, zhjnh oujhr ngq asqxne oh djgg. Tigb wfth bfvwes ohn ujdn J cp, mpuw og vken: dhtugu mfp zhpuh ljxhs xgue dtxndjhd vr ln nkvtbmhs, bpg titrwo czaz db tig zrppj sferne qi spohoog hltg'v hbvh, os nrvf, qu ioflfggueoeh. Aof L bvtlee vken, vro ncqy ph whpuh mfp, dne iuifxhd ujhis uwoskhs bpg tiglr mkyet kqtp ob oxp."
test=VigenereCrack(text2)
print(test.VCCrack())
'''
