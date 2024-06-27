from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("222x270+400+200")
window.title("SUDOKO GAME")
window.resizable(0,0)
f2=LabelFrame(window,text='SUDOKO',font=("calbri",15,"bold"),fg='gold',bg='#000080',bd=8,relief=GROOVE)
f2.place(x=0,y=0,width=220,height=270)

row1=StringVar()
row2=StringVar()
row3=StringVar()

row4=StringVar()
row5=StringVar()
row6=StringVar()

row7=StringVar()
row8=StringVar()
row9=StringVar()


tea=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row1)
tea.grid(row=1,column=0)

te=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row2)
te.grid(row=1,column=1)

t=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row3)
t.grid(row=1,column=2)

t1=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row4)
t1.grid(row=2,column=0)

tn1=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row5)
tn1.grid(row=2,column=1)

te1=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row6)
te1.grid(row=2,column=2)

t2=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row7)
t2.grid(row=3,column=0)
t01=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row8)
t01.grid(row=3,column=1)
t10=Entry(f2,font=("calbri",13,"bold"),width=3,bd=5,relief=SUNKEN,textvariable=row9)
t10.grid(row=3,column=2)

f3=Frame(f2,bd=5,relief=FLAT,pady=3,bg='#000080')
f3.place(x=0,y=112,width=197,height=60)
lab=Label(f2,text="Instruction:fill all cells\nwhose row&column\nsum is 15 ",font=("calbri",13,"bold"),bg='#000080',fg='red')
lab.place(x=0,y=170)
btn=Button(f3,text='SUBMIT',font=("calbri",13,"bold"),width=4,bd=3,relief=GROOVE,command=lambda:sub())
btn.grid(row=0,column=0,ipady=2,ipadx=4,padx=5)
btn1=Button(f3,text='CLEAR',font=("calbri",13,"bold"),width=4,bd=3,relief=GROOVE,command=lambda:clear())
btn1.grid(row=0,column=1,ipady=2)

def sub():
    R=int(tea.get())+int(te.get())+int(t.get())
    R1=int(t1.get())+int(tn1.get())+int(te1.get())
    R2=int(t2.get())+int(t01.get())+int(t10.get())
    
    C=int(tea.get())+int(t1.get())+int(t2.get())
    C1=int(te.get())+int(tn1.get())+int(t01.get())
    C2=int(t.get())+int(te1.get())+int(t10.get())

    if R==15 and R1==15 and R2==15 and C==15 and C1==15 and C2==15: 
        messagebox.showinfo("information",'you won the game ')
        messagebox.showinfo("information",'Thank you\nVisit Again!')
        
    else:
        messagebox.showerror("ERROR","TRY AGAIN :(:")
        
def clear():
    tea.delete(0,END)
    te.delete(0,END)
    t.delete(0,END)
    t1.delete(0,END)
    tn1.delete(0,END)
    te1.delete(0,END)
    t2.delete(0,END)
    t01.delete(0,END)
    t10.delete(0,END)

#hint [1,8,6,5,3,7,9,4,2]
