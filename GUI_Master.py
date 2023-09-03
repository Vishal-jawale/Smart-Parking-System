from __future__ import division
import tkinter as tk
from PIL import Image , ImageTk
import csv
from datetime import date
import time
import cv2
from tkinter.filedialog import askopenfilename
import shutil
import matplotlib.pyplot as plt
import os, glob
import numpy as np
from moviepy.editor import VideoFileClip

cwd = os.getcwd()


#==============================================================================

#######
root = tk.Tk()
root.state('zoomed')

root.title("Car Parking Spot Detection")

current_path = str(os.path.dirname(os.path.realpath('__file__')))

basepath=current_path  + "\\" 

#==============================================================================
#==============================================================================

img = Image.open(basepath + "3.png")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

bg = img.resize((w,h),Image.ANTIALIAS)

bg_img = ImageTk.PhotoImage(bg)

bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=0)




heading = tk.Label(root,text="Car Parking Spot Detection System",width=25,font=("Times New Roman",45,'bold'),bg="#192841",fg="white")
heading.place(x=240,y=0)

#============================================================================================================


def car_park():
    from subprocess import call
    call(["python","Car_parking.py"])
    




def CLOSE():
    root.destroy()
#####==========================================================================================================
    




  



      

button5 = tk.Button(root,command = car_park, text="Car Parking Spot Detection", width=20,font=("Times new roman", 25, "bold"),bg="cyan",fg="black")
button5.place(x=100,y=150)

close = tk.Button(root,command = CLOSE, text="Exit", width=20,font=("Times new roman", 25, "bold"),bg="red",fg="white")
close.place(x=100,y=300)


root.mainloop()







