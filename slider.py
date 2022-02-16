from tkinter import *
 
import tkinter.messagebox as tmsg

def submit():

	tmsg.showinfo("Rate", f"Mr/Mrs {namevar.get()} has rated {foodvar.get()} {scale.get()}/10")
	
	with open("records.text", "a") as f:
		f.write(f"Mr/Mrs {namevar.get()} has rated {foodvar.get()} {scale.get()}/10\n")

root = Tk() 

root.geometry("644x444") 
root.title("Ratings")

Label(root, text="How much rate will you give? ").grid(row=0, column=3, pady=20)

Label(root, text="Name").grid(row=1, column=2)

Label(root, text="The food to rate").grid(row=2, column=2)

namevar=StringVar() 
foodvar=StringVar() 

Entry(root, textvariable=namevar).grid(row=1, column=3, pady=10)
Entry(root, textvariable=foodvar).grid(row=2, column=3)

scale = Scale(root, from_=0, to=10, orient=HORIZONTAL)
scale.grid(row=3, column=3) 

Button(root, text=" Submit", command=submit).grid(row=4, column=3, pady=20) 





root.mainloop() 