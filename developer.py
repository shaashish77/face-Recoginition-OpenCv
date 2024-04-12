from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # title
        title_lbl = Label(self.root, text="DEVELOPER", font=("serif", 30, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Images top
        img_top = Image.open(r"college_images/dev.jpg")
        img_top = img_top.resize((1530, 720), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=720)

        main_frame = Frame(first_label, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open(r"college_images/ai-generated-8640895_1280.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ADAPTIVE)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        first_label = Label(main_frame, image=self.photoimg_top1)
        first_label.place(x=300, y=0, width=200, height=200)

        # developer Info
        developer = Label(main_frame, text="Hello From Ashish, Ritik, Ashwini", font=("sans serif", 13, "bold"),
                          bg="white", fg="blue")
        developer.place(x=0, y=5)

        developer = Label(main_frame, text="We are CSIT Undergrad", font=("sans serif", 13, "bold"),
                          bg="white", fg="blue")
        developer.place(x=0, y=40)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
