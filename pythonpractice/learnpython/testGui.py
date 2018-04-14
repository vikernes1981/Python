from tkinter import *
import tkinter.messagebox

def leftClicked(event):
	print("Left")
def middleClicked(event):
	print("Middle")
def rightClicked(event):
	print("Right")
def doNothing():
	print("Do nothing!!!")

class JoButtons: # creates 2 buttons , one to print something and one to exit app

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Click me!", command = self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = 	Button(frame, text="Quit!", command =frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("Print some random message")


root = Tk() # Always start with this

# ********* Menu **********

menu = Menu(root)

j = JoButtons(root) # instantiates the class

tkinter.messagebox.showinfo("Dummy Title", "People are strange") # creates a message box and then a question in a message box
answer = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")
if answer == "yes":
	print("8==D~ ")
frame = Frame(root, width="300", height="250") # creates a frame where you can click in it
frame.bind("<Button-1>", leftClicked)
frame.bind("<Button-2>", middleClicked)
frame.bind("<Button-3>", rightClicked)
frame.pack()

root.config(menu=menu) # creates a menu bar 
subMenu = Menu(menu) # creates the submenus (dropdown)
menu.add_cascade(label="File", menu=subMenu)# names of menus buttons
subMenu.add_command(label="New Project",command=doNothing) # name of submenu button
subMenu.add_command(label="New",command=doNothing)

subMenu.add_separator() # creates a separator

subMenu.add_command(label="Project",command=doNothing)
subMenu.add_command(label="Old",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu) # more menu buttons
editMenu.add_command(label="New Edit",command=doNothing) # and more submenu buttons
editMenu.add_command(label="Edit",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Edit Project",command=doNothing)
editMenu.add_command(label="Edit Old",command=doNothing)

# ******** ToolBar *********

toolbar = Frame(root, bg="blue") # creates the toolbar and sets the background
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


# ********** Status Bar ************


status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop() # Always end with this





'''
def leftClicked(event):
	print("Left")
def middleClicked(event):
	print("Middle")
def rightClicked(event):
	print("Right")

class JoButtons:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Click me!", command = self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = 	Button(frame, text="Quit!", command =frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("Print some random message")

button1 = Button(root, text="Click me")
button1.bind("<Button-1>",leftClicked)
button1.bind("<Button-2>", middleClicked)
button1.bind("<Button-3>", rightClicked)
button1.pack()
'''
'''
frame = Frame(root, width="300", height="250")
frame.bind("<Button-1>", leftClicked)
frame.bind("<Button-2>", middleClicked)
frame.bind("<Button-3>", rightClicked)
frame.pack()
#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)
'''
'''
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry1 = Entry(root)
entry2 = Entry(root)

label_1.grid(row=0, sticky=E)	
label_2.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root,text="Kepp me logged in")
c.grid(columnspan=2)
'''
'''
one  = Label(root, text="One", bg="black", fg="red")
one.pack()
two  = Label(root, text="One", bg="black", fg="green")
two.pack(fill=X)
three  = Label(root, text="One", bg="black", fg="blue")
three.pack(side=LEFT,fill=Y)

button1 = Button(topFrame, text=("Button 1"), fg="green")
button2 = Button(topFrame, text=("Button 2"), fg="red")
button3 = Button(topFrame, text=("Button 3"), fg="yellow")
button4 = Button(bottomFrame, text=("Button 4"), fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

'''


'''
MENU

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project",command=doNothing)
subMenu.add_command(label="New",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Project",command=doNothing)
subMenu.add_command(label="Old",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="New Edit",command=doNothing)
editMenu.add_command(label="Edit",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Edit Project",command=doNothing)
editMenu.add_command(label="Edit Old",command=doNothing)
'''