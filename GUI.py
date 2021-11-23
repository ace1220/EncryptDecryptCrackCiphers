from tkinter import *
from tkinter import messagebox
import pyperclip as cbt      ##clip board tools 
import datetime as record   ##imported timer to record times

import CaesarV5 as CC   
import VigenereV2 as VC	
import BaconianVer0 as BC
import frequencyAnalysisFinal as FA      ##This is Caesar Cipher Cracking
import kasiskiAnalysisFinal as KA       ##This is Vigenere Cipher Cracking

class GUI:       
    def __init__(self, root):
        self.root = root   
        ##This frame is constant throughout the program
        self.main_frame = Frame(root,bg = "Light Yellow")
        ##These have been initialized as frames and contain information in the corresponding functions   
        self.caesar_frame = Frame(root,bg="Light Yellow")   
        self.baconian_frame = Frame(root,bg="Light Yellow")
        self.vigenere_frame = Frame(root,bg="Light Yellow")
        #These are packed so that the program looks more orderly and these can be forgotten and reinstated easily
        self.main_frame.pack()  
        self.caesar_frame.pack()
        self.baconian_frame.pack()
        self.vigenere_frame.pack()
        ##These are creating labels to be used later on in the program to display the result
        self.caesar_result = Label(self.caesar_frame, background = "Light Yellow", wraplength=400)  
        self.vigenere_result = Label(self.vigenere_frame, bg= "Light Yellow", wraplength=400)
        self.baconian_result = Label(self.baconian_frame, bg= "Light Yellow", wraplength=400)
        ##These use grid because within all the frames grid is used, but the frames themselves are packed.
        self.caesar_result.grid(row=14)     
        self.vigenere_result.grid(row=14)
        self.baconian_result.grid(row=14)

    def CCEncryption(self,caesar_frame,entry1,entry2):
        start = record.datetime.now()
        key = entry1.get()
        if key.isdigit() == False:          ##Validation for key: integer
            messagebox.showerror("Invalid Key","Please enter the key as an integer.")
            entry1.delete(0,"end")
        else:
            key=int(key)
        text = entry2.get()
        caesarE = CC.Caesar(text,key)
        encrypting=caesarE.CaesarCipherEncryption()
        self.caesar_result.config(text=encrypting)  ##This code changes what is contained in the label in self with what has been encrypted
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.caesar_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(encrypting)) ##This button copies the output to the users clipboard
        copytoclipboard.grid(row=15)

    def CCDecryption(self,caesar_frame,entry1,entry2):
        start = record.datetime.now()
        key = entry1.get()
        text = entry2.get()
        if key.isdigit() == False:          ##Validation for key: integer
            messagebox.showerror("Invalid Key","Please enter the key as an integer.")
            entry1.delete(0,"end")
        else:
            key=int(key)
        caesarD = CC.Caesar(text,key)
        decrypting=caesarD.CaesarCipherDecryption()
        self.caesar_result.config(text=decrypting)
        copytoclipboard=Button(self.caesar_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(decrypting))
        copytoclipboard.grid(row=15)

    def CCCrack(self,caesar_frame,entry2):
        start = record.datetime.now()
        text = entry2.get()
        caesarC = FA.frequencyAnalysis(text)
        cracking = caesarC.runFA()
        self.caesar_result.config(text = cracking)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.caesar_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(cracking))
        copytoclipboard.grid(row=15)
    
    def VCEncryption(self,entry1,entry2):    ##Validation for key: string, no numbers, special characters or spaces
        start = record.datetime.now()        
        key = entry1.get()
        if key.isalpha() == False:    
            messagebox.showerror("Invalid Key","Please enter the key as a string of only letters.")
            entry1.delete(0,"end")
        text = entry2.get()
        vigenereE = VC.Vigenere(key,text)
        encrypting=vigenereE.VigenereCipherEncryption()
        self.vigenere_result.config(text=encrypting)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.vigenere_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(encrypting))
        copytoclipboard.grid(row=15)

    def VCDecryption(self,entry1,entry2):    ##Validation for key: string, no numbers, special characters or spaces
        start = record.datetime.now()
        key = entry1.get()
        if key.isalpha() == False:    
            messagebox.showerror("Invalid Key","Please enter the key as a string of only letters.")
            entry1.delete(0,"end")
        text = entry2.get()
        vigenereD = VC.Vigenere(key,text)
        decrypting=vigenereD.VigenereCipherDecryption()
        self.vigenere_result.config(text=decrypting)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.vigenere_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(decrypting))
        copytoclipboard.grid(row=15)

    def VCCrack(self,entry2):
        start = record.datetime.now()
        text = entry2.get()
        vigenereC = KA.VigenereCrack(text)
        cracking = vigenereC.VCCrack()
        self.vigenere_result.config(text = cracking)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.vigenere_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(cracking))
        copytoclipboard.grid(row=15)

    def BCEncryption(self,entry):
        start = record.datetime.now()
        text = entry.get()
        baconianE = BC.Baconian(text)
        encrypting=baconianE.BaconianCipherEncryption()
        self.baconian_result.config(text=encrypting)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.baconian_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(encrypting))
        copytoclipboard.grid(row=15)

    def BCDecryption(self, entry):
        start = record.datetime.now()
        text = entry.get()
        baconianD = BC.Baconian(text)
        decrypting=baconianD.BaconianCipherDecryption()
        self.baconian_result.config(text=decrypting)
        end = record.datetime.now()
        print("Timer: ",end-start)
        copytoclipboard=Button(self.baconian_frame,bg="white",font=("Helvetica", 9),text="Copy",command=lambda: cbt.copy(decrypting))
        copytoclipboard.grid(row=15)

    def CaesarSelect(self):
        self.caesar_frame.pack()
        self.baconian_frame.pack_forget()
        self.vigenere_frame.pack_forget()
        self.caesar_result.config(text="")
        caesar_frame=self.caesar_frame
        
        CCnote=Label(caesar_frame, bg="Light Yellow",font=("Helvetica", 10),text="Caesar Cipher Input").grid(row=7, column=0) ##This will appear on the window
        CCkey=Label(caesar_frame, bg="Light Yellow",font=("Helvetica", 9),text="Enter key:").grid(row=8)
        entry1=Entry(caesar_frame)
        CCtext=Label(caesar_frame, bg="Light Yellow",font=("Helvetica", 9),text="Enter text to be processed:").grid(row=9)
        entry2 = Entry(caesar_frame)
        entry1.grid(row = 8,column=1)
        entry2.grid(row = 9, column = 1)

        encryptButton = Button(caesar_frame, bg="white",font=("Helvetica", 9), text = "Encrypt",command=lambda: self.CCEncryption(caesar_frame,entry1,entry2))
        decryptButton = Button(caesar_frame, bg="white",font=("Helvetica", 9), text = "Decrypt",command=lambda: self.CCDecryption(caesar_frame,entry1,entry2))
        crackButton = Button(caesar_frame, bg="white",font=("Helvetica", 9), text = "Crack", command = lambda: self.CCCrack(caesar_frame,entry2))
        encryptButton.grid (row = 11, column = 0)
        decryptButton.grid (row = 11, column = 1)
        crackButton.grid(row = 11, column = 2)

    def BaconianSelect(self):
        self.caesar_frame.pack_forget()
        self.baconian_frame.pack()
        self.vigenere_frame.pack_forget()
        self.baconian_result.config(text="")  ##reseting the result value
        baconian_frame=self.baconian_frame
        BCnote=Label(self.baconian_frame, bg="Light Yellow",font=("Helvetica", 10), text="Baconian Cipher Input").grid(row=7, column=0)
        entry=Entry(self.baconian_frame)
        BCtext=Label(self.baconian_frame, bg="Light Yellow",font=("Helvetica", 9),text="Enter text to be processed:").grid(row=8)
        
        encryptButton = Button(self.baconian_frame, bg="white",font=("Helvetica", 9), text = "Encrypt",command=lambda: self.BCEncryption(entry))
        decryptButton = Button(self.baconian_frame, bg="white",font=("Helvetica", 9), text = "Decrypt",command=lambda: self.BCDecryption(entry))
        encryptButton.grid(row=11)
        decryptButton.grid (row = 11, column = 1)
        entry.grid(row=8,column=1)

    def VigenereSelect(self):
        self.caesar_frame.pack_forget()
        self.baconian_frame.pack_forget()
        self.vigenere_frame.pack()
        self.vigenere_result.config(text="")
        vigenere_frame=self.vigenere_frame
        
        VCnote=Label(vigenere_frame,bg="Light Yellow",font=("Helvetica", 10), text="Vigenère Cipher Input").grid(row=7, column=0)
        VCkey=Label(vigenere_frame, bg="Light Yellow",font=("Helvetica", 9),text="Enter key:").grid(row=8)
        entry1=Entry(vigenere_frame)

        VCtext=Label(vigenere_frame,bg="Light Yellow",font=("Helvetica", 9),text="Enter text to be processed:").grid(row=9)
        entry2 = Entry(vigenere_frame)
        entry1.grid(row=8,column=1)
        entry2.grid(row = 9, column = 1)

        encryptButton = Button(vigenere_frame, bg="white",font=("Helvetica", 10), text = "Encrypt",command=lambda: self.VCEncryption(entry1,entry2))
        decryptButton = Button(vigenere_frame, bg="white",font=("Helvetica", 10), text = "Decrypt",command=lambda: self.VCDecryption(entry1,entry2))
        crackButton = Button(vigenere_frame, bg="white",font=("Helvetica", 9), text = "Crack", command = lambda: self.VCCrack(entry2))
        encryptButton.grid (row = 11, column = 0)
        decryptButton.grid (row = 11, column = 1)
        crackButton.grid (row = 11, column = 2)

    def main(self):
        welcome=Label(self.main_frame, bg="Light Yellow", font=("Helvetica", 11), text = "Welcome \nPlease select a Cipher").grid(row=0, column=0)
        firstbutton = Button(self.main_frame, bg="white",font=("Helvetica", 9),text="Caesar Cipher", command=lambda: self.CaesarSelect()).grid(row=2,column=0)
        secondbutton = Button(self.main_frame, bg="white",font=("Helvetica", 9),text="Baconian Cipher", command=lambda: self.BaconianSelect()).grid(row= 3, column = 0)
        thirdbutton = Button(self.main_frame, bg="white",font=("Helvetica", 9), text = "Vigenère Cipher", command=lambda: self.VigenereSelect()).grid(row= 4, column = 0)
        root.mainloop()

root=Tk()
root.geometry("800x600")
root.configure(background="Light Yellow")
root.title("Cybites Cipher")
gui = GUI(root)
gui.main()

