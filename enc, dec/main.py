from tkinter import *
import base64
import tkinter
from tkinter.tix import IMAGETEXT

#initialize window
root = Tk()
root.geometry('600x500')
root.resizable(0,0)
root.config(padx=50, pady=50, background="light blue")

#title of the window
root.title(" Encode and Decode")



#label
Label(root, text ='ENCODE DECODE', font = 'roman  20 bold',bg='light blue').pack()



#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#-------------define function----------------------------

#function to encode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#function to decode
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)


#function to set mode
def Mode():
    if(mode.get() == 'encode'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'decode'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Message
Label(root, font= 'arial 12 italic', text='MESSAGE', bg='light blue', ).place(x= 60,y=100)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white', width=50,).place(x=60, y = 120)
#key
Label(root, font = 'arial 12 italic', text ='KEY',bg='light blue').place(x=60, y = 160)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white',show='*').place(x=60, y = 180)


#mode------------------------------------------------------------------------------------------------------

options = [
   "encode",
   "decode"
]
  

mode = StringVar()
  
# initial menu text
mode.set( "encode" )
  
# Create Dropdown menu
drop = OptionMenu( root , mode , *options )
drop.pack()
#------------------------------------------------------------------------------------------------


#result
Entry(root, font = 'arial 10 italic', textvariable = Result,bg = 'yellow',width=50).place(x=150, y = 240)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT',width =6  ,padx =2,bg ='aqua',fg='dark blue' ,command = Mode).place(x=60, y = 240)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'red', fg='white', padx=2).place(x=60, y = 270)

root.mainloop()