from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

#-------Variables-------#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

#----------------------First Image

        img=Image.open(r"college_images\deogiri-college-aurangabad-deogiri-college-003.jpg")
        img=img.resize((510,185),Image.ANTIALIAS)
        self.photo_img=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photo_img,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=185)

# ----------------------Second Image

        img2 = Image.open(r"college_images\IMG_20190904_120936.jpg")
        img2 = img2.resize((540, 185), Image.ANTIALIAS)
        self.photo_img2= ImageTk.PhotoImage(img2)

        self.btn_2 = Button(self.root, image=self.photo_img2, cursor="hand2")
        self.btn_2.place(x=540, y=0, width=540, height=185)

 # ----------------------Third Image-------#

        img3= Image.open(r"college_images\5th.jpg")
        img3= img3.resize((510, 185), Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img3)

        self.btn_3= Button(self.root, image=self.photo_img3, cursor="hand2")
        self.btn_3.place(x=1000, y=0, width=540, height=185)

#--------- Background Image ----------------#


        img4= Image.open(r"college_images\university.jpg")
        img4= img4.resize((1530, 720), Image.ANTIALIAS)
        self.photo_img4 = ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photo_img4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=180,width=1530,height=720)

        Lbl_title=Label(bg_lbl,text="Student Management System",font=("times new roman",30,"bold"),fg="blue",bg="white")
        Lbl_title.place(x=0,y=0,width=1530,height=40)

#---------Frame-------#

        manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=47,width=1500,height=560)

#----------------------------Left Frame----------#

        Left_frame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",13,"bold"),fg="green",bg="white")
        Left_frame.place(x=10,y=5,width=660,height=550)



        img5= Image.open(r"college_images\3rd.jpg")
        img5= img5.resize((650, 120), Image.ANTIALIAS)
        self.photo_img5 = ImageTk.PhotoImage(img5)

        my_img=Label(Left_frame,image=self.photo_img5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

 #-------Current Course LabelFrame Information -----#

        std_lbl_info_frame=LabelFrame(Left_frame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",13,"bold"),fg="green",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=115)

    #----Labels----#

        #-------Department

        lbl_dep=Label(std_lbl_info_frame,text="Departement : ",font=("arial",11,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",11,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Departement","Computer Scince","Information Technology","Chemistry","Commerce","Electronics","Science","Music","History","Economics")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #------Course

        cours_std=Label(std_lbl_info_frame,text="Courses : ",font=("arial",11,"bold"),bg="white")
        cours_std.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        combo_textcourse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("arial",11,"bold"),width=17,state="readonly")
        combo_textcourse_std["value"]=("Select Courses","BA","B.Com","B.SC","M.SC")
        combo_textcourse_std.current(0)
        combo_textcourse_std.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #-------Year

        current_year=Label(std_lbl_info_frame,text="Year : ",font=("arial",11,"bold"),bg="white")
        current_year.grid(row=1,column=0,padx=2,sticky=W)

        combo_txt_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("arial",11,"bold"),width=17,state="readonly")
        combo_txt_year["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025","2025-2026")
        combo_txt_year.current(0)
        combo_txt_year.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #------Semester

        label_semester=Label(std_lbl_info_frame,text="Semester : ",font=("arial",11,"bold"),bg="white")
        label_semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        combo_semester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester,font=("arial",11,"bold"),width=17,state="readonly")
        combo_semester["value"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6",)
        combo_semester.current(0)
        combo_semester.grid(row=1,column=3,padx=2,pady=10,sticky=W)

# -------Student Class LabelFrame Information -----#

        std_class_info_frame = LabelFrame(Left_frame, bd=4, relief=RIDGE, padx=2, text="Student Class Information",font=("times new roman", 12, "bold"), fg="green", bg="white")
        std_class_info_frame.place(x=0, y=240, width=650, height=240)

    # ----Labels----#

        # -------Student Id no

        lbl_id = Label(std_class_info_frame, text="StudentID : ", font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7,sticky=W)

        id_entry = ttk.Entry(std_class_info_frame,textvariable=self.var_std_id, font=("arial", 11, "bold"), width=22 )
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # ------Name

        lbl_Name = Label(std_class_info_frame, text="Student Name : ", font=("arial", 11, "bold"), bg="white")
        lbl_Name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name= ttk.Entry(std_class_info_frame, textvariable=self.var_std_name,font=("arial", 11, "bold"), width=22)
        txt_name.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # -------Division

        lbl_div = Label(std_class_info_frame, text="Class Division : ", font=("arial", 11, "bold"), bg="white")
        lbl_div.grid(row=1, column=0, padx=2,pady=7, sticky=W)

        combo_txt_div = ttk.Combobox(std_class_info_frame,textvariable=self.var_div, font=("arial", 11, "bold"), width=22, state="readonly")
        combo_txt_div["value"] = ("Select Division", "A","B","C","D")
        combo_txt_div.current(0)
        combo_txt_div.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # ------Roll No.

        lbl_roll = Label(std_class_info_frame, text="Roll No : ", font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        txt_roll= ttk.Entry(std_class_info_frame, textvariable=self.var_roll,font=("arial", 11, "bold"), width=22)
        txt_roll.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # -------Gender

        lbl_gender = Label(std_class_info_frame, text="Gender  : ", font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        combo_txt_gender = ttk.Combobox(std_class_info_frame, textvariable=self.var_gender,font=("arial", 11, "bold"), width=22, state="readonly")
        combo_txt_gender["value"] = ("Select Gender", "Male", "Female", "Other")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # ----------date of birth

        lbl_dob = Label(std_class_info_frame, text="DOB : ", font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        txt_dob = ttk.Entry(std_class_info_frame,textvariable=self.var_dob, font=("arial", 11, "bold"), width=22)
        txt_dob.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # ----------Email

        lbl_email = Label(std_class_info_frame, text="Email : ", font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        txt_email = ttk.Entry(std_class_info_frame,textvariable=self.var_email, font=("arial", 11, "bold"), width=22)
        txt_email.grid(row=3, column=1, padx=2, pady=10, sticky=W)


        # ----------Phone

        lbl_phone = Label(std_class_info_frame, text="Phone No. : ", font=("arial", 11, "bold"), bg="white")
        lbl_phone.grid(row=3, column=2, padx=2, pady=10, sticky=W)

        txt_phone = ttk.Entry(std_class_info_frame, textvariable=self.var_phone,font=("arial", 11, "bold"), width=22)
        txt_phone.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        # ----------Address

        lbl_address = Label(std_class_info_frame, text="Address : ", font=("arial", 11, "bold"), bg="white")
        lbl_address.grid(row=4, column=0, padx=2, pady=10, sticky=W)

        txt_address = ttk.Entry(std_class_info_frame,textvariable=self.var_address, font=("arial", 11, "bold"), width=22)
        txt_address.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        # ----------Teacher name

        lbl_teacher = Label(std_class_info_frame, text="Teacher Name : ", font=("arial", 11, "bold"), bg="white")
        lbl_teacher.grid(row=4, column=2, padx=2, pady=10, sticky=W)

        txt_teacher = ttk.Entry(std_class_info_frame,textvariable=self.var_teacher, font=("arial", 11, "bold"), width=22)
        txt_teacher.grid(row=4, column=3, padx=2, pady=10, sticky=W)

#-----------------------------------Button Frame---------------#

        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=485, width=640, height=38)

        #------Add save button
        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)


        #------Update  button
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)


        #------Delete button
        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)


        #------Reset  button
        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)




