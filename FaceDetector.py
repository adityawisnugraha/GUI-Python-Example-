from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox
import cv2

def aksikeluar():
    question = tkinter.messagebox.askquestion('Exit', 'Apakah anda yakin akan keluar?')
    if question == "yes":
        global root
        root.quit()

def fileDialog():
    panelA = None
    panelB = None
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select an Image", filetype = ((".jpg", "*.jpg"),(".jpeg","*.jpeg"),(".png","*.png")))
    if len(filename) > 0:
        img_asli = cv2.imread(filename)
        gambar = cv2.cvtColor(img_asli, cv2.COLOR_BGR2RGB)
        asli = Image.fromarray(gambar)
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray_img = cv2.cvtColor(img_asli, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
        jumlah = 0
        for x, y, w, h in faces:
            img = cv2.rectangle(img_asli, (x, y), (x + w, y + w), (0, 255, 0), 2)
            jumlah = jumlah + 1

        resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
        gambar_hasil = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        hasil = Image.fromarray(gambar_hasil)

        image = ImageTk.PhotoImage(asli)
        kotak = ImageTk.PhotoImage(hasil)
    else:
        img_asli = cv2.imread("error.jpg")
        gambar = cv2.cvtColor(img_asli, cv2.COLOR_BGR2RGB)
        asli = Image.fromarray(gambar)
        hasil = Image.fromarray(gambar)

        image = ImageTk.PhotoImage(asli)
        kotak = ImageTk.PhotoImage(hasil)
        jumlah = 0

    if panelA is None or panelB is None:
        label = Label(text="Banyak Wajah : " + str(jumlah))
        label.pack(side="bottom", fill="both", expand="yes", padx=0, pady=0)

        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left",padx=10,pady=10)

        panelB = Label(image=kotak)
        panelB.image = kotak
        panelB.pack(side="right",padx=10,pady=10)

root = Tk()
root.resizable(width=FALSE,height=FALSE)
root.title("Face Detector")

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Exit",command=aksikeluar)

#*** Toolbar ***
toolbar = Frame(root)
name=StringVar()

printButt = Button(toolbar,text="Insert Image",command=fileDialog)
printButt.pack(side="bottom",fill="both",expand="yes",padx="10",pady="10")

toolbar.pack(side=TOP,fill=X)

#*** Status Bar ***
status = Label(root,text="Aditya Wisnugraha Sugiyarto (16305141092)",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()