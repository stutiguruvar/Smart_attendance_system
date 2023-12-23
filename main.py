from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from attendance import Attendance
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
class attendance_system:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1590x900+0+0")
        self.root.title("Smart Attendance System")
        img = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\mainbg.jpg")
        img = img.resize((1590,900))
        self.photo = ImageTk.PhotoImage(img)

        bgimg = Label(self.root,image = self.photo)
        bgimg.place(x=0,y=0,width = 1590,height = 900)

        title_label = Label(bgimg,text = "Inteligente Asistencia",font=("times new roman",35,"bold"),bg = "black",fg = "skyblue")
        title_label.place(x = 0,y = 150,width=1590,height=100)

        # student details button
        studentimg = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\detailcard.png")
        studentimg = studentimg.resize((220,220))
        self.photostu = ImageTk.PhotoImage(studentimg)

        b1 = Button(bgimg,image=self.photostu,command = self.student_details,cursor="hand2")
        b1.place(x = 200,y=300,width=220,height=220)
        b1_1 = Button(bgimg,text="Student details",command = self.student_details,font=("times new roman",20,"bold"),bg = "white",fg = "black",cursor="hand2")
        b1_1.place(x = 200,y=300,width=220,height=50)

        # detect face button
        faceimg = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\traincard.jpg")
        faceimg = faceimg.resize((220,220))
        self.facephoto = ImageTk.PhotoImage(faceimg)
        b2 = Button(bgimg,image=self.facephoto,command=self.face_data,cursor="hand2")
        b2.place(x = 600,y=300,width=220,height=220)
        b2_2 = Button(bgimg,text="Face recogniser",command=self.face_data,font=("times new roman",20,"bold"),bg = "white",fg = "black",cursor="hand2")
        b2_2.place(x = 600,y=300,width=220,height=50)

        # Attendance button
        attenimg = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\attencard.jpg")
        attenimg = attenimg.resize((220,220))
        self.attenphoto = ImageTk.PhotoImage(attenimg)
        b3 = Button(bgimg,image=self.attenphoto,command=self.atten_data,cursor="hand2")
        b3.place(x = 1000,y=300,width=220,height=220)
        b3_3 = Button(bgimg,text="Student attendance",command=self.atten_data,font=("times new roman",18,"bold"),bg = "white",fg = "black",cursor="hand2")
        b3_3.place(x = 1000,y=300,width=220,height=50)

        # Train data button
        trainimg = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\facecard.png")
        trainimg = trainimg.resize((220,220))
        self.trainphoto = ImageTk.PhotoImage(trainimg)
        b4 = Button(bgimg,image=self.trainphoto,command=self.train_data,cursor="hand2")
        b4.place(x = 200,y=600,width=220,height=220)
        b4_4 = Button(bgimg,text="Train data",command=self.train_data,font=("times new roman",18,"bold"),bg = "white",fg = "black",cursor="hand2")
        b4_4.place(x = 200,y=600,width=220,height=50)

        # Photos
        phoimg = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\photocard.jpg")
        phoimg = phoimg.resize((220,220))
        self.phophoto = ImageTk.PhotoImage(phoimg)
        b5 = Button(bgimg,image=self.phophoto,cursor="hand2",command=self.open_img)
        b5.place(x = 600,y=600,width=220,height=220)
        b5_5 = Button(bgimg,text="All students' photos",command=self.open_img,font=("times new roman",15,"bold"),bg = "white",fg = "black",cursor="hand2")
        b5_5.place(x = 600,y=600,width=220,height=50)

    
    def open_img(self):
        os.startfile("data")

    # Function of buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
    
    def atten_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    



if __name__=="__main__":
    root = Tk()
    obj  = attendance_system(root)
    root.mainloop()