#activity 1
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Personal Data')

L1 = Label(my_app, text = 'Personal Data' , font = ('Arial' , 24))
L1.grid(row=0 , column=0)


L2 = Label(my_app, text = 'Name')
L2.grid(row=1 , column=0)
str2 = StringVar(value='Luckyta Afia Susanto')
E2 = Label (my_app, textvariable=str2)
E2.grid(row=1 , column=1)

L3 = Label(my_app , text = 'NIM')
L3.grid(row=2 , column=0)
str3 = StringVar(value='L200183103')
E3 = Label(my_app, textvariable=str3)
E3.grid(row=2 , column=1)

L4 = Label(my_app, text = 'Favourite Book')
L4.grid(row=3 , column=0)
str4 = StringVar(value='Sci-fi')
E4 = Label(my_app, textvariable=str4)
E4.grid(row=3, column=1)

L5 = Label(my_app , text = 'Favorite Companions of the Prophet ')
L5.grid(row=4 , column=0)
str5 = StringVar(value='Umar bin Khattab')
E5 = Label(my_app, textvariable=str5)
E5.grid(row=4 , column=1)

L6 = Label(my_app , text = 'Motto')
L6.grid(row=5 , column=0)
str6 = StringVar(value='Never stop learning')
E6 = Label(my_app, textvariable=str6)
E6.grid(row=5 , column=1)


def close():
    my_app.destroy()

B = Button(my_app.quit(), text = 'close' , command = close )
B.grid(row=6 , column=1)

my_app.mainloop()
