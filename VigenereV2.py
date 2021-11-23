class Vigenere:
    def __init__(self,key,text):
        self.fixedKey = [ord(o.lower())-96 for o in key]
        self.key = []       ##this will be key used for decryption or encryption
        self.text = list([m.lower() for m in text])
        keyLengthwr=0   ##with repeats
        for i in self.text:
            if i.isalpha():
                keyLengthwr+=1  
            else:
                pass           
        for j in range(0,keyLengthwr): 
            self.key.append(ord(key[j % len(key)])-96)


    ##This is for Vigenere
    def VCChange(self,rightorleft):                       
        letterlist = self.text
        numberlist = self.key
        encryptlist=[]
        n=0
        for i in range(0,len(letterlist)):  ##changes made here: goes through letterlist and n only increments if the letter is alphabetical
            character = letterlist[i]
            if character.isalpha():   ##validates that letter is in the alphabet 
                keynum=numberlist[n]
                shiftedletter=self.convert(character,(keynum-1), rightorleft)  ##second part is just the shift
                encryptlist.append(shiftedletter)
                n+=1
            else:
                encryptlist.append(character)
        joined="".join(map(str,encryptlist))
        ##print ("The following is the encrypted text:\n"+joined) #Outputs into terminal
        return joined
        
    def convert(self,letter, shift, rightorleft):   ##same as used in the Caesar Cipher
        l=chr(((ord(letter)-(ord('a')-1))+(rightorleft)*shift)%26+96)
        if l =="`":         
            l="z"
        return l

    def VigenereCipherEncryption(self):
        mode = +1
        ##print("Vigenere Cipher > Encryption")
        return self.VCChange(mode)


    def VigenereCipherDecryption(self):
        mode = -1
        ##print("Vigenere Cipher > Decryption")
        return self.VCChange(mode)

'''
#example:
test=Vigenere("abc","abc de!!")
print(test.VigenereCipherEncryption())
'''