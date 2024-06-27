from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random as r
window=Tk()
window.geometry("900x580")
window.title('BILL')
#window['bg']='lightgreen'#"#000080",#'#00e6e6'

#'#d9d9d9''#00e6e6'
#window.resizable(0,0)

tlab=Label(window,text='BILLING SOFTWARE',font=("calbri",22,"bold"),bd=12,relief=GROOVE,bg='#074463',fg='white').place(x=0,y=0,relwidth=1)
#===cosmetcs
soap1=IntVar()
moist1=IntVar()
face1=IntVar()
face_w1=IntVar()
hair1=IntVar()
gel1=IntVar()
body1=IntVar()
#===grocery
choco1=IntVar()
egg1=IntVar()
tea1=IntVar()
bis1=IntVar()
cof1=IntVar()
bread1=IntVar()
butter1=IntVar()
#======cold
las1=IntVar()
soda1=IntVar()
lem1=IntVar()
soft1=IntVar()
juice1=IntVar()
milk1=IntVar()
mango1=IntVar()
ch1=IntVar()
#======total product price
cos_price=StringVar()
gor_price=StringVar()
cold_price=StringVar()
cos_tax=StringVar()

gor_tax=StringVar()
cold_tax=StringVar()
#======costomer
cname=StringVar()
cphon=StringVar()
bill=StringVar()
x=r.randrange(10000,99999)
bill.set(str(x))
sbill=StringVar()

f1=LabelFrame(window,text='customer detail',font=("calbri",14,"bold"),fg='gold',bg='#074463',bd=10,relief=GROOVE)
f1.place(x=0,y=65,relwidth=1,width=325,height=93)
cl1=Label(f1,text="Customer Name ",font=("calbri",13,"bold"),bg='#074463',fg='white')
cl1.grid(row=0,column=0,padx=15,pady=5)
clen1=Entry(f1,font=("calbri",13,"bold"),width=15,bd=5,relief=SUNKEN,textvariable=cname)
clen1.grid(row=0,column=1,padx=15,pady=5)

cl2=Label(f1,text=" Phone No.",font=("calbri",13,"bold"),bg='#074463',fg='white')
cl2.grid(row=0,column=2,padx=15,pady=5)
clen2=Entry(f1,font=("calbri",13,"bold"),width=15,bd=5,relief=SUNKEN,textvariable=cphon)
clen2.grid(row=0,column=3,padx=15,pady=5)

cl3=Label(f1,text="Bill No.",font=("calbri",13,"bold"),bg='#074463',fg='white')
cl3.grid(row=0,column=4,padx=20,pady=5)
clen3=Entry(f1,font=("calbri",13,"bold"),width=15,bd=5,relief=SUNKEN,textvariable=sbill)
clen3.grid(row=0,column=5,padx=15,pady=5)

btn=Button(f1,text='search',bd=5,relief=GROOVE,font=("calbri",14,"bold"),bg='#00e6e6',fg='black')
btn.grid(row=0,column=6,pady=5,padx=10)


f2=LabelFrame(window,text='Dairy Products ',font=("calbri",15,"bold"),fg='gold',bg='#074463',bd=10,relief=GROOVE)
f2.place(x=0,y=160,width=325,height=370)
#==============Dairy Products
soap=Label(f2,text="FCM 1/2       ",font=("calbri",13,"bold"),bg='#074463',fg='lightgreen')
soap.grid(row=0,column=0,pady=5,padx=15)
soapen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=soap1)
soapen1.grid(row=0,column=1,pady=5,padx=15)

moist=Label(f2,text="FCM 1L",font=("calbri",13,"bold"),bg='#074463',fg='light green')
moist.grid(row=1,column=0,pady=5,padx=15)

moisten1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=moist1)
moisten1.grid(row=1,column=1,pady=5,padx=15)

face=Label(f2,text="COW 1/2",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=2,column=0,pady=5,padx=15,sticky='w')
faceen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=face1).grid(row=2,column=1,pady=5,padx=15)

face_w=Label(f2,text="COW 1L",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=3,column=0,pady=5,padx=15,sticky='w')
face_wen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=face_w1).grid(row=3,column=1,pady=5,padx=15)

hair_s=Label(f2,text="Super 140ml",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=4,column=0,pady=5,padx=15,sticky='w')
hair_sen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=hair1).grid(row=4,column=1,pady=3,padx=15)
gel=Label(f2,text="Hair Gel",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=5,column=0,pady=5,padx=15,sticky='w')
gelen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=gel1).grid(row=5,column=1,pady=3,padx=15)

body=Label(f2,text="Super 320ml",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=6,column=0,pady=5,padx=15,sticky='w')
bodyen1=Entry(f2,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=body1).grid(row=6,column=1,pady=5,padx=15)

