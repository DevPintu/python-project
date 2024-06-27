#project to pronounce words and if its website then its open in new tab of chrome 
from tkinter import*
import os
import webbrowser as wb
from tkinter import messagebox
import time as t

window=Tk()
window.geometry("385x280+250+150")
window.title("WEBSITE EXPLORER")
window['bg']="white"
window.resizable(False,False)


def pronounce():
    word=text_entry.get()
    search=text_entry1.get('1.0','end')
    if text_entry.get()=="" :
            messagebox.showerror("Error","All Fields are Required")
    web_name=['apple','chrome','google','bing','microsoft','yahoo','facebook','youtube','amazon','instagram','twitter','duckduckgo','flipkart']
    if word=="q":
        os.system("say 'bye bye friend'")
    else:
        speak=f"say {word}{search}"
        os.system(speak)
        for i in web_name:
            if word==i:
                if i=="youtube":
                    enter=search.split()
                    joined='+'.join(enter)
                    t.sleep(1)
                    web1=f'https://{i}.com/results?search_query={joined}'
                    wb.open(web1)
                    break
                if i=="google":
                    enter=search.split()    
                    joined='+'.join(enter)
                    t.sleep(1)
                    web1=f'https://{i}.com/search?q={joined}'
                    wb.open(web1)
                    break
                if i=="amazon":
                    enter=search.split()    
                    joined='+'.join(enter)
                    t.sleep(1)
                    web1=f'https://{i}.com/s?k={joined}'
                    wb.open(web1)
                    break
                if i=="bing":
                    enter=search.split()    
                    joined='+'.join(enter)
                    t.sleep(1)
                    web1=f'https://{i}.com/search?q={joined}'
                    wb.open(web1)
                    break
                else:
                    web1=f'https://{i}.com/'
                    wb.open(web1)

def clear():
   text_entry.delete(0,END)
   text_entry1.delete('1.0',END)
#1e81b0 #cc2b5e}{#004e92}
fram=LabelFrame(window,text="TEXT TO SEARCH",font=("calbri",15,"bold"),relief=RIDGE,bd=5,bg="#0492c2",fg="#FFF")
fram.place(x=0,y=0,height=280,width=385)
label_text=Label(fram,text="Website ",font=("calbri",18,"bold"),bg="#0492c2",fg="white")
label_text.place(x=10,y=20)
text_entry=Entry(fram,font=("calbri",13,"bold"),width=17,bd=7,relief=SUNKEN,insertwidth=0.5)
text_entry.place(x=140,y=20)
label_text1=Label(fram,text="Search",font=("calbri",20,"bold"),bg="#0492c2",fg="white")
label_text1.place(x=10,y=80)
text_entry1=Text(fram,font=("calbri",13,"bold"),width=17,bd=7,relief=SUNKEN,insertwidth=0.5,height=3,wrap='word')
text_entry1.place(x=140,y=80)
btn_clear=Button(fram,text="clear",font=("calbri",13,"bold"),relief=GROOVE,fg="white",bd=5,bg="crimson",command=clear)
btn_clear.place(x=155,y=195)
btn=Button(fram,text="Speak",font=("calbri",13,"bold"),relief=GROOVE,fg="green",bd=5,bg="white",command=pronounce,width=5)
btn.place(x=20,y=195)
btn_close=Button(fram,text="Exit",font=("calbri",13,"bold"),relief=GROOVE,fg="#fff",bd=5,bg="red",command=window.destroy)
btn_close.place(x=280,y=195)

window.mainloop()

