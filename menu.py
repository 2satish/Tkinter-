from tkinter import * 
import tkinter.messagebox as tmsg

root = Tk() 

root.geometry("444x444")
root.title("Notepad")
def cmd():
	root.destroy() 
	
def info():
	tmsg.showinfo("Information", "This GUI is made by Satish Das")
	

text = Text(root)
text.pack(fill = Y) 

main = Menu(root) 

m1 = Menu(main) 

m1.add_command(label="Exit", command=cmd) 

root.config(menu=main) 
main.add_cascade(label="File", menu=m1)

m2 = Menu(main) 

root.config(menu=main) 




m2.add_command(label="About",  command=info) 
main.add_cascade(label="About", menu=m2) 




root.mainloop() 