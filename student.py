from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import MySQLdb





class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        #=========variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_address=StringVar()
        self.var_Faculty=StringVar()
        self.var_PhotoSample=StringVar()
       



        #BG_imaeg
        img = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\st_bgimg.jpg")
        img = img.resize(( 1920 , 1080),Image.LANCZOS)
        self.pic_img = ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.pic_img)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lb1.place(x=0,y=50,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=150,width=1500,height=610)

        #left lable frame
        left_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student details",font=("times new romaan",12,"bold"))
        left_frame.place(x=10,y=10,width=780,height=590)

        #image
        img1 = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\sch_attendance.jpg")
        img1 = img1.resize(( 550,120),Image.LANCZOS)
        self.pic_img1 = ImageTk.PhotoImage(img1)
        f_lb1=Label(left_frame,image=self.pic_img1)
        f_lb1.place(x=120,y=0,width=550,height=130)


        #curent course info
        current_course_frame=LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text="Current course info",font=("times new romaan",12,"bold"))
        current_course_frame.place(x=15,y=135,width=730,height=130)

        #depatment
        dep_lable=Label(current_course_frame,text="Departement",font=("times new romaan",12,"bold"),bg="white")
        #gride rows & culm 
        dep_lable.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new romaan",10,"bold"),state="readonly",width=20)
        dep_combo['values']=("Select Department","Computer Science & Engg" ,"Informataion Science & Engg", "Electronics & Communication Engg","Mechanical Engg","Electrical & Electronics Engg","Civil Engg","Aeronautical Engg")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        #course

        course_lable=Label(current_course_frame,text="Course",font=("times new romaan",12,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10)

        course_combo= ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new romaan",10,"bold"),state="readonly",width=20)
        course_combo['values']=("Select course","BE","Arch","MCA","BSC","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,pady=10,sticky=W)

        #year

        year_lable=Label(current_course_frame,text="Year",font=("times new romaan",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=20,sticky=W)

        year_combo= ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new romaan",10,"bold"),state="readonly",width=20)
        year_combo['values']=("Select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        sem_lable=Label(current_course_frame,text="Semester",font=("times new romaan",12,"bold"),bg="white")
        sem_lable.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo= ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new romaan",10,"bold"),state="readonly",width=20)
        sem_combo['values']=("Select sem","sem1","sem2","sem3","sem4","sem5","sem6")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)  #sticky 


        
        #class student  info frame
        class_studt_frame=LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text="Class student info",font=("times new romaan",12,"bold"))
        class_studt_frame.place(x=15,y=270,width=725,height=290)

        #student id
        
        Student_ID_lable=Label(class_studt_frame,text="Student ID",font=("times new romaan",12,"bold"),bg="white")
        Student_ID_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Student_ID_entry=ttk.Entry(class_studt_frame,textvariable=self.var_std_id,width=20,font=("times new romaan",12,"bold"))
        Student_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_lable=Label(class_studt_frame,text="Student Name",font=("times new romaan",12,"bold"),bg="white")
        studentname_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_studt_frame,textvariable=self.var_std_name,width=20,font=("times new romaan",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
       

        #class didvision
        class_div_lable=Label(class_studt_frame,text="Class Division",font=("times new romaan",12,"bold"),bg="white")
        class_div_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_combo= ttk.Combobox(class_studt_frame,textvariable=self.var_div,font=("times new romaan",10,"bold"),state="readonly",width=18)
        class_combo['values']=("Select division","A","B","C","D")
        class_combo.current(0)
        class_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)  

        # class_div_entry=ttk.Entry(class_studt_frame,textvariable=self.var_div,width=20,font=("times new romaan",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll No
        roll_no_lable=Label(class_studt_frame,text="Roll_No",font=("times new romaan",12,"bold"),bg="white")
        roll_no_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_studt_frame,textvariable=self.var_roll_no,width=20,font=("times new romaan",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #gender
        gender_lable=Label(class_studt_frame,text="Gender",font=("times new romaan",12,"bold"),bg="white")
        gender_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo= ttk.Combobox(class_studt_frame,textvariable=self.var_gender,font=("times new romaan",10,"bold"),state="readonly",width=18)
        gender_combo['values']=("Select gender","Female","Male")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)  

        # gender_entry=ttk.Entry(class_studt_frame,textvariable=self.var_gender,width=20,font=("times new romaan",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
        #dob
        dob_lable=Label(class_studt_frame,text="DOB",font=("times new romaan",12,"bold"),bg="white")
        dob_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_studt_frame,textvariable=self.var_dob,width=20,font=("times new romaan",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_lable=Label(class_studt_frame,text="Email",font=("times new romaan",12,"bold"),bg="white")
        email_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_studt_frame,textvariable=self.var_email,width=20,font=("times new romaan",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone No
        phone_lable=Label(class_studt_frame,text="Phone Number",font=("times new romaan",12,"bold"),bg="white")
        phone_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_studt_frame,textvariable=self.var_phone_no,width=20,font=("times new romaan",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_lable=Label(class_studt_frame,text="Address",font=("times new romaan",12,"bold"),bg="white")
        address_lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_studt_frame,textvariable=self.var_address,width=20,font=("times new romaan",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Faculty
        faculty_lable=Label(class_studt_frame,text="Faculty",font=("times new romaan",12,"bold"),bg="white")
        faculty_lable.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        faculty_entry=ttk.Entry(class_studt_frame,textvariable=self.var_Faculty,width=20,font=("times new romaan",12,"bold"))
        faculty_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio buttons
        self.var_radio1=StringVar()
        radiob1=ttk.Radiobutton(class_studt_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiob1.grid(row=5,column=0)


      
        radiob1=ttk.Radiobutton(class_studt_frame,variable=self.var_radio1,text="Don't take photo sample",value="No")
        radiob1.grid(row=5,column=1)

        #buttom frame 
        btn_frame=LabelFrame(class_studt_frame,bd=3,relief=RIDGE,cursor="hand2",bg="white")
        btn_frame.place(x=0,y=205,width=715,height=60)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5)

        take_photo_btn=Button(btn_frame,text="Take Pic",command=self.generate_dataset,width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4,padx=5)

        up_pic_btn=Button(btn_frame,text="Update pic",width="8",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        up_pic_btn.grid(row=0,column=5,padx=5)



        #Right lable frame
        right_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student details",font=("times new romaan",12,"bold"))
        right_frame.place(x=810,y=10,width=660,height=590)

        #image
        img2 = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\class_img.jpg")
        img2 = img2.resize(( 550,120),Image.LANCZOS)
        self.pic_img2 = ImageTk.PhotoImage(img2)

        f_lb2=Label(right_frame,image=self.pic_img2,bg="white")
        f_lb2.place(x=50,y=0,width=550,height=150)

        #============search System ===============
        search_frame=LabelFrame(right_frame,bd=3,bg="white",relief=RIDGE,text="Search system",font=("times new romaan",12,"bold"))
        search_frame.place(x=5,y=150,width=630,height=70)

        #lable
        search_lable=Label(search_frame,text="Search By",font=("times new romaan",12,"bold"),bg="green")
        search_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #combo
        search_combo= ttk.Combobox(search_frame,font=("times new romaan",12,"bold"),state="readonly",width="10")
        search_combo['values']=("Select","Name","USN","SEM")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  #sticky 

        #entry
        search_entry=ttk.Entry(search_frame,width=12,font=("times new romaan",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        #buttons
        search_btn=Button(search_frame,text="Search",width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showall_btn=Button(search_frame,text="Show All",width="10",font=("times new romaan",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=5)

        #table frame
        table_frame=Frame(right_frame,bd=3,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=250,width=630,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dept","course","year","sem","id","name","div","roll_no","gender","dob","email","address","phone_no","Faculty","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll_no",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone_no",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Faculty",text="Faculty")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("Dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Faculty",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)   #getcursor fun


        self.fetch_data()       #getdata

    #===============================function Declareation===========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:           
                conn=MySQLdb.connect(host="localhost",
                                    user="root",
                                    password="roston@123",
                                    db="face_reg"
                                    )
                my_cursor=conn.cursor()
                
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone_no.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_Faculty.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","student details has been added sucessufully",parent=self.root)        
            
            except Exception as es:
                messagebox.showerror(f"Due to :{str(es)}",parent=self.root)
    

    #======================fetch Data=====================
    def fetch_data(self):
        conn=MySQLdb.connect(host="localhost", user="root",password="roston@123",db="face_reg")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #=========get cursor==============     get data back to the fields
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone_no.set(data[11]),
        self.var_address.set(data[12]),
        self.var_Faculty.set(data[13]),
        self.var_radio1.set(data[14])


    #==========update function=========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                regen=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if regen>0:
                    # conn=MySQLdb.connect(host="localhost",user="root",password="roston@123",db="face_reg")
                    
                    conn=MySQLdb.connect(host="localhost",
                                    user="root",
                                    password="roston@123",
                                    db="face_reg"
                                    )
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,Dob=%s,Email=%s,phone_no=%s,Address=%s,Faculty=%s where student_id=%s",(
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll_no.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone_no.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_Faculty.get(),
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                                                                                                 ))
                else:
                    if not regen:
                        return
                messagebox.showinfo("Sucess","Student details sucessfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"DUE to:{str(es)}",parent=self.root)

    #function deleete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","do you want to delete the student",parent=self.root)
                if delete>0:
                    conn=MySQLdb.connect(host="localhost",user="root",password="roston@123",db="face_reg")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted students details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"DUE to:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_semester.set("Select")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll_no.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_Faculty.set("")
        self.var_radio1.set("")
    

    #=============genetrate data set or take photo sample=============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:                  
                conn=MySQLdb.connect(host="localhost",
                                user="root",
                                password="roston@123",
                                db="face_reg"
                                )
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for i in myresult:                      #self.var_PhotoSample=StringVar()
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,Dob=%s,Email=%s,phone_no=%s,Address=%s,Faculty=%s where student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll_no.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone_no.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_Faculty.get(),
                                                                                                                                                                                        
                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #========================= load perdidined data on face frontals from opencv
                face_classifer=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #for obj detection
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifer.detectMultiScale(gray,1.3,5)
                    #scalig factor=1.3
                    #minimum neg=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  #setting image id name by name and ging exte
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:   #hundred samples
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","generating data set complected!!!")
            except Exception as es:
                messagebox.showerror("Error", f"DUE to:{str(es)}",parent=self.root)





            

                    


            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                



                


        











if __name__ == "__main__":
    root=Tk()
    obj = student(root )
    root.mainloop()