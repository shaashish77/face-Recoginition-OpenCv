from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # 1st image stanford
        img = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                         r"\smart-attendance.jpg")
        img = img.resize((800, 200), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=800, height=200)

        # face Rec image
        img1 = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                          r"\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((800, 200), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=800, y=0, width=800, height=200)

        # bg image
        img3 = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                          r"\bg_image.jpg")
        img3 = img3.resize((1536, 695), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=200, width=1536, height=695)

        title_lbl = Label(bg_image, text="ATTENDANCE MANAGEMENT SYSTEM", font=("serif", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1536, height=40)

        main_frame = Frame(bg_image, bd=2)
        main_frame.place(x=10, y=45, width=1530, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("sans serif", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\Ashis\OneDrive\Desktop\sdp_project\Face_Recoginization_system\college_images"
                              r"\student_details.jpg")
        img_left = img_left.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=730, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # labels and entry
        # attendance Id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("sans serif", 12, "bold"),
                                   bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20,
                                       font=("sans serif", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("sans serif", 12, "bold"),
                           bg="white")
        roll_label.grid(row=0, column=2, padx=4, pady=8)

        rollLabel_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=20,
                                    font=("sans serif", 12, "bold"))
        rollLabel_entry.grid(row=0, column=3, pady=8)

        # name
        name_label = Label(left_inside_frame, text="Name:", font=("sans serif", 12, "bold"),
                           bg="white")
        name_label.grid(row=1, column=0)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20,
                               font=("sans serif", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=8)

        # department
        dep_label = Label(left_inside_frame, text="Department:", font=("sans serif", 12, "bold"),
                          bg="white")
        dep_label.grid(row=1, column=2)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=20,
                              font=("sans serif", 12, "bold"))
        dep_entry.grid(row=1, column=3, pady=8)

        # time
        time_label = Label(left_inside_frame, text="Time:", font=("sans serif", 12, "bold"),
                           bg="white")
        time_label.grid(row=2, column=0)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=20,
                               font=("sans serif", 12, "bold"))
        time_entry.grid(row=2, column=1, pady=8)

        # date
        date_label = Label(left_inside_frame, text="Date:", font=("sans serif", 12, "bold"),
                           bg="white")
        date_label.grid(row=2, column=2)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=20,
                               font=("sans serif", 12, "bold"))
        date_entry.grid(row=2, column=3, pady=8)

        # attendance
        attendance_label = Label(left_inside_frame, textvariable=self.var_atten_attendance, text="Attendance Staus:",
                                 font=("sans serif", 12, "bold"),
                                 bg="white")
        attendance_label.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, font=("sans serif", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=270, width=715, height=35)

        save_btn = Button(btn_frame, command=self.importCsv, width=17, text="Import csv",
                          font=("sans serif", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.exportCsv, width=17, text="Export csv",
                            font=("sans serif", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, width=17, text="Update",
                            font=("sans serif", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data,width=17, text="Reset", font=("sans serif", 12, "bold"),
                           bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("sans serif", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=720, height=470)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.getCursor)

    # fetch data function************************
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import csv btn function
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All"
                                                                            "Files",
                                                                            "*.*")),
                                         parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv btn function
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found to Export", parent=self.root)
                return False

            fln = filedialog.asksaveasfile(initialdir=os.getcwd(), title="Save CSV",
                                           filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                           parent=self.root)

            if fln:
                with open(fln.name, 'w', newline="") as myfile:
                    expo_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        expo_write.writerow(i)

                messagebox.showinfo("Success", f"Data exported to {os.path.basename(fln.name)}")
            else:
                messagebox.showinfo("Cancelled", "Export cancelled by user")
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    def getCursor(self, event=" "):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # reset btn function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
