from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import time as t
window=Tk()
window.geometry("300x200+250+150")
window.title("file reader")

def new_upload():
    sel="Please: \n Select only .txt file"
    messagebox.showinfo("info",sel)
    c=fd.askopenfilename()
    new_win=Tk()    
    new_win.title("NEW WINDOW")
    new_win.geometry("565x475+230+150")
    new_win['bg']="white"
    s=open(c,'r')
    q=s.read()

    def Read():
        with open(c,'r') as spk:
            sp=spk.readlines()
            #print(sp)
            speech=f"say {sp}"
            t.sleep(1)
            os.system(speech)
    
    f1=LabelFrame(new_win,text="Area",font=("calbri",15,"bold"),bg="#008070",bd=8,fg="white")
    f1.place(x=0,y=0,width=565,height=475)
    btn_read=Button(f1,text="Read file",font=("calbri",13,"bold"),relief=GROOVE,fg="#fff",bd=5,bg="#5a4bda",command=Read)
    btn_read.place(x=80,y=390,)
    btn_close=Button(f1,text="Close",font=("calbri",13,"bold"),relief=GROOVE,fg="red",bd=5,bg="white",command=new_win.destroy)
    btn_close.place(x=390,y=390)
    txt1=Text(f1,font=('calibri',14,'bold'),wrap='word')
    txt1.place(x=10,y=0,width=520,height=375)
    txt1.insert('1.0',q)
    s.close()

fram=LabelFrame(window,text="FILE READER",font=("calbri",15,"bold"),relief=GROOVE,bd=5,bg="sandybrown",fg="#FFF")
fram.place(x=0,y=0,height=200,width=300)
btn=Button(fram,text="Upload file",font=("calbri",13,"bold"),relief=GROOVE,fg="#fff",bd=5,bg="green",command=new_upload)
btn.place(x=80,y=50)
btn_close=Button(fram,text="Close",font=("calbri",13,"bold"),relief=GROOVE,fg="red",bd=5,bg="white",width=9,command=window.destroy)
btn_close.place(x=80,y=120)

window.mainloop()
