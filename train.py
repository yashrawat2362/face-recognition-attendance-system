from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")

        #title
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=('Helvetica',30,'bold'),bg='RoyalBlue4',fg='cyan3')
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #image1
        img_top=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/train12.jpeg')
        img_top=img_top.resize((1500,790),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl1=Label(self.root,image=self.photoimg_top)
        f_lbl1.place(x=0,y=45,width=1500,height=790)


        #button
        b1_txt=Button(f_lbl1,text='Train Data',command=self.train_classifier,cursor='hand',font=('Helvetica',27,'bold'),fg='black',bg='black')
        b1_txt.place(x=630,y=370,width=200,height=45)



    #==============train============
    def train_classifier(self):
        data_dir=('Data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            if image == 'Data/.DS_Store':    #<<<<<<=================MOST DIFFICULT PROBLEM FOR ME===============>>>>>>>>>>
                continue
            img=Image.open(image).convert('L')  #gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow('Training',imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # =========== Train the classfier and save=========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Training Datasets completed!!')


            






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()