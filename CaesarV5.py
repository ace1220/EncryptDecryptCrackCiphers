##This version is altered so it works with the GUI

class Caesar:
    def __init__(self, ciphertext, shift):  
        self.ciphertext=list([m.lower() for m in ciphertext])  ##ciphertext is a list
        self.shift=shift
    
    def CCProcess(self, rightorleft):
        processlist=[]
        for a in self.ciphertext:
            if a.isalpha()==True:
                b=self.convert(a,self.shift, rightorleft)
                processlist.append(b)
            else:
                processlist.append(a)
        joined="".join(map(str,processlist))
        return joined

    def convert(self, letter, shift, rightorleft):   
        l=chr(((ord(letter)-96)+(rightorleft)*shift)%26+96)
        if l =="`":
            l="z"
        return l

    def CaesarCipherDecryption(self):
        mode = -1
        result = self.CCProcess(mode)
        return result
    
    def CaesarCipherEncryption(self):
        mode = +1
        result = self.CCProcess(mode)
        return result

'''
example:
caesar = Caesar("spam",5)
print(caesar.CaesarCipherDecryption())
'''

