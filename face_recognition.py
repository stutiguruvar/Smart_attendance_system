from pyexpat import features
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
import cv2
import mysql.connector
from time import strftime
from datetime import datetime
class Face_recognition:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1590x900+0+0")
        self.root.title("Face recognizer")
        img = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\facerec.jpg")
        img = img.resize((1590,900))
        self.photo = ImageTk.PhotoImage(img)

        bgimg = Label(self.root,image = self.photo)
        bgimg.place(x=0,y=0,width = 1590,height = 900)

        title_label = Label(bgimg,text = "Face Recognizer",font=("times new roman",35,"bold"),bg = "black",fg = "skyblue")
        title_label.place(x = 0,y = 0,width=1590,height=100)

        b1_1 = Button(bgimg,text="Recognize face",command=self.face_recog,font=("times new roman",25,"bold"),bg = "white",fg = "black",cursor="hand2")
        b1_1.place(x = 958,y=785,width=430,height=90)

    
    # Attendance

    def mark_attendance(self,i,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            my_datalist=f.readlines()
            name_list=[]
            for line in my_datalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (i not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{i},{d},{dtstring},{d1},Present")



    
    # Face recognition

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select name from student where Regno="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Dep from student where Regno="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Regno from student where Regno="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                if confidence>77:
                    cv2.putText(img,f"Reg.No.:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Name:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    self.mark_attendance(i,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
                
                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome to face recognition',img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


        



if __name__=="__main__":
    root = Tk()
    obj  = Face_recognition(root)
    root.mainloop()