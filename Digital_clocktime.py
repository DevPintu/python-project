from tkinter import *
import time
import calendar as c
#from datetime import date
window=Tk()
window.geometry("340x200+300+200")
window['bg']="black"
window.title(" Digital Clock")
#window.resizable(0,0)
def year_month():
    pass
def clock():
    cur_month=time.strftime("%b")
    cur_date=time.strftime("%d")
    current_time=time.strftime("%X")
    current_meridian=time.strftime("%p")
    label1 ["text"]=current_time,current_meridian
    label2 ["text"]=cur_date,cur_month
    window.after(1000,clock)
    
frame_time=LabelFrame(window,bd=10,highlightthickness=2,relief=GROOVE,bg="navy blue",text=" Digital clock",font=("calbri",15,"bold"),fg='gold')
frame_time.place(height="200",width="340")
label1=Label(frame_time,font=("article 35",31,"bold"),bg="navy blue",fg="white")
label1.place(x=10,y=70)
#btn_month=Button(frame_time,font=("Z003",38,"bold"),bg="navy blue",fg="#00FFFF")
#btn_month.place(x=90,y=10)
label2=Label(frame_time,font=("Z003",38,"bold"),bg="navy blue",fg="#00FFFF")
label2.place(x=90,y=10)
clock()

"""yy=int(input("enter year :"))
mm=int(input("enter month :"))
m=(c.month(yy,mm))
print(m)"""
