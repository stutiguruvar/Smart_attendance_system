from cProfile import label
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from winsound import MessageBeep
from PIL import Image,ImageTk
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1590x900+0+0")
        self.root.title("Training data set")
        img = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\traindata.png")
        img = img.resize((1590,900))
        self.photo = ImageTk.PhotoImage(img)

        bgimg = Label(self.root,image = self.photo)
        bgimg.place(x=0,y=0,width = 1590,height = 900)

        title_label = Label(bgimg,text = "Training data set",font=("times new roman",35,"bold"),bg = "black",fg = "skyblue")
        title_label.place(x = 0,y = 0,width=1590,height=100)

        b1_1 = Button(bgimg,text="Train data",command=self.train_classifier,font=("times new roman",25,"bold"),bg = "white",fg = "black",cursor="hand2")
        b1_1.place(x = 1000,y=400,width=240,height=80)

    
    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces =[]
        ids=[]
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8') 
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result",'Training data sets completed')




if __name__=="__main__":
    root = Tk()
    obj  = Train(root)
    root.mainloop()



