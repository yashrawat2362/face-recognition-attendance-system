from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os,csv
from tkinter import filedialog

mydata =[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System By Yash Rawat")

        # =========>>>>>VARIABLES<<<=========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #Image 1
        img=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/attend1.jpeg')
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #image 2
        img1=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/attend2.jpeg')
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #image 3
        img2=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/attend3.jpeg')
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        #title
        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=('Helvetica',30,'bold'),bg='RoyalBlue4',fg='cyan3')
        title_lbl.place(x=0,y=130,width=1500,height=50)

        #main frame
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=180,width=1500,height=610)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Attendance Information',font=('Helvetica',16,'italic'))
        Left_frame.place(x=10,y=5,width=660,height=580)

        #left img
        img_left=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/attend_left.jpeg')
        img_left=img_left.resize((650,130),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=130)

        # left_inside_frame
        left_inside_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,font=('Helvetica',15,'bold'))
        left_inside_frame.place(x=10,y=140,width=640,height=400)

        #Attendance id
        attendanceID_label=Label(left_inside_frame,text='Attendance ID:',font=('Helvetica',14,'bold'))
        attendanceID_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_id,font=('Helvetica',14,'bold'))
        attendanceID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Roll no
        Roll_no_label=Label(left_inside_frame,text='Roll No:',font=('Helvetica',14,'bold'))
        Roll_no_label.grid(row=0,column=2,padx=10,sticky=W)

        Roll_no_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=('Helvetica',14,'bold'))
        Roll_no_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text='Name:',font=('Helvetica',14,'bold'))
        name_label.grid(row=1,column=0,padx=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_name,font=('Helvetica',14,'bold'))
        name_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #department
        dept_label=Label(left_inside_frame,text='Department:',font=('Helvetica',14,'bold'))
        dept_label.grid(row=1,column=2,padx=10,sticky=W)

        dept_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=('Helvetica',14,'bold'))
        dept_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #time
        time_label=Label(left_inside_frame,text='Time:',font=('Helvetica',14,'bold'))
        time_label.grid(row=2,column=0,padx=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_time,font=('Helvetica',14,'bold'))
        time_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text='Date:',font=('Helvetica',14,'bold'))
        date_label.grid(row=2,column=2,padx=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=('Helvetica',14,'bold'))
        date_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #Attendance status
        attendance_status_label=Label(left_inside_frame,text='Attendance Status:',font=('Helvetica',14,'bold'))
        attendance_status_label.grid(row=3,column=0,padx=10,sticky=W)

        attend_status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=('Helvetica',13,'bold'),width=17,state='readonly')
        attend_status_combo['values']=('Status','Present','Absent')
        attend_status_combo.current(0)
        attend_status_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=270,width=611,height=35)

        import_csv_btn=Button(btn_frame,text='Import CSV',command=self.importCsv,width=14,font=('Helvetica',14,'bold'))
        import_csv_btn.grid(row=0,column=0,ipadx=2,ipady=2)

        export_csv_btn=Button(btn_frame,text='Export CSV',command=self.exportCsv,width=14,font=('Helvetica',14,'bold'))
        export_csv_btn.grid(row=0,column=1,ipadx=2,ipady=2)

        update_btn=Button(btn_frame,text='Update',width=14,font=('Helvetica',14,'bold'))
        update_btn.grid(row=0,column=2,ipadx=2,ipady=2)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=14,font=('Helvetica',14,'bold'))
        reset_btn.grid(row=0,column=3,ipadx=2,ipady=2)

        #=======>>>>>right label frame<<<<=========
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Attendance Details',font=('Helvetica',16,'italic'))
        Right_frame.place(x=690,y=5,width=720,height=580)

        # img_right=Image.open('/Users/yashrawat/Desktop/Face_Recognition_System/images/stud_details.jpeg')
        # img_right=img_right.resize((700,130),)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(Right_frame,image=self.photoimg_right)
        # f_lbl.place(x=10,y=0,width=700,height=130)

        # =======TABLE FRAME===========
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=10,width=700,height=540)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text='Attendance ID')
        self.AttendanceReportTable.heading('roll',text='Roll No')
        self.AttendanceReportTable.heading('name',text='Name')
        self.AttendanceReportTable.heading('department',text='Department')
        self.AttendanceReportTable.heading('time',text='Time')
        self.AttendanceReportTable.heading('date',text='Date')
        self.AttendanceReportTable.heading('attendance',text='Attendance')
        self.AttendanceReportTable["show"]='headings'

        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('roll',width=100)
        self.AttendanceReportTable.column('name',width=100)
        self.AttendanceReportTable.column('department',width=100)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column('attendance',width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.get_cursor)

    # =========>>>>Fetch Data<<<==========
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)



    # ======>>>>import CSV<<<<<=========
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=self.root)
        # fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=('CSV File','*.csv'),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)



    # ======>>>>export CSV<<<<<=========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('No Data','No Data Found',parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=self.root)
            with open(fln,mode='w',newline='') as myfile:
                exp_write=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo('Data Export','Your Data exported to '+os.path.basename(fln)+' successfully')
        except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)


    #=============get cursor===============
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #===========reset function===========
    def reset_data(self):
        self.var_atten_id.set('')
        self.var_atten_roll.set('')
        self.var_atten_name.set('')
        self.var_atten_dep.set('')
        self.var_atten_time.set('')
        self.var_atten_date.set('')
        self.var_atten_attendance.set('Status')



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()