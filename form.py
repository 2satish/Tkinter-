from tkinter import *

root = Tk()

root.geometry("800x400")
root.title("Satish Das")

def getcmd():
	print(f"The username is '{uservar.get()}' and the password is '{passvar.get()}' and the person has accepted our requirement? {checkvar.get()}.")
	
	with open("records.text", "a") as f:
		f.write(f"The username is '{uservar.get()}' and the password is '{passvar.get()}' and has the person  accepted our requirement? {checkvar.get()}.\n")

Label(root, text="Please fill the process.").grid(row=0, column=3)

Label(root, text="User", pady=15).grid(row=1, column=2)
Label(root, text="Password ").grid(row=2, column=2)

uservar = StringVar() 
passvar = StringVar() 
checkvar = BooleanVar() 

Entry(root, textvariable=uservar).grid(row=1,column=3)
Entry(root, textvariable=passvar).grid(row=2, column=3)


Checkbutton(root, text = "Do you agree of our privacy and policy?",variable=checkvar).grid(row=3, column=3)

Button(root, text="Send", command=getcmd, ).grid(row=4, column=3, pady=15)



root.mainloop()