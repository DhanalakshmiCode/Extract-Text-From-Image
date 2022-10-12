
#imported modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import ttk
from os import closerange
import pytesseract as tess
from PIL import Image,ImageTk
from tkinter import messagebox


global a
def new():
    text.delete(0.0,END)
def new2(event):
    text.delete(0.0,END)
def copy():
    global a
    a = text.get(0.0,END)
def new3(event):
    global a
    a = text.get(0.0,END)
def cut():
    global a
    a = text.get(0.0,END)
    text.delete(0.0,END)
def new5(event):
    global a
    a = text.get(0.0,END)
    text.delete(0.0,END)
def paste():
    global a
    text.insert(END,a)
def new4(event):
    global a
    text.insert(END,a)
def bold():
    text.config(font=("bold"))
def italic():
    text.config(font=("italic"))
def underline():
    text.config(font=("underline")) 
def quit1(event):
    boot.quit()
def quit(event):
    boot.quit()



def new1():
    global vv
    filetypes = (('JPG','*.jpg'),('PNG','*.PNG'),('JPEG','*.JPEG'))
    file1 = filedialog.askopenfilename(filetypes=filetypes)
    img  = Image.open(file1)
    tess.pytesseract.tesseract_cmd = r'C:\Users\INTEL\Desktop\OCR software\Tesseract-OCR\tesseract.exe'
    result = tess.image_to_string(img)
    filetyped = [('Text Docs','*.txt'),('All types','*.*')]
    file2 = asksaveasfilename(filetypes=filetyped)
    with open(file2,mode='w')as file:
        file.write(result)
        messagebox.showinfo("Save","Your File is Saved")
    text_file = open(file2,'r')
    stuff = text_file.read()
    text.insert(END,stuff)
    text_file.close()

boot = Tk()
boot.title("Image To Text - OCR")
boot.geometry("950x700")
boot.config(bg="gray")
boot.iconbitmap("C:\\Users\\INTEL\\Desktop\\OCR software\\images\\icon4.ico")


menubar  = Menu(boot)
file = Menu(menubar, tearoff=0)
file.add_command(label="New   Ctrl+n",command=new)
file.add_command(label="Browse Image",command=new1)
file.add_separator()
file.add_command(label="exit  Ctrl+q",command=quit)
menubar.add_cascade(label="File",menu=file) 
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Cut   Ctrl+x",command=cut)
edit.add_command(label="Copy  Ctrl+c",command=copy)
edit.add_command(label="Paste Ctrl+v",command=paste)
menubar.add_cascade(label="Edit",menu=edit)
format = Menu(menubar, tearoff=0)
format.add_command(label="Bold",command=bold)
format.add_command(label="Italic",command=italic)
format.add_command(label="Underline",command=underline)
menubar.add_cascade(label="Format",menu=format)
boot.config(menu=menubar) 

scroll_bar = Scrollbar(boot)
scroll_bar.pack(side=RIGHT, fill=Y)
text = tk.Text(boot,height=50, width=168,yscrollcommand=scroll_bar.set)
text.place(x=0,y=0)

#bind
boot.bind("<Control-n>",new2)
boot.bind("<Control-c>",new3)
boot.bind("<Control-v>",new4)
boot.bind("<Control-x>",new5)
boot.bind("<Control-q>",quit1)
boot.mainloop()