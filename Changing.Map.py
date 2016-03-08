from tkinter import *

master = Tk()

var = StringVar(master)
var.set("Default Map") # initial value

option = OptionMenu(master, var, "Map 1", "Map 2", "Map 3")
option.pack()

#
# test stuff

def ok():
    master.quit()

button = Button(master, text="Select Map", command=ok)
button.pack()

root = Tk()

myButton = Button(root)
myImage = PhotoImage(file='map.png')
myButton.image = myImage
myButton.configure(image=myImage)

mainloop()