f3=LabelFrame(window,text='Culture Product',font=("calbri",13,"bold"),fg='gold',bg='#074463',bd=10,relief=GROOVE)
f3.place(x=327,y=160,width=325,height=370)
#==============grocery
choco=Label(f3,text="COW 160ml",font=("calbri",13,"bold"),bg='#074463',fg='light green')
choco.grid(row=0,column=0,sticky='w',padx=15)
chocoen1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=choco1)
chocoen1.grid(row=0,column=1,pady=5,padx=15)

egg=Label(f3,text="Bufallo 1/2",font=("calbri",13,"bold"),bg='#074463',fg='light green')
egg.grid(row=1,column=0,sticky='w',padx=15)
eggen1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=egg1)
eggen1.grid(row=1,column=1,pady=5,padx=20)

tea=Label(f3,text="Buffalo 1L",font=("calbri",13,"bold"),bg='#074463',fg='light green')
tea.grid(row=2,column=0,sticky='w',padx=15)
teaen1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=tea1)
teaen1.grid(row=2,column=1,pady=5,padx=20)

bis=Label(f3,text="Toned 1/2",font=("calbri",13,"bold"),bg='#074463',fg='light green')
bis.grid(row=3,column=0,sticky='w',padx=15)
bisen1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=bis1)
bisen1.grid(row=3,column=1,pady=5,padx=20)

cof=Label(f3,text="Eco Chach",font=("calbri",13,"bold"),bg='#074463',fg='light green')
cof.grid(row=4,column=0,sticky='w',padx=15)
cofen1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=cof1)
cofen1.grid(row=4,column=1,pady=5,padx=20)

bread=Label(f3,text="Tadka",font=("calbri",13,"bold"),bg='#074463',fg='light green')
bread.grid(row=5,column=0,sticky='w',padx=15)
breaden1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=bread1)
breaden1.grid(row=5,column=1,pady=5,padx=20)

butter=Label(f3,text="200gm pp",font=("calbri",13,"bold"),bg='#074463',fg='light green')
butter.grid(row=6,column=0,sticky='w',padx=15)
butteren1=Entry(f3,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=butter1)
butteren1.grid(row=6,column=1,pady=5,padx=20)

f4=LabelFrame(window,text='.....',font=("calbri",15,"bold"),fg='gold',bg='#074463',bd=10,relief=GROOVE)
f4.place(x=654,y=160,width=325,height=370)
lassi=Label(f4,text="400gm pp",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=0,column=0,sticky='w',padx=15)
lassien1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=las1).grid(row=0,column=1)

soda=Label(f4,text="1L Dahi",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=0,column=0,sticky='w',padx=15)
sodaen1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=soda1).grid(row=0,column=1,pady=5,padx=15)

lemon=Label(f4,text="10 Cup ",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=1,column=0,sticky='w',padx=15)
lemonen1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=lem1).grid(row=1,column=1,pady=5,padx=15)

soft=Label(f4,text="Nova Dahi",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=2,column=0,sticky='w',padx=15)
soften1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=soft1).grid(row=2,column=1,pady=5,padx=15)

juice=Label(f4,text="Bottle Lassi",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=3,column=0,sticky='w',padx=15)
juicen1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=juice1).grid(row=3,column=1,pady=5,padx=15)

milk=Label(f4,text="Pouch Lassi",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=4,column=0,sticky='w',padx=15)
milken1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=milk1).grid(row=4,column=1,pady=5,padx=15)

ch=Label(f4,text="Paneer",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=5,column=0,sticky='w',padx=15)
chen1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=ch1).grid(row=5,column=1,pady=5,padx=15)

ch=Label(f4,text="450ML Chach",font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=6,column=0,sticky='w',padx=15)
chen1=Entry(f4,font=("calbri",13,"bold"),width=8,bd=5,relief=SUNKEN,textvariable=mango1).grid(row=6,column=1,pady=5,padx=15)

#======bill area
f5=Frame(window,bd=10,relief=GROOVE)
f5.place(x=980,y=160,width=310,height=370)
bilt=Label(f5,text='BILL AREA',font=("Arial",15,"bold"),bd=5,relief=GROOVE,bg="#000080",fg='white').grid(sticky=W,ipadx=90)
scr_y=Scrollbar(f5,orient=VERTICAL)
txtarea=Text(f5,yscrollcommand=scr_y.set)
scr_y.grid()
scr_y.config(command=txtarea.yview)
txtarea.grid(sticky='nsew')
def welcome():
    txtarea.delete('1.0',END)
    txtarea.insert(END,'\tWelcome Shiv Dairy Retails\n')
    txtarea.insert(END,f'\n Bill Number : {bill.get()}')
    txtarea.insert(END,f'\n Customer Name : {cname.get()}')
    txtarea.insert(END,f'\n Phone Number : {cphon.get()}')
    txtarea.insert(END,f'\n ====================================')
    txtarea.insert(END,f'\n Products\t\tQTY\t\tPrice')
    txtarea.insert(END,f'\n ====================================')
