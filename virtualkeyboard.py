from tkinter import*
window=Tk()
window.geometry("950x570")
window.title("virtual keyboard")
#window['bg']='blue'
abc=StringVar()
x=[]
def press(value):
    x.append(txt1.get('end')+value)
    txt1.insert('end',x[-1])
    global l
    l=len(x)
    abc.set(l)
    
def press(value):
    x=txt1.get('end')+value
    txt1.insert('end',x)
    
def backsp():
    txt1.delete('end-2c')
    """l=len(x)
    txt1.delete("1.l",'end')
    abc.set(l)"""
    
def space():
    txt1.insert('insert',' ')
    
def enter():
    txt1.insert('insert','\n')

def tab():
    txt1.insert('insert','\t')

def call():
    pass
def delet():
    global l
    l=len(x)
    txt1.delete('1.l','end')
    abc.set(l)
    #l=len(txt1.get("0.0","end"))
    #txt1.delete(l-1,'end')
    
f1=LabelFrame(window,text="Area",font=("calbri",15,"bold"),bg="#008070",bd=8,fg="white")
f1.place(x=0,y=0,width=1295,height=328)
    
txt1=Text(f1,font=('calibri',14,'bold'))
txt1.place(x=10,y=0,width=1257,height=279.7)

f2=LabelFrame(window,text="keyboard",font=("calbri",15,"bold"),bg="black",bd=8,fg="white")
f2.place(x=0,y=328,width=1295,height=375)

