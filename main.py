from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import subprocess,platform,os
from student import student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")

        #Image 1
        img=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/fc.jpeg')
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #image 2
        img1=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/fc2.jpeg')
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #image 3
        img2=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/fc3.jpeg')
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/bg.webp')
        img3=img3.resize((1500,660),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=660)

        #title
        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=('Helvetica',30,'bold'),bg='royalblue4',fg='cyan3')
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #student button
        img4=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/student.jpeg')
        img4=img4.resize((200,200),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand')
        b1.place(x=200,y=100,width=200,height=200)

        b1_txt=Button(bg_img,text='Student Details',command=self.student_details,cursor='hand',font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b1_txt.place(x=200,y=300,width=200,height=35)

        #detect_face button
        img5=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/detection.jpeg')
        img5=img5.resize((200,200),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor='hand',command=self.face_recog)
        b2.place(x=500,y=100,width=200,height=200)

        b2_txt=Button(bg_img,text='Face Detector',cursor='hand',command=self.face_recog,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b2_txt.place(x=500,y=300,width=200,height=35)

        #Attendance button
        img6=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/attendance.jpeg')
        img6=img6.resize((200,200),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor='hand',command=self.attend_details)
        b3.place(x=800,y=100,width=200,height=200)

        b3_txt=Button(bg_img,text='Attendance',cursor='hand',command=self.attend_details,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b3_txt.place(x=800,y=300,width=200,height=35)

        #help button
        img7=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/help.jpeg')
        img7=img7.resize((200,200),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor='hand')
        b4.place(x=1100,y=100,width=200,height=200)

        b4_txt=Button(bg_img,text='Help Desk',cursor='hand',font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b4_txt.place(x=1100,y=300,width=200,height=35)

        #train button
        img8=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/train.jpeg')
        img8=img8.resize((200,200),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor='hand',command=self.train_data)
        b5.place(x=200,y=380,width=200,height=200)

        b5_txt=Button(bg_img,text='Train Data',cursor='hand',command=self.train_data,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b5_txt.place(x=200,y=580,width=200,height=35)
        
        #photos button
        img9=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/photos.jpeg')
        img9=img9.resize((200,200),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor='hand',command=self.open_img)
        b6.place(x=500,y=380,width=200,height=200)

        b6_txt=Button(bg_img,text='Photos',cursor='hand',command=self.open_img,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b6_txt.place(x=500,y=580,width=200,height=35)

        #developer button
        img10=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/developer.jpeg')
        img10=img10.resize((200,200),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor='hand',command=self.dev_page)
        b7.place(x=800,y=380,width=200,height=200)

        b7_txt=Button(bg_img,text='Developers',cursor='hand',command=self.dev_page,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b7_txt.place(x=800,y=580,width=200,height=35)

        #exit button
        img11=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/exit.jpeg')
        img11=img11.resize((200,200),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor='hand',command=self.iExit)
        b8.place(x=1100,y=380,width=200,height=200)

        b8_txt=Button(bg_img,text='Exit',cursor='hand',command=self.iExit,font=('Helvetica',15,'bold'),bg='RoyalBlue4',fg='black')
        b8_txt.place(x=1100,y=580,width=200,height=35)

    def open_img(self):
        subprocess.run(['open', 'Data'], check=True)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno('Face Recognition','Are you sure exit this project',parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



    #==============FUNCTION BUTTON================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attend_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def dev_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)























if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()