welcome()
#===button
f6=LabelFrame(window,text='Bill Menu',font=("calbri",15,"bold"),fg='gold',bg='#074463',bd=10,relief=GROOVE)
f6.place(x=0,y=535,relwidth=1,height=165)
m1=Label(f6,text='Total Cosmetics Price',font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=0,column=0,sticky='w')
m1en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=cos_price).grid(row=0,column=1,padx=15,pady=3)

m2=Label(f6,text='Total Grocery price',font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=1,column=0,sticky='w')
m2en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=gor_price).grid(row=1,column=1,padx=15,pady=3)

m3=Label(f6,text='Total Cold Drink Price',font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=2,column=0,sticky='w')
m3en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=cold_price).grid(row=2,column=1,padx=15,pady=3)

m4=Label(f6,text='cosmatic Tax',font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=0,column=2,sticky='w')
m4en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=cos_tax).grid(row=0,column=3,padx=15,pady=3)

m5=Label(f6,text='Grocery Tax',font=("calbri",13,"bold"),bg='#074463',fg='light green').grid(row=1,column=2,sticky='w')
m5en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=gor_tax).grid(row=1,column=3,padx=15,pady=3)

m6=Label(f6,text='Cold Drink Tax',font=("calbri",14,"bold"),bg='#074463',fg='light green').grid(row=2,column=2,sticky='w')
m6en1=Entry(f6,width=7,font=("calbri",13,"bold"),bd=5,relief=SUNKEN,textvariable=cold_tax).grid(row=2,column=3,padx=15,pady=3)
#m7=Label(f6,text='created by pintu').grid(row=2,column=5,padx=30)
f7=Frame(f6,bd=5,relief=GROOVE)
f7.place(x=670,width=580,height=100)
tbtn=Button(f7,text='Total',bg='cadetblue',fg='black',width=5,font=("calbri",14,"bold"),bd=5,anchor='center',command=lambda:total()).grid(row=0,column=0,ipadx=5,ipady=7,padx=7,pady=3)
tbtn=Button(f7,text='Generate Bill',bg='cadetblue',fg='black',width=5,font=("calbri",14,"bold"),bd=5,anchor='center',command=lambda:billarea()).grid(row=0,column=1,ipadx=24,ipady=7,padx=7,pady=5)
tbtn=Button(f7,text='Clear',bg='cadetblue',fg='black',width=5,font=("calbri",14,"bold"),bd=5,anchor='center').grid(row=0,column=2,ipadx=5,ipady=7,padx=7,pady=5)
tbtn=Button(f7,text='Exit',bg='cadetblue',fg='black',width=5,font=("calbri",14,"bold"),bd=5,anchor='center',command=window.destroy).grid(row=0,column=3,ipadx=5,ipady=7,padx=7,pady=10)
"""def clear():
    soap1.delete(0,END)
    moist1.delete(0,END)
    face1.delete(0,END)
    face_w1.delete(0,END)
    hair1.delete(0,END)
    gel1.delete(0,END)
    body1.delete(0,END)
    choco1.delete(0,END)
    egg1.delete(0,END)
    tea1.delete(0,END)
    bis1.delete(0,END)
    cof1.delete(0,END)
    bread1.delete(0,END)
    butter1.delete(0,END)
    las1.delete(0,END)
    soda1.delete(0,END)
    lem1.delete(0,END)
    soft1.delete(0,END)
    juice1.delete(0,END)
    milk1.delete(0,END)
    mango1.delete(0,END)
    ch1.delete(0,END)
    cos_price.delete(0,END)
    gor_price.delete(0,END)
    cold_price.delete(0,END)
    cos_tax.delete(0,END)

    gor_tax.delete(0,END)
    cold_tax.delete(0,END)"""
def total():    
    totalp=float(
        soap1.get()*40+
        face1.get()*120+
        face_w1.get()*60+
        hair1.get()*160+
        gel1.get()*90+
        moist1.get()*130+
        body1.get()*210
        )
    cos_price.set("Rs "+str(totalp))
    cos_tax.set("Rs "+str(round((totalp*0.05),2)))

    
    totalGp=float(
        choco1.get()*70+
        egg1.get()*10+
        tea1.get()*50+
        bis1.get()*20+
        cof1.get()*100+
        bread1.get()*35+
        butter1.get()*52
        )
    gor_price.set("Rs "+str(totalGp))
    gor_tax.set("Rs "+str(round((totalGp*0.05),2)))

    
    totalCDp=float(
        las1.get()*30+
        soda1.get()*20+
        lem1.get()*200+
        soft1.get()*65+
        juice1.get()*60+
        milk1.get()*57+
        mango1.get()*50
        )
    cold_price.set("Rs "+str(totalCDp))
    cold_tax.set("Rs "+str(round((totalCDp*0.05),2)))
def billarea():
    welcome()
    cname.get()
    cphon.get()

window.mainloop()












