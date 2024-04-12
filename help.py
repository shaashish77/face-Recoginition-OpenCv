from tkinter import *
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # title
        title_lbl = Label(self.root, text="HELP DESK", font=("serif", 30, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Images top
        img_top = Image.open(r"college_images/help.jpg")
        img_top = img_top.resize((1530, 720), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=720)

        helpDesk = Label(first_label, text="Email:ASHISHSAH022.as@gmail.com", font=("sans serif", 13, "bold"),
                         bg="white", fg="blue")
        helpDesk.place(x=650, y=120)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
