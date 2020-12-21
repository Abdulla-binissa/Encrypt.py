from tkinter import *

import random
import time
import datetime

import base64 

# creating root
root = Tk()

# setting title and size
root.title("Enrcypt.py")
root.geometry("1200x6000")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

##################
###### Time ######

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(
        Tops, 
        font = ('helvetica', 50, 'bold'), 
        text = "SECRET MESSAGING /n Vigenere cipher",
        fg = "Black",
        bd = 10,
        anchor = 'w')
lblInfo.grid(row = 0, column = 0)

lblInfo = Label(
        Tops,
        font = ('arial' , 20, 'bold'),
        text = localtime, 
        fg = "Steel Blue",
        bd = 10,
        anchor = 'w')
lblInfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
    root.destroy()

# reset window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

# reference
lblReference = Label(
        f1, 
        font = ('arial', 16, 'bold'),
        text = "Name: ",
        bd = 16,
        anchor = 'w')
lblReference.grid(row = 0, column = 0)

txtReference = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = rand, bd = 10,
        insertwidth = 4,
        bg = "powder blue", justify = 'right')
txtReference.grid(row = 0, column = 1)

####################
###### Labels ######

lblMsg = Label(
        f1,
        font = ('arial', 16, 'bold'),
        text = "MESSAGE",
        bd = 16, anchor = 'w')
lblMsg.grid(row = 1, column = 1)

txtMsg = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = Msg, 
        bd = 10,
        insertwidth = 4,
        bg = "powder blue",
        justify = 'right')
txtMsg.grid(row = 1, column = 1)

lblkey = Label(
        f1,
        font = ('arial', 16, 'bold'),
        text = "KEY",
        bd = 16,
        anchor = 'w')
lblkey.grid(row = 2, column = 0)

txtkey = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = key,
        bd = 10,
        insertwidth = 4,
        bg = "powder blue", justify = 'right')
txtkey.grid(row = 2, column = 1)

lblmode = Label(
        f1,
        font = ('arial', 16, 'bold'),
        text = "MODE(e for encrype, d for decrypt)",
        bd = 16,
        anchor = 'w')
lblmode.grid(row = 3, column = 0)

txtmode = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = mode,
        bd = 10,
        insertwidth = 4,
        bg = "powder blue",
        justify = 'right')
txtmode.grid(row = 3, column = 1)

lblService = Label(
        f1,
        font = ('arial', 16, 'bold'),
        text = "The Result-",
        bd = 16,
        anchor = 'w')
lblService.grid(row = 2, column = 3)

txtService = Entry(
        f1,
        font = ('arial', 16, 'bold'),
        textvariable = Result,
        bd = 10,
        insertwidth = 4,
        bg = "powder blue",
        justify = 'right')
txtService.grid(row = 2, column = 3)

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

# Ref
def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k= key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

#####################
###### Buttons ######

# Show Message button
btnTotal = Button(
        f1,
        padx = 16,
        pady = 8,
        bd = 16,
        fg = "black",
        font = ('arial', 16, 'bold'),
        width = 10,
        text = "Show Message",
        bg = "powder blue",
        command = Ref)
btnTotal.grid(row = 7, column = 1)

# Show Reset button
btnReset = Button(
        f1,
        padx = 16, 
        pady = 8,
        bd = 16,
        fg = "black", 
        font = ('arial', 16, 'bold'),
        width = 10,
        text = "Reset",
        bg = "green",
        command = Reset)
btnReset.grid(row = 7, column = 2)

btnExit = Button(
        f1,
        padx = 16,
        pady = 8,
        bd = 16,
        fg = "black",
        font = ('arial', 16, 'bold'),
        width = 10,
        text = "Exit",
        bg = "red",
        command = qExit)
btnExit.grid(row = 7, column = 3)

# Run
root.mainloop()

    

