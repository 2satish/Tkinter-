from tkinter import *
from tkinter.messagebox import *

root = Tk() 

def register():
	nam = name.get() 
	ad = add.get() 
	fa = fat.get() 
	mo = mot.get() 
	ag = age.get() 
	phone = ph.get() 
	
	if nam == "":
		showerror("Error", "Please enter your name")
		
	elif ad == "":
		showerror("Error", "Please enter your address")
		
	elif fa == "":
		showerror("Error", "Please enter your father name. ")
		
	elif mo == "":
		showerror("Error", "Please enter your mother name")
		
	elif ag == "":
		showerror("Error", "Please enter your age")
		
	elif phone == "":
		showerror("Error", "Please enter your phone number. ")
		
	else:
		Label(root, text="Your Registration is completed.", fg="green", font=" Helvetica 8 bold").place(x=150, y=570)
	

#You can use the below code. 	
						
#	if nam == "":
#		Label(root, text="Please enter the name. ", fg="red").place(x=200, y=570)
#		
#	elif ad == "":
#		Label(root, text="Please enter the address.", fg="red").place(x=200, y=570)
#		
#	elif fa == "":
#		Label(root, text="Please enter the father name.", fg="red").place(x=200, y=570)
#		
#	elif mo == "":
#		Label(root, text="Please enter the mother name.", fg="red").place(x=200, y=570)
#		
#	elif ag == "":
#		Label(root, text="Please enter the age.", fg="red").place(x=200, y=570)
#		
#	elif phone == "":
#		Label(root, text="Please enter the phone no.", fg="red").place(x=200, y=570)
#		
#	else:
#		Label(root, text="Your Registration is completed.", fg="green", font=" Helvetica 8 bold").place(x=150, y=570)
#		
		

root.geometry("700x650")

Label(root, text="PLEASE FILL THE FORM", font="Helvetica 10 bold", bg="red", fg="white", pady=10).pack(fill=X) 

Label(root, text="NAME", font="Helvetica 7 bold").place(x=40, y=100) 

Label(root, text="ADDRESS", font="Helvetica 7 bold").place(x=40, y=160) 

Label(root, text="FATHER", font="Helvetica 7 bold").place(x=40, y=220) 

Label(root, text="MOTHER", font="Helvetica 7 bold").place(x=40, y=280) 

Label(root, text="AGE", font="Helvetica 7 bold").place(x=40, y=340) 

Label(root, text="PHONE NO. ", font="Helvetica 7 bold").place(x=40, y=400) 


name = StringVar() 
add = StringVar() 
fat  = StringVar() 
mot   = StringVar() 
age    = StringVar() 
ph     = StringVar() 
      
Entry(root, textvariable=name, bd=4).place(x = 220, y=100) 
Entry(root, textvariable=add, bd=4).place(x = 220, y=160) 
Entry(root, textvariable=fat, bd=4).place(x = 220, y=220) 
Entry(root, textvariable=mot, bd=4).place(x = 220, y=280) 
Entry(root, textvariable=age, bd=4).place(x = 220, y=340)    
Entry(root, textvariable=ph, bd=4).place(x = 220, y=400) 

Button(root, text="Register", command=register, bd=6).place(x=240, y=480)

root.mainloop() 