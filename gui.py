import tkinter
from tkinter import *
import tkinter.messagebox as tkMessageBox
import trainer as tr
import webbrowser
import pandas
import main
import PIL.Image
import PIL
from PIL import ImageTk

root = Tk()
root.geometry('495x500')
root.configure(bg='#C1EFF0')
root.title("Cross Site Scripting Detection (XSS) using Deep Learning")
#canvas = Canvas(root, width = 300, height = 450)  
#canvas.pack()
#img = PhotoImage(width=300,height=300)
img = PIL.Image.open('mit-1.png')
im = ImageTk.PhotoImage(img)
label1 = tkinter.Label(image=im)
label1.image=im
label1.config(bg="#C1EFF0")
label1.place(x=12,y=10)
#panel = Label(root, image = img)
#panel.config(bg="#C1EFF0")
#panel.pack()
#img = PhotoImage(Image.open("mit-1.png"))
data = ("{red red red red blue blue blue blue}")
#root.attributes('-alpha',0.9)
root.iconbitmap(r'mit.ico')
#root.configure(background='thistle')
#root.geometry("800x100")
frame = Frame(root)
frame.pack()
#bottomframe = Frame(root)
#bottomframe.pack(side=BOTTOM)

L1 = Label(root, text="Enter the URL Below: ",bg='#01D8D4').place(x = 180,y = 200)

E1 = Entry(root, width=150)
E1.pack(side=LEFT,padx=60, pady=5)


def submitCallBack():
    url = E1.get()
    main.process_test_url(url, 'test_features.csv')
    return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
    a = str(return_ans).split()
    print("-----")
    print("return_ans:",return_ans)
    print("-----")
    if int(a[1]) == 0:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Trusted or Not XSSed")
        new=1
        
    elif int(a[1]) == 1:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Malicious or XSSed")
        
    else:
        tkMessageBox.showinfo("Predicted Result",'"'+url+'"'+ " is Malicious or XSSed")
        

def about():

    tkMessageBox.showinfo("Credits","Guide : Mr.Ashok Kumar.S \nStudents: Nithesh Kumar.M, Balaji.S")


B2=Button(root,text="Credits",activebackground='#40BA12',command=about).place(x=220,y=150)
B1=Button(root,text="Check",activebackground='#40BA12',command=submitCallBack).place(x=225,y=270)
#B2.pack(side=TOP, padx=5, pady=5)
#B1.pack(side=TOP, padx=5,pady=5)
root.mainloop()




