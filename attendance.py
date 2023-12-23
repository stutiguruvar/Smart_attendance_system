
#   Python 2
import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from PIL import Image,ImageTk


    
    
    



# --- classes ---

class Attendance:

    def __init__(self, root):

        self.root = root
        
        self.root.geometry("1590x900+0+0")
        self.root.title("Smart Attendance System")
        img = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\mainbg.jpg")
        img = img.resize((1590,900))
        self.photo = ImageTk.PhotoImage(img)

        bgimg = Label(self.root,image = self.photo)
        bgimg.place(x=0,y=0,width = 1590,height = 900)

        self.filename = None
        self.df = None

        self.text = tk.Text(self.root)
        self.text.pack()

        

        self.button = tk.Button(self.root, text='DISPLAY DATA', command=self.display)
        self.button.pack()

    def load(self):

        name = ("attendance.csv")
        
        if name:
            if name.endswith('.csv'):
                self.df = pd.read_csv(name)
            else:
                self.df = pd.read_excel(name)

            self.filename = name

            # display directly
            #self.text.insert('end', str(self.df.head()) + '\n')

    def display(self):
        # ask for file if not loaded yet
        if self.df is None:
            self.load()

        # display if loaded
        
        if self.df is not None:
            self.text.insert('end', self.filename + '\n')
            self.text.insert('end', str(self.df.head()) + '\n')


# --- main ---

if __name__ == '__main__':
    root = tk.Tk()
    top = Attendance(root)
    root.mainloop()