import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
# window
root = tk.Tk()
root.title("Image Resizer")
root.geometry('800x480+280+130')
# functions
def open_file():
    global filepath
    filepath = filedialog.askopenfilename()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image_path = filepath
    image = Image.open(image_path)
    image = image.resize((260, 260))
    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)
    # Create a label widget to display the image
    label = tk.Label(root, image=photo)
    label.image = photo  
    # Place the label on the window
    label.place(x=60,y=120)
def image_convert():
    global filepath
    img=cv2.imread(filepath,1)
    x=int(width.get())
    y=int(height.get())
    img = cv2.resize(img,(x,y))
    a= format.get()
    cv2.imwrite(a,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# labels
water_mark = tk.Label(root,text='Youtube | AK Deep Knowledge',font=("Arial",20,'bold'),fg='Green')
water_mark.pack()
water_mark = tk.Label(root,text='LIKE SHARE & SUBSCRIBE',font=("Arial",15,'bold'),fg='Green')
water_mark.pack()
width = tk.Label(root,text='😎 IMAGE RESIZER 😎',font=("Arial",20,'bold'),fg='Green')
width.pack()
width = tk.Label(root,text='Width (Pixels)',width=15,font=("Arial",12,'bold'))
width.place(x=380,y=120)
height = tk.Label(root,text='Height (Pixels)',width=15,font=("Arial",12,'bold'))
height.place(x=380,y=220)
format = tk.Label(root,text='Image Format',width=15,font=("Arial",12,'bold'))
format.place(x=380,y=320)
example = tk.Label(root,text='File_Name.(png,jpg,jpeg)',font=("Arial",9,'bold'),fg='red')
example.place(x=570,y=348)
# Entries
width = tk.Entry(root,width=15,font=("Arial",15,'bold'),fg='red')
width.place(x=570,y=120)
height = tk.Entry(root,width=15,font=("Arial",15,'bold'),fg='red')
height.place(x=570,y=220)
format = tk.Entry(root,width=15,font=("Arial",15,'bold'),fg='red')
format.place(x=570,y=320)
# buttons
upload = tk.Button(root, text="Upload File",width=12,font=("Arial",15,'bold'),bg='blue',fg='white',command=open_file)
upload.place(x=150,y=400)
export = tk.Button(root, text="Export",width=12,font=("Arial",15,'bold'),bg='Green',fg='white',command=image_convert)
export.place(x=320,y=400)
close = tk.Button(root, text="Close",width=12,font=("Arial",15,'bold'),bg='red',fg='white', command=root.destroy)
close.place(x=490,y=400)
root.mainloop()