import random
import tkinter as tk
from tkinter import messagebox
from tkinter import Text
class Password():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("550x550")
        self.window.title("password maker")
        self.window.config(bg="black",cursor="mouse")
        self.window.resizable(False,False)
    def vals(self):
        self.numbers = [1,2,3,4,5,6,7,8,9,0]
        self.letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.specials = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","/",".",":",";"]
        self.password = tk.StringVar()
    def generate(self):
        txt = self.password.get()
        if len(txt)>=4:
            board = tk.Text(self.window,width=40,height=25,bg="black",fg="white",font=("Tahoma",12))
            board.grid(row=5,column=0)
            for i in range(1,15+1):
                hashpassword = random.choice(self.numbers)
                txt = txt.replace(txt[random.randint(0,len(txt)-1)],random.choice(self.specials))
                txt+="{}{}".format(random.choice(self.letters),hashpassword)
                board.insert(float(i)," ( {} )".format(txt))
        else:
            messagebox.showinfo("password maker","len of text lower of 4")
    def body(self): 
        tk.Label(self.window,text="please len of your text be higher of 4 thanks",bg="black",fg="white",font=("Tahoma",12)).grid(row=1,column=0)
        tk.Label(self.window,text="enter your txt here:",bg="black",fg="white",font=("Tahoma",12)).grid(row=2,column=0)
        tk.Entry(self.window,textvariable=self.password,bd=0,fg="black",bg="white",font=("Tahoma",14)).grid(row=3,column=0)
        tk.Button(self.window,text="Generate",bg="black",fg="white",font=("Tahoma",14),command=(self.generate)).grid(row=4,column=0)
    def main(self):
        self.vals()
        self.body()
        
        self.window.mainloop()