
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))






Height = tk.IntVar()
Weight = tk.IntVar()

def main():
    h = Height.get()
    w = Weight.get()
    
    # while True:
    #     try:
    #         # Taking user input
    #         Height = h
    
    #         Weight = w
            
    #     except ValueError:
    #         # Validation error.
    #         print("Please provide valid input.")
    #         continue  # Return to the start of the loop.
       # else:
    if h <= 0 or w <= 0:
                print("Your input must not be zero or less.")
          # continue
    else:
                # Calculate BMI
                BMIIndex = round(w / (h * h) * 703, 2)
    
                # Print the output
                print("Your Body Mass Index is: ", BMIIndex)
                # l9 = tk.Label(root, text="h :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
                # l9.place(x=130, y=500)
    
    if BMIIndex < 18.5:
                    print("Oops! You are underweight")
                    l9 = tk.Label(root, text="Oops! You are underweight", width=50, font=("Times new roman", 15, "bold"), bg="#CD0000",fg="white")
                    l9.place(x=200, y=500)
                    
                     
                
    elif BMIIndex <= 24.9:
                    print("Awesome! You are healthy.")
                    l9 = tk.Label(root, text="Awesome! You are healthy", width=50, font=("Times new roman", 15, "bold"), bg="#CD0000",fg="white")
                    l9.place(x=200, y=500)
    elif BMIIndex <= 29.9:
                    print("Eee! You are overweight")
                    l9 = tk.Label(root, text="Eee! You are overweight", width=50, font=("Times new roman", 15, "bold"), bg="#CD0000	",fg="white")
                    l9.place(x=200, y=500)
    else:
                    print("Seesh! You are obese")
                    l9 = tk.Label(root, text="Seesh! You are obese ", width=50, font=("Times new roman", 15, "bold"), bg="#CD0000",fg="white")
                    l9.place(x=200, y=500)
                


# def reg():
    
# ##### tkinter window ######
    
#     print("Submit")
#     from subprocess import call
#     call(["python", "registration.py"])   



# def login():
    
# ##### tkinter window ######
    
#     print("log")
#     from subprocess import call
#     call(["python", "login.py"])   






#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 =Image.open('m1.jpg')
# image2 =image2.resize((w,h), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

image2 = Image.open('img.jpg')
image2 = image2.resize((1500, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Virtual health care assistant with BMI calculator", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=40,bg="#8B0A50",fg="white")
lbl.place(x=0, y=3)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=450, y=300)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
lbl = tk.Label(root, text="Please enter your height in inches:", font=('times', 20,' bold '), height=1, width=30,fg="black")
lbl.place(x=100, y=200)

t9 = tk.Entry(root, textvar=Height, width=20, font=('', 15))
t9.place(x=700, y=200)



         
lbl = tk.Label(root, text="Please enter your weight in pound:", font=('times', 20,' bold '), height=1, width=30,bg="green",fg="white")
lbl.place(x=100, y=300)


t9 = tk.Entry(root, textvar=Weight, width=20, font=('', 15))
t9.place(x=700, y=300)

btn = tk.Button(root, text="submit", bg="#192841",font=("",20),fg="white", width=9, height=0, command = main)
btn.place(x=500, y=400)


root.mainloop()