from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # variables ***************
        self.var_program = StringVar()
        self.var_dep = StringVar()
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

        # 1st image stanford
        img = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                         r"\student.png")
        img = img.resize((500, 130), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=5, y=0, width=500, height=130)

        # face Rec image
        img1 = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                          r"\classroom.jpg")
        img1 = img1.resize((500, 130), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=500, y=0, width=550, height=130)

        # college image
        img2 = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                          r"\college-friends.jpg")
        img2 = img2.resize((500, 130), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1000, y=0, width=560, height=130)

        # background image
        img3 = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                          r"\bg_image.jpg")
        img3 = img3.resize((1536, 695), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1536, height=695)

        title_lbl = Label(bg_image, text="STUDENT MANAGEMENT SYSTEM", font=("serif", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1536, height=40)

        main_frame = Frame(bg_image, bd=2)
        main_frame.place(x=10, y=45, width=1500, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Details",
                                font=("sans serif", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        # left panel image
        img_left = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                              r"\student_details.jpg")
        img_left = img_left.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=15, y=0, width=730, height=130)

        # current course
        current_course_frame = LabelFrame(Left_frame, bg="white", bd=2, relief=RIDGE, text="Current Course Information",
                                          font=("sans serif", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=115)

        # program
        program_label = Label(current_course_frame, text="Program", font=("sans serif", 12, "bold"), bg="white")
        program_label.grid(row=0, column=0, padx=10)

        program_combo = ttk.Combobox(current_course_frame, textvariable=self.var_program, state="readonly", width=17,
                                     font=("sans serif", 12, "bold"))
        program_combo["values"] = ("Select Program", "B.TECH", "M.TECH")
        program_combo.current(0)
        program_combo.grid(row=0, column=1, padx=2, pady=10)

        # department
        department_label = Label(current_course_frame, text="Department", font=("sans serif", 12, "bold"), bg="white")
        department_label.grid(row=0, column=2, padx=10, sticky=W)

        department_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, state="readonly", width=17,
                                        font=("sans serif", 12, "bold"))
        department_combo["values"] = ("Select Department", "CSIT", "CSE", "CVL", "ME", "ECE", "EEE")
        department_combo.current(0)
        department_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=("sans serif", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=0, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, state="readonly", width=17,
                                      font=("sans serif", 12, "bold"))
        semester_combo["values"] = ("Select Semester", 1, 2, 3, 4, 5, 6, 7, 8)
        semester_combo.current(0)
        semester_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=("sans serif", 12, "bold"), bg="white")
        year_label.grid(row=1, column=2, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, state="readonly", width=17,
                                  font=("sans serif", 12, "bold"))
        year_combo["values"] = ("Select Year", "2020-24", "2021-25", "2022-26", "2023-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student details
        class_Student_frame = LabelFrame(Left_frame, bg="white", bd=2, relief=RIDGE, text="Class Student Information",
                                         font=("sans serif", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        # student Id
        studentId_label = Label(class_Student_frame, text="Student ID:", font=("sans serif", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20,
                                    font=("sans serif", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("sans serif", 12, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=20,
                                      font=("sans serif", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class SEC
        class_div_label = Label(class_Student_frame, text="Class Section:", font=("sans serif", 12, "bold"),
                                bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, state="readonly", width=17,
                                 font=("sans serif", 12, "bold"))
        div_combo["values"] = ("A", "B", "C", "D", "E", "F")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll no
        roll_no_label = Label(class_Student_frame, text="Roll NO:", font=("sans serif", 12, "bold"),
                              bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20,
                                  font=("sans serif", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("sans serif", 12, "bold"),
                             bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, state="readonly", width=17,
                                    font=("sans serif", 12, "bold"))
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("sans serif", 12, "bold"),
                          bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("sans serif", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email
        email_label = Label(class_Student_frame, text="Email:", font=("sans serif", 12, "bold"),
                            bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20,
                                font=("sans serif", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone no
        phone_label = Label(class_Student_frame, text="Phone No:", font=("sans serif", 12, "bold"),
                            bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20,
                                font=("sans serif", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # addresses
        address_label = Label(class_Student_frame, text="Address:", font=("sans serif", 12, "bold"),
                              bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20,
                                  font=("sans serif", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("sans serif", 12, "bold"),
                              bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20,
                                  font=("sans serif", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample",
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, width=17, command=self.add_data, text="Save", font=("sans serif", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, width=17, command=self.update_data, text="Update",
                            font=("sans serif", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, command=self.delete_data, width=17, text="Delete",
                            font=("sans serif", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data, width=17, text="Reset", font=("sans serif", 12, "bold"),
                           bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, width=35, text="Take Photo Sample",
                                font=("sans serif", 12, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, width=35, text="Update Photo Sample", font=("sans serif", 12, "bold"),
                                  bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Details",
                                 font=("sans serif", 12, "bold"))
        Right_frame.place(x=780, y=10, width=700, height=580)

        img_right = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                               r"\books-1281581_1280.jpg ")
        img_right = img_right.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_label = Label(Right_frame, image=self.photoimg_right)
        first_label.place(x=5, y=0, width=720, height=130)

        #     search system
        search_frame = LabelFrame(Right_frame, bg="white", bd=2, relief=RIDGE, text="Search System",
                                  font=("sans serif", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("sans serif", 15, "bold"),
                             bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, state="readonly", width=15, font=("sans serif", 12, "bold"))
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=18, font=("sans serif", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        #         buttons for right field
        search_btn = Button(search_frame, width=13, text="Search", font=("sans serif", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, width=13, text="Show All", font=("sans serif", 10, "bold"), bg="blue",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame

        table_frame = Frame(Right_frame, bg="white", bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=(
                                              "dep", "program", "year", "sem", "id", "name", "div", "roll", "gender",
                                              "dob", "email", "phone", "address", "teacher",
                                              "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("program", text="Program")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("program", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #     functions declarations ***************
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="W7301@jqir#",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                                  "%s)", (
                                      self.var_dep.get(), self.var_program.get(), self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student detail has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # fetch data from database into the student table
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="username", password="passwordyours"
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # function get cursor
    def get_cursor(self, event=" "):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_program.set(data[1]),
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

    #   update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update the student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="W7301@jqir#",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep= %s, Program= %s, Year= %s, semester= %s, "
                                      "Name= %s, Division = %s, Roll = %s, Gender= %s,"
                                      "DOB= %s, Email= %s, Phone= %s, Address = %s, Teacher =%s, PhotoSample= %s "
                                      "where Student_id = %s", (
                                          self.var_dep.get(), self.var_program.get(), self.var_year.get(),
                                          self.var_semester.get(),
                                          self.var_std_name.get(), self.var_div.get(),
                                          self.var_roll.get(),
                                          self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                                          self.var_phone.get(),
                                          self.var_address.get(), self.var_teacher.get(),
                                          self.var_radio1.get(),
                                          self.var_std_id.get()
                                      ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #  delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id is Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Info", "Do you really want to delete the information?",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="W7301@jqir#",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id= %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "successfully deleted student data", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #     reset function
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_program.set("select Program")
        self.var_year.set("select Year")
        self.var_semester.set("select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Generate dataset and take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="W7301@jqir#",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute("update student set Dep= %s, Program= %s, Year= %s, semester= %s, "
                                  "Name= %s, Division = %s, Roll = %s, Gender= %s,"
                                  "DOB= %s, Email= %s, Phone= %s, Address = %s, Teacher =%s, PhotoSample= %s "
                                  "where Student_id = %s", (
                                      self.var_dep.get(), self.var_program.get(), self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_std_name.get(), self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(), self.var_teacher.get(),
                                      self.var_radio1.get(),
                                      self.var_std_id.get() == id + 1
                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # Load predefined data on face frontal from openCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed !!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
