import tkinter
from time import strftime
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st image stanford
        img = Image.open(r"college_images"
                         r"\stanford.jpg")
        img = img.resize((500, 130), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=130)

        # face Rec image
        img1 = Image.open(r"college_images"
                          r"\faceAshish.jpg")
        img1 = img1.resize((500, 130), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=500, y=0, width=550, height=130)

        # college image
        img2 = Image.open(r"college_images"
                          r"\collegeFront.jpg")
        img2 = img2.resize((500, 130), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1000, y=0, width=560, height=130)

        # background image
        img3 = Image.open(r"college_images"
                          r"\bg_image.jpg")
        img3 = img3.resize((1536, 695), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1536, height=695)

        title_lbl = Label(bg_image, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("serif", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1536, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4 = Image.open(r"college_images"
                          r"\student.png")
        img4 = img4.resize((220, 220), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn1 = Button(bg_image, image=self.photoimg4, command=self.student_details, cursor="hand2")
        btn1.place(x=200, y=100, width=220, height=220)

        btn1_1 = Button(bg_image, text="Student Details", command=self.student_details, cursor="hand2",
                        font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=200, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"college_images"
                          r"\face-detector.jpg")
        img5 = img5.resize((220, 220), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_image, command=self.face_detector, image=self.photoimg5, cursor="hand2")
        btn1.place(x=500, y=100, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.face_detector, text="Face Detector", cursor="hand2",
                        font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=500, y=300, width=220, height=40)

        # attendance button
        img6 = Image.open(r"college_images"
                          r"\attendance.jpg")
        img6 = img6.resize((220, 220), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1 = Button(bg_image, command=self.attendance_data, image=self.photoimg6, cursor="hand2")
        btn1.place(x=800, y=100, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.attendance_data, text="Attendance", cursor="hand2",
                        font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        img7 = Image.open(r"college_images"
                          r"\help_desk.jpg")
        img7 = img7.resize((220, 220), Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn1 = Button(bg_image, command=self.help, image=self.photoimg7, cursor="hand2")
        btn1.place(x=1100, y=100, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.help, text="Help Desk", cursor="hand2", font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=1100, y=300, width=220, height=40)

        # Train Data button
        img8 = Image.open(r"college_images"
                          r"\train-data.jpg")
        img8 = img8.resize((220, 220), Image.ADAPTIVE)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn1 = Button(bg_image, command=self.train_data, image=self.photoimg8, cursor="hand2")
        btn1.place(x=200, y=380, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.train_data, text="Train Data", cursor="hand2",
                        font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=200, y=580, width=220, height=40)

        # Photos button
        img9 = Image.open(r"college_images"
                          r"\photos.jpg")
        img9 = img9.resize((220, 220), Image.ADAPTIVE)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn1 = Button(bg_image, image=self.photoimg9, command=self.open_img, cursor="hand2")
        btn1.place(x=500, y=380, width=220, height=220)

        btn1_1 = Button(bg_image, text="Photos", command=self.open_img, cursor="hand2", font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"college_images"
                           r"\developer.jpg")
        img10 = img10.resize((220, 220), Image.ADAPTIVE)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn1 = Button(bg_image, command=self.developer, image=self.photoimg10, cursor="hand2")
        btn1.place(x=800, y=380, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.developer, text="Developer", cursor="hand2", font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=800, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"college_images"
                           r"\exit.jpg")
        img11 = img11.resize((220, 220), Image.ADAPTIVE)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn1 = Button(bg_image, command=self.Iexit_btn, image=self.photoimg11, cursor="hand2")
        btn1.place(x=1100, y=380, width=220, height=220)

        btn1_1 = Button(bg_image, command=self.Iexit_btn, text="Exit", cursor="hand2", font=("serif", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=1100, y=580, width=220, height=40)

    def Iexit_btn(self):
        self.Iexit_btn = tkinter.messagebox.askyesno("Face Recognition", "Are You Sure?")
        if self.Iexit_btn > 0:
            self.root.destroy()
        else:
            return

    #     functions button *******************
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
