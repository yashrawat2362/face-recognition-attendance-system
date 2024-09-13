from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")


        # ========variables===============
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
    
        #Image 1
        img=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/stud1.jpeg')
        img=img.resize((1500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        # #image 2
        # img1=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/st2.jpeg')
        # img1=img1.resize((500,130),Image.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=130)

        # #image 3
        # img2=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/st3.jpeg')
        # img2=img2.resize((500,130),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=500,height=130)

        #title
        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=('Helvetica',30,'bold'),bg='RoyalBlue4',fg='cyan3')
        title_lbl.place(x=0,y=130,width=1500,height=45)

        #main frame
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=175,width=1500,height=615)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Information',font=('Helvetica',16,'bold'))
        Left_frame.place(x=10,y=5,width=660,height=580)

        #==========>current course<==============
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text='Current Course Info',font=('Helvetica',15,'bold'))
        current_course_frame.place(x=20,y=10,width=600,height=130)

        #department
        dept_label=Label(current_course_frame,text='Department',font=('Helvetica',14,'bold'))
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=('Helvetica',13),width=17,state='readonly')
        dept_combo['values']=('Select Department','CSE','ECE','ME','Civil','IT')
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text='Course',font=('Helvetica',14,'bold'))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('Helvetica',13),width=17,state='readonly')
        course_combo['values']=('Select Course','Btech','BCA','MCA')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text='Year',font=('Helvetica',14,'bold'))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('Helvetica',13),width=17,state='readonly')
        year_combo['values']=('Select Year','2020-21','2021-22','2022-23','2023-24','2024-25')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_label=Label(current_course_frame,text='Semester',font=('Helvetica',14,'bold'))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('Helvetica',13),width=17,state='readonly')
        sem_combo['values']=('Select Semester','1st','2nd','3rd','4th','5th','6th','7th','8th')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #=====>>>class student Information<<<<========
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text='Class Student Info',font=('Helvetica',15,'bold'))
        class_student_frame.place(x=20,y=150,width=600,height=400)

        #studentID
        studentID_label=Label(class_student_frame,text='Student ID:',font=('Helvetica',14,'bold'))
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=('Helvetica',14))
        studentID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #student Name
        student_name_label=Label(class_student_frame,text='Student Name:',font=('Helvetica',14,'bold'))
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=('Helvetica',14))
        student_name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Class Division
        class_div_label=Label(class_student_frame,text='Class Division:',font=('Helvetica',14,'bold'))
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('Helvetica',13),width=17,state='readonly')
        division_combo['values']=('Select Divsion','A','B','C','D')
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Roll No
        roll_no_label=Label(class_student_frame,text='Roll No:',font=('Helvetica',14,'bold'))
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=('Helvetica',14))
        roll_no_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text='Gender:',font=('Helvetica',14,'bold'))
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('Helvetica',13),width=17,state='readonly')
        gender_combo['values']=('Select Gender','Male','Female','Transgender')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #DOB
        dob_label=Label(class_student_frame,text='DOB:',font=('Helvetica',14,'bold'))
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=('Helvetica',14))
        dob_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #Email
        email_label=Label(class_student_frame,text='Email:',font=('Helvetica',14,'bold'))
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=('Helvetica',14))
        email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #phone no.
        phone_label=Label(class_student_frame,text='Phone No:',font=('Helvetica',14,'bold'))
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=('Helvetica',14))
        phone_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        #address
        add_label=Label(class_student_frame,text='Address:',font=('Helvetica',14,'bold'))
        add_label.grid(row=4,column=0,padx=10,sticky=W)

        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=('Helvetica',14))
        add_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text='Teacher Name:',font=('Helvetica',14,'bold'))
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=('Helvetica',14))
        teacher_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='Take Photo Sample',value='Yes')
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='No Photo Sample',value='No')
        radiobtn2.grid(row=6,column=1)

        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=20,y=270,width=550,height=35)

        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=12,font=('Helvetica',14,'bold'))
        save_btn.grid(row=0,column=0,ipadx=2,ipady=2)

        update_btn=Button(btn_frame,text='Update',command=self.update_data,width=12,font=('Helvetica',14,'bold'))
        update_btn.grid(row=0,column=1,ipadx=2,ipady=2)

        delete_btn=Button(btn_frame,text='Delete',command=self.delete_data,width=12,font=('Helvetica',14,'bold'))
        delete_btn.grid(row=0,column=2,ipadx=2,ipady=2)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=12,font=('Helvetica',14,'bold'))
        reset_btn.grid(row=0,column=3,ipadx=2,ipady=2)

        # button1 frame
        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn1_frame.place(x=120,y=320,width=373,height=35)

        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text='Take Photo Sample',width=18,font=('Helvetica',14,'bold'))
        take_photo_btn.grid(row=0,column=0,ipadx=2,ipady=2)

        update_photo_btn=Button(btn1_frame,text='Update Photo Sample',width=18,font=('Helvetica',14,'bold'))
        update_photo_btn.grid(row=0,column=1,ipadx=2,ipady=2)




        #====>>>right label frame<<<======
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Details',font=('Helvetica'))
        Right_frame.place(x=690,y=5,width=720,height=580)

        img_right=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/college_images/studz_ryt.jpeg')
        img_right=img_right.resize((700,130),)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=700,height=130)

        # =====================SEARCH SYSTEM==================

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text='Search System',font=('Helvetica',14,'italic'))
        search_frame.place(x=10,y=140,width=700,height=70)

        search_label=Label(search_frame,text='Search By:',font=('Helvetica',14,'bold'))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=('Helvetica',13),width=17,state='readonly')
        search_combo['values']=('Select','Roll_No','Phone_No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=13,font=('Helvetica',14))
        search_entry.grid(row=0,column=2,padx=4,pady=10,sticky=W)

        search_btn=Button(search_frame,text='Search',width=13,font=('Helvetica',14,'bold'))
        search_btn.grid(row=0,column=3,padx=4)

        show_all_btn=Button(search_frame,text='Show All',width=13,font=('Helvetica',14,'bold'))
        show_all_btn.grid(row=0,column=4,padx=4)

        # =======TABLE FRAME===========
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=220,width=700,height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=('dept','course','year','sem','id','name','div','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dept',text='Department')
        self.student_table.heading('course',text='Course')
        self.student_table.heading('year',text='Year')
        self.student_table.heading('sem',text='Semester')
        self.student_table.heading('id',text='ID')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('div',text='Division')
        self.student_table.heading('roll',text='Roll')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('phone',text='Phone')
        self.student_table.heading('address',text='Address')
        self.student_table.heading('teacher',text='Teacher')
        self.student_table.heading('photo',text='PhotoSampleStatus')
        self.student_table["show"]='headings'

        self.student_table.column('dept',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('div',width=100)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('address',width=100)
        self.student_table.column('teacher',width=100)
        self.student_table.column('photo',width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()

    # ===========Function declaration============
    def add_data(self):
        if self.var_dept.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error",'All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()

                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)

    #=============fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from student')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()
            

    #=============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ======update function======
    def update_data(self):
        if self.var_dept.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error",'All fields are required',parent=self.root)
        else:
            try:
                Update=messagebox.askyesno('Update','Do you want to update this student details',parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s',(
                                                                                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo('success','Student details successfully update completed',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root) 

    #=========delete function==========
    def delete_data(self):
        if self.var_std_id.get()=='':
            messagebox.showerror('Error','Student ID must be required',parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno('Student Delete Page','Do you want to delete this student',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql='delete from student where Student_ID=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                messagebox.showinfo('Delete','Successfully deleted student details',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)

    #===========reset function===========
    def reset_data(self):
        self.var_dept.set('Select Department')
        self.var_course.set('Select Course')
        self.var_year.set('Select Year')
        self.var_semester.set('Select Semester')
        self.var_std_id.set('')
        self.var_std_name.set('')
        self.var_div.set('Select Division')
        self.var_roll.set('')
        self.var_gender.set('Select Gender')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_teacher.set('')
        self.var_radio1.set('')

    #============generate dataset or take photo sample===========
    def generate_dataset(self):
        if self.var_dept.get()=='Select Department' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error",'All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',passwd='S19k2dfb',database='face_recognizer',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from student')
                myresult=my_cursor.fetchall()
                id=0
                for i in myresult:
                    id+=1
                my_cursor.execute('update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s',(
                                                                                                                                                                                                                        self.var_dept.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()==id
                                                                                                                                                                                                                        ))
                print(id)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ==============Load predefined data on face frontals from opencv============
                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path='Data/user.'+str(id)+'.'+str(img_id)+'.jpg'   #...<<>>>....
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Croped Face',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Generating data sets compled!!!')
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()