from tkinter import Tk, Label, Button

class MapSelection:
    def __init__(self, master):
        self.master = master
        master.title("Map Change")

        self.label = Label(master, text="Pick Your Map!")
        self.label.pack()

        self.map1_button = Button(master, text="Map 1", command=self.select_map_1)
        self.map1_button.pack()

        self.map2_button = Button(master, text="Map 2", command=self.select_map_2)
        self.map2_button.pack()

        self.map3_button = Button(master, text="Map 3", command=self.select_map_3)
        self.map3_button.pack()

        self.close_button = Button(master, text="Quit Game", command=root.quit)
        self.close_button.pack()
        
    def select_map_1(self):
        map_name = "shop1.png"
        root.quit
    def select_map_2(self):
        map_name = "shop2.png"

    def select_map_3(self):
        map_name = "shop3.png"

root = Tk()
my_gui = MapSelection(root)
root.mainloop()
