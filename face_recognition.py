from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")

        #title
        title_lbl=Label(self.root,text="FACE RECOGNITIONS",font=('Helvetica',30,'bold'),bg='RoyalBlue4',fg='cyan3')
        title_lbl.place(x=0,y=0,width=1500,height=55)

        #image1
        img_top=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/face_recogbg.jpeg')
        img_top=img_top.resize((1500,750),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1500,height=750)

        # #image2
        # img_btm=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/developer.jpeg')
        # img_btm=img_btm.resize((950,750),Image.LANCZOS)
        # self.photoimg_btm=ImageTk.PhotoImage(img_btm)

        # f_lbl=Label(self.root,image=self.photoimg_btm)
        # f_lbl.place(x=650,y=55,width=850,height=750)

        #button
        b1_txt=Button(f_lbl,text='FACE RECOGNITION',cursor='hand',command=self.face_recog,font=('Helvetica',20,'bold'),fg='black',bg='black')
        b1_txt.place(x=725,y=340,width=270,height=45)

    # =======Attendance==========
    def mark_attendace(self,i,r,n,d):
        with open('yash.csv','r+',newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((','))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{i},{r},{n},{d},{dtString},{d1},Present')


    #=======face recognition======
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            try:
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                
                for (x,y,w,h) in features:
                    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    # print(id)
                    confidence=int((100*(1-predict/300)))
                    # print(confidence)

                    conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute('select Name from student where Student_ID='+str(id))
                    n=my_cursor.fetchone()
                    # print(n)
                    # n=str(n)
                    n='+'.join(n)

                    my_cursor.execute('select Roll from student where Student_ID='+str(id))
                    r=my_cursor.fetchone()
                    # r=str(r)
                    r='+'.join(r)

                    my_cursor.execute('select Dept from student where Student_ID='+str(id))
                    d=my_cursor.fetchone()
                    # d=str(d)
                    d='+'.join(d)

                    my_cursor.execute('select Student_Id from student where Student_ID='+str(id))
                    i=my_cursor.fetchone()
                    # i=str(i)
                    i='+'.join(i)

                    if confidence>77:
                        cv2.putText(img,f'ID:{i}',(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f'Roll:{r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f'Name:{n}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f'Department:{d}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        self.mark_attendace(i,r,n,d)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,'Unknown Face',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                    coord=[x,y,w,h]

                return coord
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)
        
        def recognize(img,faceCascade,clf):
            coord=draw_boundry(img,faceCascade, 1.1, 10, (255,255,255), 'Face',clf)
            return img
        

        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,faceCascade,clf)
            cv2.imshow('Welcome to Face Recognition',img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()