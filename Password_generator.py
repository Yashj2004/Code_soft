import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import random
import string
import pyautogui

t = tk.Tk()
t.title("Password generator")
t.resizable(width=False, height=False)
t.configure(height=112, width=300)

def generar_func():
    tam = tam_variable.get()
    caja_contra.delete('1.0', tk.END)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    chars = lower + upper + num + symbols
    temp = random.sample(chars, tam)
    lol = "".join(temp)
    
    caja_contra.insert(tk.END, lol)
   
    t.clipboard_clear() 
    t.clipboard_append(lol)
    
    pyautogui.alert(text="Generated password copied to clipboard.", title="Password generator")

tam_entry = ttk.Entry(t)
tam_variable = tk.IntVar()
tam_entry.configure(justify="center",textvariable=tam_variable)
tam_entry.place(anchor="nw", relx=0.32, rely=0.12, x=0, y=0)

generar_button = ttk.Button(t)
generar_button.configure(text='Gen password')
generar_button.place(anchor="nw", relx=0.40, rely=0.37, x=0, y=0)
generar_button.configure(command=generar_func)

caja_contra = ScrolledText(t)
caja_contra.place(anchor="nw",relheight=0.23,relwidth=0.68,relx=0.24,rely=0.68,x=0,y=0)

t.mainloop()
