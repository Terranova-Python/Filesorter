import tkinter as tk
from tkinter import *

window = tk.Tk()

label_1=Label(window,width="20",height="6",bg='red')
label_2=Label(window,width="20",height="6",bg='green')
label_3=Label(window,width="20",height="6",bg='blue')

label_4=Label(window,width="20",height="6",bg='white')
label_5=Label(window,width="20",height="6",bg='black')
label_6=Label(window,width="20",height="6",bg='yellow')

label_7=Label(window,width="20",height="6",bg='red')
label_8=Label(window,width="20",height="6",bg='green')
label_9=Label(window,width="20",height="6",bg='blue')

label_10=Label(window,width="20",height="6",bg='white')
label_11=Label(window,width="20",height="6",bg='black')
label_12=Label(window,width="20",height="6",bg='yellow')

label_1.grid(row=0,column=0)
label_2.grid(row=0,column=1)
label_3.grid(row=0,column=2)

label_4.grid(row=1,column=0)
label_5.grid(row=1,column=1)
label_6.grid(row=1,column=2)

label_7.grid(row=2,column=0)
label_8.grid(row=2,column=1)
label_9.grid(row=2,column=2)

label_10.grid(row=3,column=0)
label_11.grid(row=3,column=1)
label_12.grid(row=3,column=2)

window.mainloop()
