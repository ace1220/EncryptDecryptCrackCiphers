##Cracking Caesar Cipher: Frequency Analysis

import CaesarV5 as CC
import EnglishCheckerFinal as EC

class frequencyAnalysis:
    def __init__(self,ciphertext):
        self.ciphertext = ciphertext.lower()
        self.tableOfCipherText = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,
                    "g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
                    "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,
                    "t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        self.sixMostFrequentLetters=["e","t","a","o","i","n"]
        self.dictionary = open("english2.txt", "r").read().splitlines()

    def modalLetter(self):  ##finding most frequently occuring letter
        for letter in self.ciphertext:
                if letter.isalpha()==True:
                    self.tableOfCipherText[letter]=self.tableOfCipherText[letter]+1
        mostfrequent=max(zip(self.tableOfCipherText.values(),self.tableOfCipherText.keys()))
        MFL = mostfrequent[1] ##gets rid of unwanted 2D array for 1 element
        return MFL

    def attemptingtocrack(self,modal):
        letterindex=0
        correctDecryption = "not found"
        while letterindex<6:  
            attemptKey=ord(modal)-ord(self.sixMostFrequentLetters[letterindex])
            attempt = CC.Caesar(self.ciphertext, attemptKey)
            attempting = attempt.CaesarCipherDecryption()   ##decrypted text regardless of whether it is correct
            wordlist= EC.EnglishChecker(attempting)
            attemptEEng = wordlist.englishcheckerBF()   ##True or False
            if attemptEEng==True:
                correctDecryption=attempting
                letterindex+=1      ##It will continue running through the list so the while loop is satisfied
            else:
                letterindex+=1
        return(correctDecryption)

    def runFA(self):
        MFL = self.modalLetter()
        cracked=self.attemptingtocrack(MFL)
        return cracked

'''
#example:
ciphertext="Pa tbza ohcl illu hyvbuk h xbhyaly av lslclu. H zhpsvy jhtl pu huk vyklylk h jopsl kvn huk jvmmll. P zspjlk h ibu, qlyrlk h myhur vba vm aol ivpspun dhaly, ulzalk pa, wvbylk h ohsm-kpwwly vm jopsl vcly aol myhur huk zwypurslk pa spilyhssf dpao jovwwlk vupvuz. P zjypiislk h joljr huk wba pa if opz wshal. P dvbsku’a ohcl yljvttluklk aol buwhshahisl tlzz av h zahycpun hupths. Aol zhpsvy dhz aol vusf jbzavtly, huk hmaly ol hal opz kvn ol slma. Aoha dhz aol lehja tvtlua zol lualylk. H zthss dvthu, ohyksf tvyl aohu mpcl mlla. Zol ohk aol mpnbyl vm h alluhnl npys. Oly zbpa dhz h isbl adllk, zthyasf jba, huk vcly oly aopu zovbsklyz zol dvyl h mby qhjrla, ivslyv slunao. Apuf nvsk jpyjbshy lhyypunz jsbun av oly zthss wplyjlk lhyz. Oly ohukz huk mlla dlyl zthss, huk dolu zol zlhalk olyzlsm ha aol jvbualy P uvapjlk zol dhzu’a dlhypun huf ypunz."
test = frequencyAnalysis(ciphertext)
print(test.runFA())
'''