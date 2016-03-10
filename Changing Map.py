from tkinter import Tk, Label, Button

class MapSelection:
    def __init__(self, master):
        self.master = master
        master.title("Map Change")

        self.label = Label(master, text="Pick Your Map!")
        self.label.pack()

        self.map1_button = Button(master, text="Map 1", command=self.confirm)
        self.map1_button.pack()

        self.close_button = Button(master, text="Map 2", command=master.quit)
        self.close_button.pack()

        self.close_button = Button(master, text="Map 3", command=master.quit)
        self.close_button.pack()
        
    def confirm(self):
        print("Map Loaded")

root = Tk()
my_gui = MapSelection(root)
root.mainloop()
