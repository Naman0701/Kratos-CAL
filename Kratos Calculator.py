import tkinter as tk

test=tk.Tk()
i=1920;j=1080
test.geometry(f'{i}x{j}')
test.title('NA Calculator')
img=tk.PhotoImage(file= r'icon\IMN00.png')
bimg=tk.PhotoImage(file= r'icon\IMN000.png')

win=tk.Label(test,image=img)
win.place(x=-50*4,y=-50*2)


test.wm_iconbitmap('krato.ico')
# Icon ka path
def dele(event=None):
    global exp
    exps=exp[:-1]
    print(exp,exps)
    exp=exps
    in_txt.set(exp)
def click(item,event=None):
    global exp
    try:
        exp+= str(item)
        in_txt.set(exp)
    except:
        exp=''
        in_txt.set(exp)

def clr(event=None):
    global exp
    exp=''
    in_txt.set('')
def eq(event=None):
    global exp
    try:
        result=str(eval(exp))
        result=float(result)
        result=round(result,5)
        result=str(result)
        in_txt.set(result)
        exp=result
    except ZeroDivisionError:
        in_txt.set('Can not divide by 0')
        exp=''
    except:
        exp=''
        in_txt.set('ERROR')

exp=''
in_txt=tk.StringVar()

in_fr= tk.Frame(test,width=i/1.5,height=50,bd=2,bg='white',highlightbackground='black',highlightcolor='black',highlightthickness=2)
in_fr.pack(side=tk.TOP)

in_field=tk.Entry(in_fr,font=('Algerian',22,'bold'),textvariable=in_txt,width=50,bg='black',fg='white',bd=0,justify=tk.RIGHT)
in_field.pack(side=tk.TOP)
in_field.pack(ipady=10)
btn_fr=tk.Frame(test,width=i/1.34,height=272.5,bg='grey')
btn_fr.pack(pady=20)

cler=tk.Button(btn_fr,text='C',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:clr()).grid(row=0,column=0,padx=1,pady=1)
sq=tk.Button(btn_fr,text='^x',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('**')).grid(row=0,column=1,padx=1,pady=1)
po=tk.Button(btn_fr,text='<--',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:dele()).grid(row=0,column=2,padx=1,pady=1)
div=tk.Button(btn_fr,text='/',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('/')).grid(row=0,column=3,padx=1,pady=1)

sev=tk.Button(btn_fr,text='7',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(7)).grid(row=1,column=0,padx=1,pady=1)
eth=tk.Button(btn_fr,text='8',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(8)).grid(row=1,column=1,padx=1,pady=1)
nin=tk.Button(btn_fr,text='9',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(9)).grid(row=1,column=2,padx=1,pady=1)
mul=tk.Button(btn_fr,text='*',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('*')).grid(row=1,column=3,padx=1,pady=1)


fou=tk.Button(btn_fr,text='4',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(4)).grid(row=2,column=0,padx=1,pady=1)
fiv=tk.Button(btn_fr,text='5',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(5)).grid(row=2,column=1,padx=1,pady=1)
six=tk.Button(btn_fr,text='6',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(6)).grid(row=2,column=2,padx=1,pady=1)
sub=tk.Button(btn_fr,text='-',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('-')).grid(row=2,column=3,padx=1,pady=1)

one=tk.Button(btn_fr,text='1',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(1)).grid(row=3,column=0,padx=1,pady=1)
two=tk.Button(btn_fr,text='2',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(2)).grid(row=3,column=1,padx=1,pady=1)
the=tk.Button(btn_fr,text='3',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(3)).grid(row=3,column=2,padx=1,pady=1)
add=tk.Button(btn_fr,text='+',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('+')).grid(row=3,column=3,padx=1,pady=1)

zer=tk.Button(btn_fr,text='0',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click(0)).grid(row=4,column=0,padx=1,pady=1)
st=tk.Button(btn_fr,text='Square\nRoot',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('**0.5')).grid(row=4,column=1,padx=1,pady=1)
dec=tk.Button(btn_fr,text='.',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=lambda:click('.')).grid(row=4,column=2,padx=1,pady=1)
equ=tk.Button(btn_fr,text='=',image=bimg,compound=tk.CENTER,fg='yellow',font=('Algerian',22,'bold'),bd=0,cursor='hand2',command=eq).grid(row=4,column=3,padx=1,pady=1)
test.bind('<Return>',eq)
test.bind('c',clr)
test.bind('<BackSpace>',dele)
test.bind('/',lambda event : click('/'))
test.bind('*',lambda event : click('*'))
test.bind('-',lambda event : click('-'))
test.bind('+',lambda event : click('+'))
test.bind('^',lambda event : click('**'))
test.bind('x',lambda event : click('**0.5'))
test.bind('.',lambda event : click('.'))


# for kop in range(10):
#     test.bind(str(kop), lambda event: click(kop))

test.bind('0',lambda event : click(0))
test.bind('1',lambda event : click(1))
test.bind('2',lambda event : click(2))
test.bind('3',lambda event : click(3))
test.bind('4',lambda event : click(4))
test.bind('5',lambda event : click(5))
test.bind('6',lambda event : click(6))
test.bind('7',lambda event : click(7))
test.bind('8',lambda event : click(8))
test.bind('9',lambda event : click(9))
# test.bind('',lambda event : click(0))


test.mainloop()