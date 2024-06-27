import calendar as c
from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("400x220+400+200")
window.title('CALENDAR')

yy=StringVar()
mm=StringVar()

f2=LabelFrame(window,text='Calendar',font=("calbri",14,"bold"),fg='gold',bg='#0744ba',bd=10,relief=GROOVE)
f2.place(x=0,y=0,width=400,height=220)

lab1=Label(f2,text='Year :',font=("calbri",15,"bold"),bg='#0744ba',fg='#ffffff')
lab1.grid(row=0,column=0,padx=10,pady=10)

ent1=Entry(f2,font=("calbri",15,"bold"),width=12,bd=5,relief=SUNKEN,textvariable=yy)
ent1.grid(row=0,column=1,padx=10,pady=5)

lab2=Label(f2,text='Month :',font=("calbri",15,"bold"),bg='#0744ba',fg='#ffffff')
lab2.grid(row=1,column=0,padx=15,pady=5)


ent2=Entry(f2,font=("calbri",15,"bold"),width=12,bd=5,relief=SUNKEN,textvariable=mm)
ent2.grid(row=1,column=1,padx=15,pady=5)

btn=Button(f2,text='Show',bd=5,relief=GROOVE,font=("calbri",14,"bold"),bg='#00e6e6',fg='black',command=lambda:search())
btn.place(x=120,y=120)

def search():
    if ent1.get()=="":
         messagebox.showerror("Error","All fields are Required")
    elif ent2.get()=="":
        messagebox.showerror("Error","All fields are Required")
    year=int(ent1.get())
    month=ent2.get()
    if month in'january':
        month=1
    elif month=='february':
        month=2
    elif month=='march':
        month=3
    elif month=='april':
        month=4
    elif month=='may':
        month=5
    elif month=='june':
        month=6
    elif month=='july':
        month=7
    elif month=='august':
        month=8
    elif month=='september':
        month=9
    elif month=='october':
        month=10
    elif month=='november':
        month=11
    elif month=='december':
        month=12
    ym=c.month(year,month)
    messagebox.showinfo("calendar",ym)
    

    
"""yy=int(input("enter year :"))
mm=int(input("enter month :"))
m=(c.month(yy,mm))
print(m)"""

"""month=int(input("Enter month no :"))
if month==1:
    print('january'.capitalize())
elif month==2:
    print('february'.capitalize())
elif month==3:
    print('march'.capitalize())
elif month==4:
    print('april'.capitalize())
elif month==5:
    print('may'.capitalize())
elif month==6:
    print('june'.capitalize())
elif month==7:
    print('july'.capitalize())
elif month==8:
    print('august'.capitalize())
elif month==9:
    print('september'.capitalize())
elif month==10:
    print('october'.capitalize())
elif month==11:
    print('november'.capitalize())
elif month==12:
    print('december'.capitalize())
else:
    print("pls enter from 1 to 12 to get result")"""
