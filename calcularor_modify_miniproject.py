
#==========================importing module============================================================
from tkinter import* 
window=Tk() 
window.title("Calculator") 
window.geometry("419x405+300+200") 
#window.resizable(0,0)
displayValue=StringVar()
b=StringVar()

#============================operation that need to execute calculation=================================
def shw(value):
    fetchValue=displayValue.get()+value
    displayValue.set(fetchValue)
    
def clear_function():
    displayValue.set("")
    
def result_function():
    displayData=displayValue.get()
    result=eval(displayData)
    displayValue.set(result)
    
def delete_function():
    l=len(dis.get())
    dis.delete(l-1,'end')
    if l==1:
        dis.insert(0,'0')
#============================framing of structue===========================================================

f1=LabelFrame(window,text="Calculator",font=("calbri",15,"bold"),fg='gold',bg='#000080',bd=10,relief=GROOVE)
f1.place(x=0,y=0,width=420,height=410)
#=============================creating display area========================================================= 
dis=Entry(f1,font=("calibri",20,'bold'), textvariable=displayValue,bd=10,insertwidth=5,bg="powder blue",justify="right")
dis.grid(row=0, column=0, padx=5,pady=5, columnspan=6)
#=============================creating buttons for calculator===============================================
btn1=Button(f1,text="7", font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("7"))
btn1.grid(row=2, column=0, padx=5,pady=5)
btn2=Button(f1,text="8",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("8"))
btn2.grid(row=2, column=1, padx=5,pady=5)
btn5=Button(f1,text="9",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("9"))
btn5.grid(row=2, column=2, padx=5,pady=5)
op4=Button(f1,text="/",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("/"))
op4.grid(row=2, column=3 ,padx=5,pady=5)
op1=Button(f1,text="+",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("+"))
op1.grid(row=5, column=3, padx=5,pady=5)

btn4=Button(f1,text="4",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("4"))
btn4.grid(row=3, column=0, padx=5,pady=5)
btn5=Button(f1,text="5",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("5"))
btn5.grid(row=3, column=1, padx=5,pady=5)
btn6=Button(f1,text="6",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("6"))
btn6.grid(row=3, column=2, padx=5,pady=5)
op5=Button(f1,text="*",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("*"))
op5.grid(row=3, column=3, padx=5,pady=5)
op2=Button(f1,text="-",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("-"))
op2.grid(row=4, column=3, padx=5,pady=5)

btn7=Button(f1,text="1",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("1"))
btn7.grid(row=4, column=0, padx=5,pady=5)
btn8=Button(f1,text="2",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("2"))
btn8.grid(row=4, column=1, padx=5,pady=5)
btn9=Button(f1,text="3",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("3"))
btn9.grid(row=4, column=2, padx=5,pady=5)

btn11=Button(f1,text="0",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("0"),anchor='center')
btn11.grid(row=5, column=0, padx=5,pady=5)
btn12=Button(f1,text="Clr",bg="#F00048",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE, command=clear_function)
btn12.grid(row=5, column=1, padx=5,pady=5)
rame1=Button(f1,text="=",bg="#FF4500",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=result_function)
rame1.grid(row=5, column=2, padx=5,pady=5)

btna=Button(f1,text="(",bg="#000000",foreground="white",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("("))
btna.grid(row=1,column=0,padx=5,pady=5)
btnb=Button(f1,text=")",bg="#000000",foreground="white",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw(")"))
btnb.grid(row=1,column=1,padx=5,pady=5)
btnc=Button(f1,text="MRC",bg="#000000",foreground="white",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE)
btnc.grid(row=1,column=2,padx=5,pady=5)
btnd=Button(f1,text="GT",bg="#000000",foreground="white",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE)
btnd.grid(row=1,column=3,padx=5,pady=5)
btne=Button(f1,text="X",bg="red",foreground="white",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=window.destroy)
btne.grid(row=1,column=4,padx=5,pady=5,ipadx=0)

btnf=Button(f1,text="%",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("%"))
btnf.grid(row=2,column=4,padx=5,pady=5)
btng=Button(f1,text=".",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("."))
btng.grid(row=3,column=4,padx=5,pady=5)
btnh=Button(f1,text="**",font=("calibri",14,'bold'),width=3,bd=5,relief=GROOVE,command=lambda:shw("**"))
btnh.grid(row=4,column=4,padx=5,pady=5)
btni=Button(f1,text="DEL",bg="green",font=("calibri",13,'bold'),width=3,bd=5,relief=GROOVE,command=delete_function)
btni.place(x=319,y=310,width=75)

window.mainloop() #tell that python to run the event of the loop through out the programe

#=======================Programee end===================================================================================




