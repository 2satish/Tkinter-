from tkinter import *
from tkinter.messagebox import showinfo


def submit():
	showinfo("Submitted", "Your Form Is Submitted! ")
	
	print(f"Aspirant name is {name.get()} ,  father's name is {fname.get()}, mother's name is {mname.get()}, age of the aspirant is {age.get()} and phone number is {ph.get()}.")
	
	
root = Tk() 
root.title("School Form")
root.geometry("744x564")

Label(root, text="PLEASE FILL THIS FORM", font="Lucida 10 bold", bg="red", fg="white",).grid(row= 1 , column = 2, pady=20, sticky="ew")

Label(root, text="NAME",font="Lucida 8 bold").grid(row=3 , column = 1,  pady=10, padx=10,sticky="w")

Label(root, text="FATHER'S NAME",font="Lucida 8 bold").grid(row= 4 , column = 1,  pady=10, padx=10, sticky="w")

Label(root, text="MOTHER'S NAME",font="Lucida 8 bold").grid(row= 5 , column = 1, pady=10, padx=10)

Label(root, text="ADDRESS",font="Lucida 8 bold").grid(row= 6 , column = 1, pady=10, padx=10, sticky="w")

Label(root, text="AGE",font="Lucida 8 bold").grid(row= 7 , column = 1, pady=10, padx=10, sticky="w")

Label(root, text="PH NO:",font="Lucida 8 bold").grid(row= 8 , column = 1, pady=10, padx=10, sticky="w")

name=StringVar() 
fname = StringVar() 
mname = StringVar() 
add = StringVar() 
age = StringVar() 
ph = StringVar() 


Entry(root, textvariable=name).grid(row=3, column=2, sticky ="w") 
Entry(root, textvariable=fname).grid(row=4, column=2, sticky="w") 
Entry(root, textvariable=mname).grid(row=5, column=2, sticky="w") 
Entry(root, textvariable=add).grid(row=6, column=2, sticky="w") 
Entry(root, textvariable=age).grid(row=7, column=2, sticky="w") 
Entry(root, textvariable=ph).grid(row=8, column=2, sticky="w") 

Button(root, text="Submit", command=submit).grid(row=9, column=2, sticky="w", pady=20)



root.mainloop () 