esc=Button(f2,text="Esc",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("Esc"),bg="#000000",fg="white",anchor=CENTER)
esc.place(x=15,y=0,width=50,height=40)
f1=Button(f2,text="F1",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F1"),bg="#000000",fg="white")
f1.place(x=73,y=0,width=50,height=40)
fa2=Button(f2,text="F2",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F2"),bg="#000000",fg="white")
fa2.place(x=130,y=0,width=50,height=40)
f3=Button(f2,text="F3",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F3"),bg="#000000",fg="white")
f3.place(x=190,y=0,width=50,height=40)
f4=Button(f2,text="F4",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F4"),bg="#000000",fg="white")
f4.place(x=250,y=0,width=50,height=40)
f5=Button(f2,text="F5",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F5"),bg="#000000",fg="white")
f5.place(x=310,y=0,width=50,height=40)
f6=Button(f2,text="F6",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F6"),bg="#000000",fg="white")
f6.place(x=370,y=0,width=50,height=40)
f7=Button(f2,text="F7",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F7"),bg="#000000",fg="white")
f7.place(x=430,y=0,width=50,height=40)
f8=Button(f2,text="F8",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F8"),bg="#000000",fg="white")
f8.place(x=490,y=0,width=50,height=40)
f9=Button(f2,text="F9",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F9"),bg="#000000",fg="white")
f9.place(x=550,y=0,width=50,height=40)
f10=Button(f2,text="F10",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F10"),bg="#000000",fg="white")
f10.place(x=610,y=0,width=50,height=40)
f11=Button(f2,text="F11",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F11"),bg="#000000",fg="white")
f11.place(x=670,y=0,width=50,height=40)
f12=Button(f2,text="F12",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F12"),bg="#000000",fg="white")
f12.place(x=730,y=0,width=50,height=40)
prt=Button(f2,text="prt", font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("Esc"),bg="#000000",fg="white")
prt.place(x=790,y=0,width=50,height=40)
ins=Button(f2,text="Inst",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F1"),bg="#000000",fg="white")
ins.place(x=850,y=0,width=50,height=40)
dele=Button(f2,text="del",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white",command=delet)
dele.place(x=910,y=0,width=52,height=40)

page=Button(f2,text="PG",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F3"),bg="#000000",fg="white")
page.place(x=1028,y=0,width=50,height=40)
pgdn=Button(f2,text="pgdn",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F4"),bg="#000000",fg="white")
pgdn.place(x=1088,y=0,width=50,height=40)
hom=Button(f2,text="HoM",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F3"),bg="#000000",fg="white")
hom.place(x=1148,y=0,width=50,height=40)
end=Button(f2,text="End",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F4"),bg="#000000",fg="white")
end.place(x=1208,y=0,width=50,height=40)


tild=Button(f2,text="~", font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("~"),bg="#000000",fg="white")
tild.place(x=15,y=52,width=50,height=45)
bb1=Button(f2,text="!",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("!"),bg="#000000",fg="white")
bb1.place(x=76,y=52,width=50,height=45)
bb2=Button(f2,text="@",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("@"),bg="#000000",fg="white")
bb2.place(x=142,y=52,width=50,height=45)
bb3=Button(f2,text="#",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("#"),bg="#000000",fg="white")
bb3.place(x=204,y=52,width=50,height=45)
bb4=Button(f2,text="$",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("$"),bg="#000000",fg="white")
bb4.place(x=268,y=52,width=50,height=45)
bb5=Button(f2,text="%",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("%"),bg="#000000",fg="white")
bb5.place(x=336,y=52,width=50,height=45)
bb6=Button(f2,text="^",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("^"),bg="#000000",fg="white")
bb6.place(x=403,y=52,width=50,height=45)
bb7=Button(f2,text="&",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("&"),bg="#000000",fg="white")
bb7.place(x=467,y=52,width=50,height=45)
bb8=Button(f2,text="*",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("*"),bg="#000000",fg="white")
bb8.place(x=529,y=52,width=50,height=45)
bb9=Button(f2,text="(",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("("),bg="#000000",fg="white")
bb9.place(x=591,y=52,width=50,height=45)
bb10=Button(f2,text=")",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(")"),bg="#000000",fg="white")
bb10.place(x=653,y=52,width=50,height=45)
bb11=Button(f2,text="_",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("_"),bg="#000000",fg="white")
bb11.place(x=715,y=52,width=50,height=45)
bb12=Button(f2,text="=",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("="),bg="#000000",fg="white")
bb12.place(x=777,y=52,width=50,height=45)
bb13=Button(f2,text="Backspace",font=("calibri",14),width=3,bd=5,relief=GROOVE,bg="#000000",fg="white",command=backsp)
bb13.place(x=839,y=52,width=123,height=45)


numl=Button(f2,text="No.L",font=("calibri",14),width=1,bd=5,relief=GROOVE)
numl.place(x=1028,y=52,width=49,height=45)
p4=Button(f2,text="/",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("/"))
p4.place(x=1088,y=52,width=49,height=45)
p1=Button(f2,text="*",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("*"))
p1.place(x=1148,y=52,width=49,height=45)
p2=Button(f2,text="-",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("-"))
p2.place(x=1208,y=52,width=49,height=45)



tab=Button(f2,text="Tab", font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white",command=tab)
tab.place(x=15,y=109,width=84,height=45)
btn1=Button(f2,text="Q", font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("Q"),bg="#000000",fg="white")
btn1.place(x=117,y=107,width=50,height=45)
btn2=Button(f2,text="W",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("W"),bg="#000000",fg="white")
btn2.place(x=181,y=107,width=50,height=45)
btn5=Button(f2,text="E",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("E"),bg="#000000",fg="white")
btn5.place(x=245,y=107,width=50,height=45)
op4=Button(f2,text="R",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("R"),bg="#000000",fg="white")
op4.place(x=311,y=107,width=50,height=45)
op1=Button(f2,text="T",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("T"),bg="#000000",fg="white")
op1.place(x=377,y=107,width=50,height=45)
btn4=Button(f2,text="Y",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("Y"),bg="#000000",fg="white")
btn4.place(x=443,y=107,width=50,height=45)
btn5=Button(f2,text="U",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("U"),bg="#000000",fg="white")
btn5.place(x=509,y=107,width=50,height=45)
btn6=Button(f2,text="I",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("I"),bg="#000000",fg="white")
btn6.place(x=575,y=107,width=50,height=45)
op5=Button(f2,text="O",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("O"),bg="#000000",fg="white")
op5.place(x=641,y=107,width=50,height=45)
op2=Button(f2,text="P",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("P"),bg="#000000",fg="white")
op2.place(x=707,y=107,width=50,height=45)
op6=Button(f2,text="[",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("["),bg="#000000",fg="white")
op6.place(x=773,y=107,width=50,height=45)
opp=Button(f2,text="]",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("]"),bg="#000000",fg="white")
opp.place(x=839,y=107,width=50,height=45)
opp1=Button(f2,text="|",font=("calibri",14), width=1,bd=5,relief=GROOVE,command=lambda:press("|"),bg="#000000",fg="white")
opp1.place(x=909,y=107,width=50,height=45)

n1=Button(f2,text="7", font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("7"))
n1.place(x=1028,y=107,width=49,height=45)
n2=Button(f2,text="8",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("8"))
n2.place(x=1088,y=107,width=49,height=45)
n5=Button(f2,text="9",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("9"))
n5.place(x=1148,y=107,width=49,height=45)
plus=Button(f2,text="+",font=("calibri",14,'bold'),height=4,bd=5,relief=GROOVE,bg="#000000",fg="white",command=lambda:press("+"))
plus.place(x=1208,y=107,width=49,height=102)

cap=Button(f2,text="CapsLock",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(""),bg="#000000",fg="white")
cap.place(x=15,y=162,width=104,height=45)
btn7=Button(f2,text="A",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("A"),bg="#000000",fg="white")
btn7.place(x=132,y=162,width=50,height=45)
btn8=Button(f2,text="S",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("S"),bg="#000000",fg="white")
btn8.place(x=198,y=162,width=50,height=45)
btn9=Button(f2,text="D",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("D"),bg="#000000",fg="white")
btn9.place(x=264,y=162,width=50,height=45)
btn11=Button(f2,text="F",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("F"),bg="#000000",fg="white")
btn11.place(x=330,y=162,width=50,height=45)
btn12=Button(f2,text="G",font=("calibri",14),width=1,bd=5,relief=GROOVE, command=lambda:press("G"),bg="#000000",fg="white")
btn12.place(x=396,y=162,width=50,height=45)
rame1=Button(f2,text="H",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("H"),bg="#000000",fg="white")
rame1.place(x=462,y=162,width=50,height=45)
btna=Button(f2,text="J",bg="#000000",fg="white",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("J"))
btna.place(x=528,y=162,width=50,height=45)
btnb=Button(f2,text="K",bg="#000000",fg="white",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("K"))
btnb.place(x=594,y=162,width=50,height=45)
btnc=Button(f2,text="L",bg="#000000",fg="white",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("L"))
btnc.place(x=660,y=162,width=50,height=45)
btnd=Button(f2,text=";",bg="#000000",fg="white",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(";"))
btnd.place(x=726,y=162,width=50,height=45)
btne=Button(f2,text="'",bg="#000000",fg="white",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("'"))
btne.place(x=792,y=162,width=50,height=45)
ent=Button(f2,text="Enter",font=("calibri",14),width=7,bd=5,relief=GROOVE,bg="#000000",fg="white",command=enter)
ent.place(x=858,y=162,width=102,height=45)

n4=Button(f2,text="4",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("4"))
n4.place(x=1028,y=162,width=50,height=45)
na5=Button(f2,text="5",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("5"))
na5.place(x=1088,y=162,width=50,height=45)
n6=Button(f2,text="6",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("6"))
n6.place(x=1148,y=162,width=50,height=45)

shift=Button(f2,text="Shift",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("A"),bg="#000000",fg="white")
shift.place(x=15,y=218,width=122,height=45)
btnf=Button(f2,text="Z",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("Z"),bg="#000000",fg="white")
btnf.place(x=154,y=218,width=50,height=45)
btng=Button(f2,text="X",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("X"),bg="#000000",fg="white")
btng.place(x=220,y=218,width=50,height=45)
btnh=Button(f2,text="C",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("C"),bg="#000000",fg="white")
btnh.place(x=286,y=218,width=50,height=44)
btni=Button(f2,text="V",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("V"),bg="#000000",fg="white")
btni.place(x=352,y=218,width=50,height=45)
btnj=Button(f2,text="B",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("B"),bg="#000000",fg="white")
btnj.place(x=418,y=218,width=50,height=45)
btnk=Button(f2,text="N",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("N"),bg="#000000",fg="white")
btnk.place(x=484,y=218,width=50,height=45)
btnl=Button(f2,text="M",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("M"),bg="#000000",fg="white")
btnl.place(x=550,y=218,width=50,height=45)
btnm=Button(f2,text=",",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(","),bg="#000000",fg="white")
btnm.place(x=616,y=218,width=50,height=45)
btnn=Button(f2,text=".",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("."),bg="#000000",fg="white")
btnn.place(x=682,y=218,width=50,height=45)
btno=Button(f2,text="/",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press("/"),bg="#000000",fg="white")
btno.place(x=748,y=218,width=50,height=45)
shift1=Button(f2,text="Shift",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
shift1.place(x=814,y=218,width=143,height=45)

n7=Button(f2,text="1",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("1"))
n7.place(x=1028,y=218,width=49,height=45)
n8=Button(f2,text="2",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("2"))
n8.place(x=1088,y=218,width=49,height=45)
n9=Button(f2,text="3",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("3"))
n9.place(x=1148,y=218,width=49,height=45)

ctr=Button(f2,text="Ctrl",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
ctr.place(x=15,y=273,width=50,height=45)
fn=Button(f2,text="Fn",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
fn.place(x=88,y=273,width=50,height=45)
win=Button(f2,text="win",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
win.place(x=153,y=273,width=50,height=45)
alt=Button(f2,text="Alt",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
alt.place(x=220,y=273,width=50,height=45)
space=Button(f2,text="SpaceBar",font=("calibri",14),width=20,bd=5,relief=GROOVE,bg="#000000",fg="white",command=space)
space.place(x=286,y=273,width=314,height=45)
alt1=Button(f2,text="Alt",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
alt1.place(x=616,y=273,width=50,height=45)
ctr1=Button(f2,text="Crlt",font=("calibri",14),width=1,bd=5,relief=GROOVE,bg="#000000",fg="white")
ctr1.place(x=682,y=273,width=50,height=45)

fl1=Button(f2,text="<-",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(""),bg="#000000",fg="white")
fl1.place(x=748,y=297,width=50,height=30)
fd1=Button(f2,text="^d",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(""),bg="#000000",fg="white")
fd1.place(x=824,y=295,width=50,height=30)
fu1=Button(f2,text="^u",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(""),bg="#000000",fg="white")
fu1.place(x=824,y=268,width=50,height=30)
fr1=Button(f2,text="->",font=("calibri",14),width=1,bd=5,relief=GROOVE,command=lambda:press(""),bg="#000000",fg="white")
fr1.place(x=898,y=295,width=50,height=30)


btn11=Button(f2,text="0",font=("calibri",14,'bold'),width=5,bd=5,relief=GROOVE,command=lambda:press("0"))
btn11.place(x=1028,y=273,width=105,height=47)
na6=Button(f2,text=".",font=("calibri",14,'bold'),width=1,bd=5,relief=GROOVE,command=lambda:press("."))
na6.place(x=1148,y=273,width=49,height=47)
en1=Button(f2,text="Ent",font=("calibri",14),height=4,bd=5,relief=GROOVE,bg="#000000",fg="white",command=enter)
en1.place(x=1208,y=218,width=49,height=104)

window.mainloop()
