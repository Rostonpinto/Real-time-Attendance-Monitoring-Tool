from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import MySQLdb
import cv2
import os
import numpy as np





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")


        title_lb1=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=50,width=1530,height=45)

                #BG_imaeg
        img = Image.open(r"C:\Users\Roston\OneDrive\Desktop\Face_R\images\st_bgimg.jpg")
        img = img.resize(( 1920 , 1080),Image.LANCZOS)
        self.pic_img = ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.pic_img)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        title_lb1=Label(bg_img,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="orange")
        title_lb1.place(x=0,y=50,width=1530,height=45)

        #button
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="black")
        b1_1.place(x=120,y=180,width=700,height=80)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        facess=[]
        ids=[]

        for image in path:
            imge=Image.open(image).convert('L')  #gray scale img
            imageNP=np.array(imge,'uint8')
            idd=int(os.path.split(image)[1].split('.')[1])

            facess.append(imageNP)
            ids.append(idd)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13

        ids=np.array(ids)  #numpy good performing  to convert array 


        #===========train the classifir=======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(facess,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set complected")

if __name__ == "__main__":
    root=Tk()
    obj =Train(root )
    root.mainloop()
