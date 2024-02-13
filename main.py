from tkinter import*
from PIL import Image,ImageTk
from student import student
import os
from train import Train
from face_recog import Face_recognition

 


class Face_reg:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        #BG_imaeg
        img = Image.open(r"images\bgimage.jpg")
        img = img.resize(( 1920 , 1080),Image.LANCZOS)
        self.pic_img = ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.pic_img)
        bg_img.place(x=0,y=0,width=1920,height=1080)


        #studemt button
        img1 = Image.open(r"images\studentlogo.png")
        img1 = img1.resize(( 220,220),Image.LANCZOS)
        self.pic_img1 = ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.pic_img1,command=self.student_details,cursor="hand2")       #command=self.student_details to link to the next website
        b1.place(x=150,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=150,y=400,width=220,height=40)

        #Detect Face button
        img2 = Image.open(r"images\facedetect.png")
        img2 = img2.resize(( 220,220),Image.LANCZOS)
        self.pic_img2 = ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.pic_img2,cursor="hand2",command=self.face_data)
        b2.place(x=450,y=200,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b2_2.place(x=450,y=400,width=220,height=40)
        
        #attendance button
        img3 = Image.open(r"images\face_attendance.png")
        img3 = img3.resize(( 220,220),Image.LANCZOS)
        self.pic_img3 = ImageTk.PhotoImage(img3)

        b3=Button(bg_img,image=self.pic_img3,cursor="hand2")
        b3.place(x=750,y=200,width=220,height=220)

        b3_3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b3_3.place(x=750,y=400,width=220,height=40)

        #help button
        img4 = Image.open(r"C:images\help.jpg")
        img4 = img4.resize(( 220,220),Image.LANCZOS)
        self.pic_img4 = ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.pic_img4,cursor="hand2")
        b4.place(x=1050,y=200,width=220,height=220)

        b4_4=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b4_4.place(x=1050,y=400,width=220,height=40)

        #Train face 
        img5 = Image.open(r"images\face_train.jpg") #(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\face_train.jpg")
        img5 = img5.resize(( 220,220),Image.LANCZOS)
        self.pic_img5 = ImageTk.PhotoImage(img5)

        b5=Button(bg_img,image=self.pic_img5,command=self.train_data,cursor="hand2")
        b5.place(x=150,y=450,width=220,height=220)

        b5_5=Button(bg_img,text="Face Train",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b5_5.place(x=150,y=650,width=220,height=40)

        #photos face butoon
        img6 = Image.open(r"images\face_photos.png")
        img6 = img6.resize(( 220,220),Image.LANCZOS)
        self.pic_img6 = ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.pic_img6,cursor="hand2",command=self.open_img)
        b6.place(x=450,y=450,width=220,height=220)

        b6_6=Button(bg_img,text="Face photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b6_6.place(x=450,y=650,width=220,height=40)

        #devloper details 
        img7 = Image.open(r"images\dev.png")
        img7 = img7.resize(( 220,220),Image.LANCZOS)
        self.pic_img7 = ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.pic_img7,cursor="hand2")
        b7.place(x=750,y=450,width=220,height=220)

        b7_7=Button(bg_img,text="Developer Details",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b7_7.place(x=750,y=650,width=220,height=40)

        #exit button
        img8= Image.open(r"images\exit.jpg")
        img8 = img8.resize(( 220,220),Image.LANCZOS)
        self.pic_img8 = ImageTk.PhotoImage(img8)

        b8=Button(bg_img,image=self.pic_img8,cursor="hand2")
        b8.place(x=1050,y=450,width=220,height=220)

        b8_8=Button(bg_img,text="EXit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b8_8.place(x=1050,y=650,width=220,height=40)

        #facee functiom
    def open_img(self):
        os.startfile("data")




         #=============== student function buttons==============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student( self.new_window)


    # train fun
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train( self.new_window)

    #facee data

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition( self.new_window)
    


       



if __name__ == "__main__":
    root=Tk()
    obj = Face_reg(root)
    root.mainloop()

