from tkinter import *
from PIL import ImageTk , Image
from tkinter import filedialog
import os

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="black")

label_img = Label(root , bg="white" , highlightthickness=5)
label_img.place(relx=0.5 , rely=0.5 , anchor=CENTER)

img_file = ""

def openImage():
    global name
    img_file = filedialog.askopenfilename(title=" Open Image File", filetypes=[( "Image Files" , " *.jpg *.png *.gif"  )])                            
    print(img_file)
    im = Image.open(img_file)
    img = ImageTk.PhotoImage(im)
    name = os.path.basename(img_file)
    formated_name = name.split('.')[0]
    root.title(formated_name)
    label_img["image"] = img
    img.close()
    

open_button=Button(root,text="OpenFile", command=openImage)
open_button.place(relx=0.5,rely=0.1,anchor=CENTER)

                  
root.mainloop()