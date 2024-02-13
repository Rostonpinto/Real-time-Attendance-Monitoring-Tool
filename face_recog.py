from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import MySQLdb
import cv2
import os
import numpy as np





class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        img = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\face_bgg.jpg")
        img = img.resize(( 1920 , 1080),Image.LANCZOS)
        self.pic_img = ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.pic_img)
        bg_img.place(x=0,y=0,width=1800,height=785)

        
        #image
        img1 = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\face_de.jpeg")
        img1 = img1.resize(( 500,550),Image.LANCZOS)
        self.pic_img1 = ImageTk.PhotoImage(img1)
        f_lb1=Label(bg_img,image=self.pic_img1)
        f_lb1.place(x=100,y=120,width=500,height=550)

        #button
        b1_1=Button(bg_img,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="black") #command=self.train_classifier
        b1_1.place(x=100,y=620,width=500,height=60)


    #=============face recognition==========

    def face_recog(self):
        def draw_doundary(img,classifier,scaleFactor,minNeg,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeg)


            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=MySQLdb.connect(host="localhost",
                                    user="root",
                                    password="roston@123",
                                    db="face_reg"
                                    )
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll_No from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dept from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence > 80:  #pridect 
                    cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]

            return coord
        
        
        def recoginz(img,clf,faceCascade):
            coord=draw_doundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Roston\OneDrive\Desktop\Face_R\classifier.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recoginz(img,clf,faceCascade)
            cv2.imshow("welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj =Face_recognition(root)
    root.mainloop()