#----------------------------Right Frame----------#

        Right_frame=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Details",font=("times new roman",13,"bold"),fg="red",bg="white")
        Right_frame.place(x=680,y=10,width=800,height=540)

    # img1
        img6= Image.open(r"college_images\VKD3152-1024x683.jpg")
        img6= img6.resize((780, 200), Image.ANTIALIAS)
        self.photo_img6 = ImageTk.PhotoImage(img6)

        my_img=Label(Right_frame,image=self.photo_img6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)

    #-----Search system---------#

        Search_frame=LabelFrame(Right_frame,bd=4,relief=RIDGE,padx=2,text="View Student Details & Search System",font=("times new roman",13,"bold"),fg="black",bg="white")
        Search_frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(Search_frame,font=("arial",11,"bold"),text="Search By :",fg="white",bg="red")
        search_by.grid(row=0,column=0,padx=2,pady=2)

        #-----search

        self.var_combo_search=StringVar()

        com_txt_search=ttk.Combobox(Search_frame,textvariable=self.var_combo_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Roll","Phone","student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()

        txt_search=ttk.Entry(Search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(Search_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_showAll=Button(Search_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_showAll.grid(row=0,column=4,padx=5)

        #-----------Student table scroll bar---------#

        table_frame=Frame(Right_frame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#------- Add data

    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()=="" or self.var_gender.get()==""):
            messagebox.showerror("Error","All Field required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="nik358",database="company")
                my_curser=conn.cursor()
                my_curser.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                          self.var_dep.get(),
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
                                                                                                          self.var_teacher.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Studetn has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#-----Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="nik358", database="company")
        my_curser = conn.cursor()
        my_curser.execute("select * from student")
        data=my_curser.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#----Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])


#-----Update-----#

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()=="" or self.var_gender.get()==""):
            messagebox.showerror("Error","All Field required")
        else:
            try:
                update=messagebox.askyesno("Update","are you sure update this student data",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="nik358", database="company")
                    my_curser = conn.cursor()
                    my_curser.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                                                                                                                                                          self.var_dep.get(),
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
                                                                                                                                                                                                          self.var_std_id.get()
                                                                                                                                                                                                         ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student succesfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#------- Delete--------#
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feild required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delte this student",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="nik358", database="company")
                    my_curser = conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_curser.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#--------Reset---------#

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

#------Search data

    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="nik358", database="company")
                my_curser = conn.cursor()
                my_curser.execute("select * from student where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_curser.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







if __name__=="__main__":
    root=Tk()
    obg=Student(root)
    root.mainloop()
