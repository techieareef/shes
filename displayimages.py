from tkinter import *
import os
from PIL import Image, ImageTk
root=Tk()
def display_images( root):
  filenames =['Pictures/MDR-100120.9089378292622078.jpg', 'Pictures/MDR-100120.13253401043434576.jpg','Pictures/MDR-100120.9089378292622078.jpg', 'Pictures/MDR-100120.13253401043434576.jpg','Pictures/MDR-100120.9089378292622078.jpg', 'Pictures/MDR-100120.13253401043434576.jpg']


  columns = 5
  image_count = 0
  window = Toplevel(root)
  window.wm_geometry("1200x600")
  canvas = Canvas(window, width = 2350, height = 600)
  canvas.grid(row=0, column=0, sticky= "news")
  #canvas.place(x=0, y=0)

  vsb = Scrollbar(window, orient="vertical", command=canvas.yview)
  vsb.grid(row=0, column=0, sticky="ns")
  canvas.configure(yscrollcommand= vsb.set)

  frame_image = Frame(canvas)
  frame_image.pack(expand=True, fill="both")
  #frame_image.grid_rowconfigure(0, weight = 1)
  #frame_image.grid_columnconfigure(0, weight = 1)
  canvas.create_window((0,0), window=frame_image, anchor="nw")

  for name in filenames:
    image_count += 1
    r, c = divmod(image_count - 1, columns)
    im = Image.open(name)
    resized = im.resize((200,200), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(resized)
    myvar = Label(frame_image, image = tkimage)
    myvar.image = tkimage
    myvar.grid(row=r, column = c)
    #print "here"
  # window.mainloop()
display_images(root)
mainloop()