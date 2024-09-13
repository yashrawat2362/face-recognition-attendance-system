from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")

        #title
        title_lbl=Label(self.root,text="DEVELOPER",font=('Helvetica',30,'bold'),bg='RoyalBlue4',fg='cyan3')
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #image1
        img_top=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/dev11.jpeg')
        img_top=img_top.resize((1500,745),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=745)

        #main frame
        main_frame=Frame(f_lbl,bd=2,bg='white')
        main_frame.place(x=930,y=80,width=450,height=600)








if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()