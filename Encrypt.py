from tkinter import *

import random
import time
import datetime

import base64 

# creating root
root = Tk()


# setting title and size
root.title("Encrypt.py")
root.geometry("600x300")

f1 = Frame(root, width = 300, height = 600, relief = SUNKEN)
f1.pack(fill = BOTH)

OriginalMsg = StringVar()
key = StringVar()
Result = StringVar()

# exit function
def qExit():
    root.destroy()

# reset window
def Reset():
    OriginalMsg.set("")
    key.set("")
    Result.set("")

#############################
###### Vigenère cipher ######

# Encode
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decode
def decode(key, enc):
	dec = []

	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
		dec.append(dec_c)
	return "".join(dec)

# Button Refs
def EncRef():
	print("Message= ", (txtMsg.get("1.0",END)))

	clear = txtMsg.get("1.0",END)
	k = key.get()
	txtService.delete(1.0, END)
	txtService.insert(1.0, encode(k, clear))

def DecRef():
	print("Message= ", (txtMsg.get("1.0",END)))

	clear = txtMsg.get("1.0",END)
	k = key.get()
	txtService.delete(1.0, END)
	txtService.insert(1.0, decode(k, clear))

######################################################
#################### Labels ##########################

# Key: 
lblkey = Label(
        f1,
        font = ('arial', 16, 'bold'),
        text = " Key:",
        anchor = 'w')
lblkey.place(
        width = 80,
        height = 50,
        x = 0, 
        y = 5)

# Key Entry Box
txtkey = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = key,
        insertwidth = 4,
        bg = "powder blue",
        justify = 'right')
txtkey.place(
        width = 210,
        height = 40, 
        x = 80, 
        y = 10)

# Encode Button
btnEnc = Button(
        f1,
        fg = "black",
        font = ('arial', 16, 'bold'),
        width = 6,
        text = "Encrypt",
        bg = "green",
        command = EncRef)
btnEnc.place(
        width = 120, 
        height = 50, 
        x = 310, 
        y = 5)

# Deccode Button
btnDec = Button(
        f1,
        fg = "black",
        font = ('arial', 16, 'bold'),
        width = 6,
        text = "Decrypt",
        bg = "green",
        command = DecRef)
btnDec.place(
        width = 120, 
        height = 50, 
        x = 435, 
        y = 5)

# Message: 
lblMsg = Label(
        f1,
        padx = 10,
        font = ('arial', 16, 'bold'),
        text = "Message",
        anchor = 'w')
lblMsg.place(
        width = 300,
        height = 40, 
        x = 0, 
        y = 60)

# Result: 
lblMsg = Label(
        f1,
        padx = 10,
        font = ('arial', 16, 'bold'),
        text = "Result",
        anchor = 'w')
lblMsg.place(
        width = 300,
        height = 40, 
        x = 300, 
        y = 60)

# Message Box
txtMsg = Text(
        f1,
        font = ('arial', 16, 'bold'),
        bg = "powder blue")
txtMsg.place(
        width = 280,
        height = 190, 
        x = 10, 
        y = 100)

# Result Box
txtService = Text(
        f1,
        font = ('arial', 16, 'bold'),
        bg = "powder blue")
txtService.place(
        width = 280,
        height = 190, 
        x = 310, 
        y = 100)

###### Run
root.mainloop()

    

