import os
from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("200x80+400+300")
win.title('creation')

def creation():
    window=Tk()
    window.geometry("376x225+300+200")
    window.title('folder')
    
    file=StringVar()
    loc=StringVar()

    f2=LabelFrame(window,text='folder',font=("calbri",14,"bold"),fg='gold',bg='#000066',bd=10,relief=GROOVE)
    f2.place(x=0,y=0,width=375,height=225)
    lab1=Label(f2,text='File Name :',font=("calbri",15,"bold"),bg='#000066',fg='#ffffff')
    lab1.grid(row=1,column=0,padx=10,pady=5)
    ent1=Entry(f2,font=("calbri",15,"bold"),width=12,bd=5,relief=SUNKEN,textvariable=file)
    ent1.grid(row=1,column=1,padx=10,pady=5)
    lab2=Label(f2,text='Location :',font=("calbri",15,"bold"),bg='#000066',fg='#ffffff')
    lab2.grid(row=0,column=0,pady=5,sticky=W,padx=10)
    ent2=Entry(f2,font=("calbri",15,"bold"),width=12,bd=5,relief=SUNKEN,textvariable=loc)
    ent2.grid(row=0,column=1,padx=15,pady=5)
    
    btn=Button(f2,text='Submit',bd=5,relief=GROOVE,font=("calbri",14,"bold"),bg='#00e6e6',fg='black',command=lambda:submit())
    btn.place(x=100,y=120)
    def submit():
        file_name=ent1.get()
        location=ent2.get()
        combine=os.getcwd()+'/'+location.capitalize()+'/'+file_name.capitalize()
        os.mkdir(combine)
        let=location.capitalize()
        #messagebox.showinfo("Doucuments","folder created successfully in location")
        variable="folder created successfully in location i.e -"+"\n",let
        messagebox.showinfo("Doucuments",variable)
        
btn1=Button(win,text='create'.upper(),bd=5,relief=GROOVE,font=("calbri",14,"bold"),bg='#008080',fg='white',command=lambda:creation())
btn1.place(x=0,y=0,width=200,height=80)
win.mainloop()
