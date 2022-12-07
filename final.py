import trainer as tr
import pandas
import main
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tkMessageBox
root = Tk()
root.geometry('500x500')
root.configure(bg='#C1EFF0')
root.title("Cross Site Scipting(XSS) using Deep Learning")
img = Image.open("C:\mit-1.png")
im = ImageTk.PhotoImage(img)
label1=tkinter.Label(image=im)
label1.image=im
label1.config(bg="#C1EFF0")
label1.place(x=12,y=10)
frame = Frame(root)
frame.pack()
enter_url = Label(root,text = "Enter URL").place(x = 120,y = 150)
input_area = Entry(root,width = 30).place(x = 180,y = 150)


def submitCallBack():
    url = input_area.get()
    main.process_test_url(url, 'test_features.csv')
    return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
    a = str(return_ans).split()
    print("-----")
    print("return_ans:",return_ans)
    print("-----")
    if int(a[1]) == 0:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Benign")
        new=1
        
    elif int(a[1]) == 1:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Malicious or XSSed")
        
    else:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Malicious or XSSed")
        
def about():

    tkMessageBox.showinfo("Credits","Author: Nithesh Kumar.M - Reg.No 17TD0947")
B2 = Button(root, text="Credits",activebackground='#40BA12',command=about).place(x=450,y=470)
b = Button(root,text="Check!",activebackground='#40BA12',command=submitCallBack).place(x=230,y=180)
root.mainloop()