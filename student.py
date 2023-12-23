from msilib.schema import Font
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

from PIL import Image,ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1590x900+0+0")
        self.root.title("Student Details")

        # variables
        self.var_dep = StringVar()
        self.var_yr = StringVar()
        self.var_regno = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()




        img = Image.open(r"C:\Users\MI\Desktop\Face-recognition system\images\mainbg.jpg")
        img = img.resize((1590,900))
        self.photo = ImageTk.PhotoImage(img)

        bgimg = Label(self.root,image = self.photo)
        bgimg.place(x=0,y=0,width = 1590,height = 900)
        title_label = Label(bgimg,text = "Student Management System",font=("times new roman",35,"bold"),bg = "black",fg = "skyblue")
        title_label.place(x = 0,y = 0,width=1590,height=100)

        # Frame
        main_frame = Frame(bgimg,bd=2)
        main_frame.place(x=0,y=200,width=1590,height=700)

        # Left frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",20,"bold"),bg="black",fg="skyblue")
        left_frame.place(x=0,y=0,width=800,height=700)

        # current course frame
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times new roman",20,"bold"),bg="black",fg="skyblue")
        current_course_frame.place(x=0,y=0,width=798,height=150)

        # Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",20),bg="black",fg="skyblue")
        dep_label.grid(row=0,column=0,padx=10,pady=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",20),width=17,state="readonly")
        dep_combo["values"] = ("Select Department","Computer Science","ECE","Civil","Mechanical","IT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10)

        # Year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",20),bg="black",fg="skyblue")
        year_label.grid(row=1,column=0,padx=10,pady=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_yr,font=("times new roman",20),width=17,state="readonly")
        year_combo["values"] = ("Select year","First","Second","Third","Final")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10)

        # Class info frame
        student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",20),bg="black",fg="skyblue")
        student_frame.place(x=0,y=150,width=798,height=500)

        # Registration number
        reg_label = Label(student_frame,text="Registration No. :",font=("times new roman",20),bg="black",fg="skyblue")
        reg_label.grid(row=0,column=0,padx=10,pady=10)

        reg_entry = Entry(student_frame,textvariable=self.var_regno,width=20,font=("times new roman",20))
        reg_entry.grid(row=0,column=1,padx=10,pady=10)

        # Name
        name_label = Label(student_frame,text="Name : ",font=("times new roman",20),bg="black",fg="skyblue")
        name_label.grid(row=1,column=0,padx=10,pady=10)

        name_entry = Entry(student_frame,textvariable=self.var_name,width=20,font=("times new roman",20))
        name_entry.grid(row=1,column=1,padx=15,pady=15)

        # Gender
        gender_label = Label(student_frame,text="Gender :",font=("times new roman",20),bg="black",fg="skyblue")
        gender_label.grid(row=2,column=0,padx=10,pady=10)

        gender_entry = Entry(student_frame,textvariable=self.var_gender,width=20,font=("times new roman",20))
        gender_entry.grid(row=2,column=1,padx=10,pady=10)

               

        # Phone number
        phone_label = Label(student_frame,text="Phone number :",font=("times new roman",20),bg="black",fg="skyblue")
        phone_label.grid(row=3,column=0,padx=10,pady=10)

        phone_entry = Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",20))
        phone_entry.grid(row=3,column=1,padx=10,pady=10)

        # Email
        email_label = Label(student_frame,text="Email : ",font=("times new roman",20),bg="black",fg="skyblue")
        email_label.grid(row=4,column=0,padx=10,pady=10)

        email_entry = Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",20))
        email_entry.grid(row=4,column=1,padx=10,pady=10)

        # button frame
        btn_frame = LabelFrame(student_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=0,y=300,width=795,height=70)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",20),bg="skyblue",fg="black")
        save_btn.grid(row=0,column=0,padx=10,pady=10)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=10,font=("times new roman",20),bg="skyblue",fg="black")
        update_btn.grid(row=0,column=1,padx=10,pady=10)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",20),bg="skyblue",fg="black")
        delete_btn.grid(row=0,column=2,padx=10,pady=10)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",20),bg="skyblue",fg="black")
        reset_btn.grid(row=0,column=3,padx=10,pady=10)

        photo_btn_frame = LabelFrame(student_frame,bd=2,relief=RIDGE,bg="black")
        photo_btn_frame.place(x=0,y=375,width=795,height=70)

        take_photo_btn = Button(photo_btn_frame,command=self.generate_dataset,text="Take photo",width=25,font=("times new roman",20),bg="skyblue",fg="black")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(photo_btn_frame,text="Update photo",width=25,font=("times new roman",20),bg="skyblue",fg="black")
        update_photo_btn.grid(row=1,column=1)




        # Right frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",20,"bold"),bg="black",fg="skyblue")
        right_frame.place(x=800,y=0,width=800,height=700)

        # Search frame
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",20,"bold"),bg="black",fg="skyblue")
        search_frame.place(x=0,y=0,width=798,height=100)

        search_label = Label(search_frame,text="Search by :",font=("times new roman",20),bg="black",fg="skyblue")
        search_label.grid(row=0,column=0,padx=10,pady=10)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",20),width=17,state="readonly")
        search_combo["values"] = ("Select","Phone_no","Registration_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10)

        search_btn = Button(search_frame,text="Search",width=10,font=("times new roman",20),bg="skyblue",fg="black")
        search_btn.grid(row=0,column=2,padx=10,pady=10)

        showall_btn = Button(search_frame,text="Show all",width=10,font=("times new roman",20),bg="skyblue",fg="black")
        showall_btn.grid(row=0,column=3,padx=10,pady=10)

        # Table frame
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Student information",font=("times new roman",20),bg="black",fg="skyblue")
        table_frame.place(x=0,y=120,width=798,height=500)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=('Dep','yr','Regno.', 'name','gender','phone','email'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("yr",text="Year")
        self.student_table.heading("Regno.",text="Registration_number")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("email",text="Email")
        
        self.student_table["show"] = "headings"
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    # Function declarations

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phone.get()== "" or self.var_yr.get()=="Year" :
            messagebox.showerror("Error", "some fields are left to be filled")
        else: 
            conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_dep.get(),
                                                                                  self.var_yr.get(),
                                                                                  self.var_regno.get(),
                                                                                  self.var_name.get(),
                                                                                  self.var_gender.get(),
                                                                                  self.var_phone.get(),
                                                                                  self.var_email.get()

                                                                                  ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","student details has been added")
    
    # Fetching data

    def fetch_data(self):
        conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_yr.set(data[1])
        self.var_regno.set(data[2])
        self.var_name.set(data[3])
        self.var_gender.set(data[4])
        self.var_phone.set(data[5])
        self.var_email.set(data[6])

    # update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phone.get()== "" or self.var_yr.get()=="Year" :
            messagebox.showerror("Error", "some fields are left to be filled")
        else:
            try:
                updt = messagebox.askyesno("update","Do you want to update your data")
                if updt>0:
                    conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Year=%s,name=%s,gender=%s,phone=%s,email=%s where Regno =%s",(
                                                                                                                           self.var_dep.get(),
                                                                                                                           self.var_yr.get(),
                                                                                                                           self.var_name.get(),
                                                                                                                           self.var_gender.get(),
                                                                                                                           self.var_phone.get(),
                                                                                                                           self.var_email.get(),
                                                                                                                           self.var_regno.get()
                        ))
                else:
                    if not updt:
                        return
                messagebox.showinfo("Success","Student details updated")
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to {str(es)}")
    
    # delete function
    def delete_data(self):
        if self.var_regno.get() == "":
            messagebox.showerror("Error","User doesn't exist")
        else:
            try:
                delet = messagebox.askyesno("Delete","do you want to delete this data")
                if delet>0:
                    conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Regno=%s"
                    val=(self.var_regno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delet:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted successfully")
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to {str(es)}")

    # Reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_yr.set("Select Year")
        self.var_regno.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_email.set("")


    # generate data set
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_phone.get()== "" or self.var_yr.get()=="Year" :
            messagebox.showerror("Error", "some fields are left to be filled")
        else:
            try:
                conn=mysql.connector.connect(host = "localhost",username = "root",password = "E@glecrow8",database = "facerecognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Year=%s,name=%s,gender=%s,phone=%s,email=%s where Regno =%s",(
                                                                                                                           self.var_dep.get(),
                                                                                                                           self.var_yr.get(),
                                                                                                                           self.var_name.get(),
                                                                                                                           self.var_gender.get(),
                                                                                                                           self.var_phone.get(),
                                                                                                                           self.var_email.get(),
                                                                                                                           self.var_regno.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    clr = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    faces=face_classifier.detectMultiScale(clr,1.3,5)

                    for (x,y,w,h) in  faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(myframe),(450,450),cv2.INTER_AREA)
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,87,255),2)
                    cv2.imshow('Cropped face',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data set generated")




            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


                



        


        











if __name__=="__main__":
    root = Tk()
    obj  = Student(root)
    root.mainloop()