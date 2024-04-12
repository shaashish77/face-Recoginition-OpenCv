from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # title
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("serif", 30, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Images top
        img_top = Image.open(r"college_images/facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=325)

        # button train data
        btn1_1 = Button(self.root, text="TRAIN DATA", command=self.trai_classifier, cursor="hand2",
                        font=("serif", 20, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=0, y=380, width=1530, height=60)

        # Images down
        img_bottom = Image.open(r"college_images/opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ADAPTIVE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        first_label = Label(self.root, image=self.photoimg_bottom)
        first_label.place(x=0, y=440, width=1530, height=325)

    def trai_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        #         train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
