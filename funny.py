# Python program to create
# yes/no message box

"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


def call():
	res = mb.askquestion('Exit Application',
						'Do you really want to exit')
	
	if res == 'yes' :
		root.destroy()
		
	else :
		mb.showinfo('Return', 'Returning to main application')

# Driver's code
root = tk.Tk()
canvas = tk.Canvas(root,
				width = 200,
				height = 200)

canvas.pack()
b = Button(root,
		text ='Quit Application',
		command = call)

canvas.create_window(100, 100,
					window = b)

root.mainloop()
"""
"""
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
button1 = tk.Button (root, text='Exit Application',command=ExitApplication,bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)
  
root.mainloop()
"""

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

mb = Tk()

mb.geometry('350x450+700+200')
mb.resizable(0,0)




def answer():
    mb.showerror("Answer", "Sorry, no answer available")

def callback():
    if mb.askyesno('Verify', 'are you an idiot?'):
        mb.showwarning('Yes', 'I knew it')
    else:
        mb.showwarning('No', callback())
#def ankit():






tk.Button(text='Quit', command=callback).pack(fill=tk.X)
tk.Button(text='Answer', command=answer).pack(fill=tk.X)

tk.mainloop()