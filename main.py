import tkinter as tk
import sys
from PIL import Image, ImageTk
import winsound
from time import *
from random import randint
from threading import Thread

############################# Global functions

def openImage(filename): # opens all type of images for further use
    image = Image.open(filename)
    tkImage = ImageTk.PhotoImage(image)
    return tkImage

def sound():    
    winsound.PlaySound("button.wav", winsound.SND_ALIAS)

def getText(textFile): # opens text file, reads info from it and then closes it
        try:
            f = open(textFile, "r")
            text = f.read()
            return text
        
        finally:
            f.close()

def combine_funcs(*funcs): # combines multiple functions given for further use when passed as command
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def binarySearch(selectedGameList, gameID):  #binary search that takes a list and an object and returns true if that object is in the list, and otherwise - false
            if len(selectedGameList) != 0:   
                mid = len(selectedGameList)//2
                if selectedGameList[mid]==gameID:
                    return True
                elif gameID < selectedGameList[mid]:
                    return binarySearch(selectedGameList[:mid], gameID) # recursion until object is found or none is left 
                else:
                    return binarySearch(selectedGameList[mid+1:], gameID)
            else:
                return False
            
#############################   Global variables:
            
global sec
sec = 1  
global selectedGameList
selectedGameList = []
global imageDict, labelDict
imageDict = {}
labelDict = {}
global playerStartPos
playerStartPos = ()

############################
class Game():
    '''class for defining a game'''
    def __init__(self, ID, name, category, price, rating,imageName, labelName, x, y):
        self.ID = ID
        self.name = name
        self.categ = category
        self.price = price
        self.rating = rating
        self.imageName = imageName
        self.labelName = labelName
        self.X = x
        self.Y = y

        global imageDict, labelDict
        imageDict[ID] = self.imageName  #puts game id as a key and game image as a value into a dict
        labelDict[ID] = self.labelName  #puts game id as a key and game label used for shopping list into a dict        

    def setCoord(self, x, y): # idk if used
        
        self.X = x
        self.Y = y
########################################################################################################

class GameShop(tk.Tk):
    '''GUI class for creating the game window and swiching between frames'''
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args,**kwargs)
        tk.Tk.iconbitmap(self, default = "icon.ico")
        container = tk.Frame(self)
        self.title("Game Shop")
        
        container.pack(side = "top", fill = "both", expand = True)

        self.frames = {} #all game frames
        for F in (StartPage, InfoPage, SelectionPage, GamePage): #if new frame is created add it here
            
            frame = F(container, self)
            
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()


##############################################################################################################################################
class StartPage(tk.Frame):
    '''GUI class that sets all widgets in the startpage '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #setting the background 
        self.menuBackGround = openImage('menuPage.png')
        self.menuIcon = openImage ('ps4.png')
        canvas1 = tk.Canvas(self, width = 1024, height = 768, bg = "white")
        canvas1.create_image(1024/2,768/2,image = self.menuBackGround)
        canvas1.pack()
        #creating game title on screen
        canvas1.create_text(512, 150, fill = 'grey6', font = ("fixedsys", 52, 'bold'), text = 'Welcome to the\nGame Shop',justify = 'center' )

        #creating start button that will open selection page
        button1 = tk.Button(canvas1, text = "START GAME", font = ("fixedsys",18), command = lambda: combine_funcs(controller.show_frame(SelectionPage),sound()), cursor = 'hand2',borderwidth=3,foreground= "white", bg = "forest green", activebackground= "lime green", activeforeground= "white")
        button1.place(x = 512, y = 500, height = 57, width = 292, anchor = 'n')
        #cretaing option button that will open info page
        button2 = tk.Button(canvas1, text = "INFORMATION",font = ("fixedsys",18), command = lambda:combine_funcs( controller.show_frame(InfoPage),sound()), cursor = 'hand2',borderwidth=3, foreground= "white", bg = "DodgerBlue3", activebackground= "DodgerBlue2", activeforeground= "white")
        button2.place(x = 512, y = 575, height = 57, width = 292, anchor = 'n')
        #creating exit button that will shut down the program
        button3 = tk.Button(canvas1, text = "EXIT GAME",font = ("fixedsys",18), command = lambda: combine_funcs(sound(), app.destroy()), cursor = 'hand2', borderwidth= 3,foreground= "white", bg = "firebrick4", activebackground= "firebrick3", activeforeground= "white")
        button3.place(x = 512, y = 650, height = 57, width = 292, anchor = 'n')
        

#############################################################################################################################################
class InfoPage(tk.Frame):
    """GUI class that creates all widgets in info page and manages them """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #images that are used in this class, must be created as 'self.image' otherwise wont be shown
        self.infoBackGround = openImage('menuPage.png')
        self.backIcon = openImage('back.png')
        self.forwardIcon = openImage('for.png')
        #setting the background
        canvas2 = tk.Canvas(self, width = 1024, height = 768, bg = "white")
        canvas2.create_image(1024/2,768/2,image = self.infoBackGround)
        canvas2.pack()
        #creating the title and middle text that are permanent
        canvas2.create_text(512, 100, fill = 'grey6', font = ("fixedsys", 48, "bold"), text = "INFORMATION", justify = 'center')
        canvas2.create_text(512, 450, fill = 'grey6', font = ("fixedsys", 18), text = getText('text7.txt'),justify = 'center' )
        
        self.pageCount = 0 #page counter to know on with part of the changeable text we are
        #navigation buttons
        buttonBack = tk.Button(canvas2, text = "<", font = ("fixedsys",18,'bold'),state = 'disabled', command = lambda : goBack(self.pageCount), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4", activebackground= "purple3", activeforeground= "white")
        buttonBack.place(x = 100,y = 430, height = 35, width = 35)
        buttonForward = tk.Button(canvas2, text = ">", font = ("fixedsys",18,'bold'), command = lambda : goForward(self.pageCount), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4", activebackground= "purple3", activeforeground= "white")
        buttonForward.place(x = 890,y = 430, height = 35, width = 35)
        #text that will be changed when navigation button pressed
        changeableText = canvas2.create_text(512, 295, fill = 'grey6', font = ("fixedsys", 18), text = getText('text1.txt'), justify = 'center')
        #start game  button that shows selection page frame
        button4 = tk.Button(canvas2, text = "START GAME", font = ("fixedsys",18), command = lambda: combine_funcs(controller.show_frame(SelectionPage),sound(), resetPages()), cursor = 'hand2',borderwidth=3,foreground= "white", bg = "forest green", activebackground= "lime green", activeforeground= "white")
        button4.place(x = 512, y = 575, height = 57, width = 292, anchor = 'n')
        #button that shows menu frame again
        button5 = tk.Button(canvas2, text = "BACK", font = ("fixedsys",18), command = lambda :combine_funcs( controller.show_frame(StartPage),sound(), resetPages()), cursor = 'hand2', borderwidth= 3,foreground= "white", bg = "dark orange", activebackground= "orange", activeforeground= "white")
        button5.place(x = 512, y = 650, height = 57, width = 292, anchor = 'n')

        def resetPages(): # pages should reset when leaving info page
            self.pageCount = 0
            txt = getText('text1.txt')
            canvas2.itemconfigure(changeableText, text = txt)
            
        def goForward(count): # when forward button pressed, change changeable text data file into the further one and add +1 to the counter

            self.pageCount = count + 1
            if  self.pageCount== 1:
                txt = getText('text2.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 2:
                txt = getText('text3.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 3:
                txt = getText('text4.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 4:
                txt = getText('text5.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount== 5:
                txt = getText('text6.txt')
                canvas2.itemconfigure(changeableText, text = txt)

            #this part handles button state - back disabled when on the first page and forward - when on the last one
            if  self.pageCount >0:
                buttonBack.config(state = 'normal')
            else:
                buttonBack.config(state = 'disabled')
                
            if self.pageCount < 5:
                buttonForward.config(state ='normal')
            else:
                buttonForward.config(state = 'disabled')

            
        def goBack(count):# when back button pressed, change changeable text data file into the previous one and add -1 to the counter

            self.pageCount = count - 1
            if self.pageCount == 0:
                txt = getText('text1.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 1:
                txt = getText('text2.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 2:
                txt = getText('text3.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 3:
                txt = getText('text4.txt')
                canvas2.itemconfigure(changeableText, text = txt)
            elif self.pageCount == 4:
                txt = getText('text5.txt')
                canvas2.itemconfigure(changeableText, text = txt)

            if self.pageCount > 0 :
                buttonBack.config(state = 'normal')
            else:
                buttonBack.config(state = 'disabled')
                
            if self.pageCount < 5:
                buttonForward.config(state = 'normal')
            else:
                buttonForward.config(state = 'disabled')
########################################################################################################################
class SelectionPage(tk.Frame):
    '''GUI class that creates objects in selection page and manages them'''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # defining all images that are used by this class
        self.selectionBackGround = openImage('selectPage.png')
        self.miniShop = openImage('miniShop.png')
        self.selectno=openImage('sel0.jpg')
        self.selectyes=openImage('sel1.png')
        self.menu=openImage('menu.png')
        self.game1 = openImage(imageDict[1])
        self.game2 = openImage(imageDict[2])
        self.game3 = openImage(imageDict[3])
        self.game4 = openImage(imageDict[4])
        self.game5 = openImage(imageDict[5])
        self.game6 = openImage(imageDict[6])
        self.game7 = openImage(imageDict[7])
        self.game8 = openImage(imageDict[8])
        self.game9 = openImage(imageDict[9])
        self.game10 = openImage(imageDict[10])
        self.game11 = openImage(imageDict[11])
        self.game12 = openImage(imageDict[12])
        self.game13 = openImage(imageDict[13])
        self.game14 = openImage(imageDict[14])
        self.game15 = openImage(imageDict[15])
        self.game16 = openImage(imageDict[16])
        self.game17 = openImage(imageDict[17])

        self.game1L = openImage(labelDict[1])
        self.game2L = openImage(labelDict[2])
        self.game3L = openImage(labelDict[3])
        self.game4L = openImage(labelDict[4])
        self.game5L = openImage(labelDict[5])
        self.game6L = openImage(labelDict[6])
        self.game7L = openImage(labelDict[7])
        self.game8L = openImage(labelDict[8])
        self.game9L = openImage(labelDict[9])
        self.game10L = openImage(labelDict[10])
        self.game11L = openImage(labelDict[11])
        self.game12L = openImage(labelDict[12])
        self.game13L = openImage(labelDict[13])
        self.game14L = openImage(labelDict[14])
        self.game15L = openImage(labelDict[15])
        self.game16L = openImage(labelDict[16])
        self.game17L = openImage(labelDict[17])

        #variables sucj as counters and the ones that contain widget states
        self.activatedAction = False
        self.activatedAdventure = False
        self.activatedIndie = False
        self.activatedPuzzle = False
        self.activatedSports = False
        self.posCount = 0
        self.entrypos = 0
        self.listCount =0
        
        def setStart(pos): # sets player position acoording which button for setting start on the map was pressed, updates data in Player class
            if pos == 1:
                gamer.startPos = (1,0)
                Player.updatePos(gamer,1, 0)
            elif pos == 2:
                gamer.startPos = (8,25)
                Player.updatePos(gamer,8, 25)

        #sets background
        canvas3 = tk.Canvas(self, width = 1024, height = 768, bg = "lightBlue")
        canvas3.create_image(1024/2,768/2,image = self.selectionBackGround)
        canvas3.pack()

        #category buttons
        cButton1 = tk.Button(canvas3, text = "Action", font = ("fixedsys",12), command = lambda: combine_funcs( expandGames(1),createGameButtons(1, self.activatedAction)), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4", activebackground= "purple3", activeforeground= "white")
        cButton1.place(x = 450, y = 100, height = 35, width = 90)
        cButton2 = tk.Button(canvas3, text = "Adventure", font = ("fixedsys",12), command = lambda: combine_funcs( expandGames(2),createGameButtons(2, self.activatedAdventure)), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4",activebackground= "purple3",activeforeground= "white")
        cButton2.place(x = 550, y = 100, height = 35, width = 90)
        cButton3 = tk.Button(canvas3, text = "Indie", font = ("fixedsys", 12), command = lambda: combine_funcs(expandGames(3), createGameButtons(3, self.activatedIndie)), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4",activebackground= "purple3",activeforeground= "white")
        cButton3.place(x = 650, y = 100, height = 35, width = 90)
        cButton4 = tk.Button(canvas3, text = "Puzzle", font = ("fixedsys", 12), command = lambda: combine_funcs(expandGames(4), createGameButtons(4, self.activatedPuzzle)), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4",activebackground= "purple3",activeforeground= "white")
        cButton4.place(x = 750, y = 100, height = 35, width = 90)
        cButton5 = tk.Button(canvas3, text = "Sports", font = ("fixedsys",12), command = lambda: combine_funcs(expandGames(5), createGameButtons(5,self.activatedSports)), cursor = 'hand2', borderwidth = 3, foreground= "white", bg = "purple4",activebackground= "purple3",activeforeground= "white")
        cButton5.place(x = 850, y = 100, height = 35, width = 90)

        # labels used in window
        canvas3.create_text(205, 62, fill = 'white', font = ("fixedsys", 24, "bold"), text = "YOUR SHOPPING LIST" )
        canvas3.create_text(690, 62, fill = 'white', font = ("fixedsys", 24, "bold"), text = "SELECT YOUR GAMES" )
        canvas3.create_text(700, 430, fill = 'white', font = ("fixedsys", 24, "bold"), text = "SELECT A STARTING POINT" )
        canvas3.create_image(1024/3*2+10,768/3*2+85,image = self.miniShop)

        #player positioning on the map buttons
        pos1Button = tk.Button(canvas3,image = self.selectno ,state = 'normal', command = lambda: combine_funcs(pos1Button.config(image = self.selectyes),pos2Button.config(image = self.selectno),confirm(), setStart(1)), cursor = 'hand2', borderwidth = 3)
        pos2Button = tk.Button(canvas3,image = self.selectno ,state = 'normal', command = lambda: combine_funcs(pos2Button.config(image = self.selectyes),pos1Button.config(image = self.selectno),confirm(), setStart(2)), cursor = 'hand2', borderwidth = 3)
        pos1Button.place(x = 510, y = 498, height = 32, width = 32)
        pos2Button.place(x = 820, y = 614, height = 32, width = 32)

        #confirmation button that opens game frame and info button that opens information page
        confirmButton = tk.Button(canvas3, text = "CONFIRM", font = ("fixedsys",18), command = lambda: combine_funcs(sound(),controller.show_frame(GamePage)), state = 'disabled', cursor = 'hand2',borderwidth=3,foreground= "white", bg = "forest green", activebackground= "lime green", activeforeground= "white")
        confirmButton.place(x = 250, y = 665, height = 57, width = 230, anchor = 'n')
        infoButton = tk.Button(canvas3,image = self.menu, command = lambda:combine_funcs(sound(), controller.show_frame(InfoPage)), cursor = 'hand2',borderwidth=3)
        infoButton.place(x = 80, y = 665, height = 57, width = 60, anchor = 'n')

        #creating all avaible game buttons
        self.gameAc1 = tk.Button(canvas3, image = self.game1 ,command = lambda:  combine_funcs(intolist(1),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAc2 = tk.Button(canvas3, image = self.game2 ,command = lambda: combine_funcs(intolist(2),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAc3 = tk.Button(canvas3, image = self.game3 ,command = lambda:combine_funcs(intolist(3),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAc4 = tk.Button(canvas3, image = self.game4 ,command = lambda:combine_funcs(intolist(4),displayList()), cursor = 'hand2', borderwidth = 3)

        self.gameAd1 = tk.Button(canvas3, image = self.game5,command = lambda: combine_funcs(intolist(5),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAd2 = tk.Button(canvas3, image = self.game6,command = lambda: combine_funcs(intolist(6),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAd3 = tk.Button(canvas3, image = self.game7,command = lambda: combine_funcs(intolist(7),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameAd4 = tk.Button(canvas3, image = self.game8,command = lambda: combine_funcs(intolist(8),displayList()), cursor = 'hand2', borderwidth = 3)

        self.gameI1 = tk.Button(canvas3, image = self.game9,command = lambda: combine_funcs(intolist(9),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameI2 = tk.Button(canvas3, image = self.game10,command = lambda: combine_funcs(intolist(10),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameI3 = tk.Button(canvas3, image = self.game11,command = lambda: combine_funcs(intolist(11),displayList()), cursor = 'hand2', borderwidth = 3)

        self.gameP1 = tk.Button(canvas3,image = self.game12,command = lambda: combine_funcs(intolist(12),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameP2 = tk.Button(canvas3,image = self.game13,command = lambda: combine_funcs(intolist(13),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameP3 = tk.Button(canvas3, image = self.game14,command = lambda: combine_funcs(intolist(14),displayList()), cursor = 'hand2', borderwidth = 3)

        self.gameS1 = tk.Button(canvas3, image = self.game15,command = lambda: combine_funcs(intolist(15),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameS2 = tk.Button(canvas3, image = self.game16,command = lambda: combine_funcs(intolist(16),displayList()), cursor = 'hand2', borderwidth = 3)
        self.gameS3 = tk.Button(canvas3, image = self.game17,command = lambda: combine_funcs(intolist(17),displayList()), cursor = 'hand2', borderwidth = 3)
        
        def createGameButtons(cat, state): # when button were created and destroyed, creates them again
            
            if cat == 1 and state == False:
                self.gameAc1 = tk.Button(canvas3, image = self.game1 ,command = lambda: intolist(1), cursor = 'hand2', borderwidth = 3)
                self.gameAc2 = tk.Button(canvas3, image = self.game2 ,command = lambda: intolist(2), cursor = 'hand2', borderwidth = 3)
                self.gameAc3 = tk.Button(canvas3, image = self.game3 ,command = lambda: intolist(3), cursor = 'hand2', borderwidth = 3)
                self.gameAc4 = tk.Button(canvas3, image = self.game4 ,command = lambda: intolist(4), cursor = 'hand2', borderwidth = 3)
                
            elif cat == 2 and state == False:
                self.gameAd1 = tk.Button(canvas3, image = self.game5,command = lambda: intolist(5), cursor = 'hand2', borderwidth = 3)
                self.gameAd2 = tk.Button(canvas3, image = self.game6,command = lambda: intolist(6), cursor = 'hand2', borderwidth = 3)
                self.gameAd3 = tk.Button(canvas3, image = self.game7,command = lambda: intolist(7), cursor = 'hand2', borderwidth = 3)
                self.gameAd4 = tk.Button(canvas3, image = self.game8,command = lambda: intolist(8), cursor = 'hand2', borderwidth = 3)
                
            elif cat == 3 and state == False:

                self.gameI1 = tk.Button(canvas3, image = self.game9,command = lambda: intolist(9), cursor = 'hand2', borderwidth = 3)
                self.gameI2 = tk.Button(canvas3, image = self.game10,command = lambda: intolist(10), cursor = 'hand2', borderwidth = 3)
                self.gameI3 = tk.Button(canvas3, image = self.game11,command = lambda: intolist(11), cursor = 'hand2', borderwidth = 3)

            elif cat == 4 and state == False:
                
                self.gameP1 = tk.Button(canvas3, image = self.game12,command = lambda: intolist(12), cursor = 'hand2', borderwidth = 3)
                self.gameP2 = tk.Button(canvas3, image = self.game13,command = lambda: intolist(13), cursor = 'hand2', borderwidth = 3)
                self.gameP3 = tk.Button(canvas3, image = self.game14,command = lambda: intolist(14), cursor = 'hand2', borderwidth = 3)

            elif cat == 5 and state == False:

                self.gameS1 = tk.Button(canvas3, image = self.game15,command = lambda: intolist(15), cursor = 'hand2', borderwidth = 3)
                self.gameS2 = tk.Button(canvas3, image = self.game16,command = lambda: intolist(16), cursor = 'hand2', borderwidth = 3)
                self.gameS3 = tk.Button(canvas3, image = self.game17,command = lambda: intolist(17), cursor = 'hand2', borderwidth = 3)
            

        def expandGames(category): # if the category button is pressed once places game buttons on screen, when category button is pressed again, game buttons are destroyed

            if category == 1:
                
                if self.activatedAction == False:
                    self.gameAc1.place(x = 460, y = 150, height = 42, width = 66)
                    self.gameAc2.place(x = 460, y = 200, height = 42, width = 66)
                    self.gameAc3.place(x = 460, y = 250, height = 42, width = 66)
                    self.gameAc4.place(x = 460, y = 300, height = 42, width = 66)

                elif self.activatedAction == True:
                    self.gameAc1.destroy()
                    self.gameAc2.destroy()
                    self.gameAc3.destroy()
                    self.gameAc4.destroy()

                if self.activatedAction == False:
                    self.activatedAction = True
                else:
                    self.activatedAction = False

                    

            if category == 2:
                
                if self.activatedAdventure == False:
                    self.gameAd1.place(x = 560, y = 150, height = 42, width = 66)
                    self.gameAd2.place(x = 560, y = 200, height = 42, width = 66)
                    self.gameAd3.place(x = 560, y = 250, height = 42, width = 66)
                    self.gameAd4.place(x = 560, y = 300, height = 42, width = 66)
                    
                elif self.activatedAdventure == True:
                    self.gameAd1.destroy()
                    self.gameAd2.destroy()
                    self.gameAd3.destroy()
                    self.gameAd4.destroy()

                if self.activatedAdventure == False:
                    self.activatedAdventure = True
                else:
                    self.activatedAdventure = False
                    

            if category == 3:
                
                if self.activatedIndie == False:
                    self.gameI1.place(x = 660, y = 150, height = 42, width = 66)
                    self.gameI2.place(x = 660, y = 200, height = 42, width = 66)
                    self.gameI3.place(x = 660, y = 250, height = 42, width = 66)
                    
                elif self.activatedIndie == True:
                    self.gameI1.destroy()
                    self.gameI2.destroy()
                    self.gameI3.destroy()

                if self.activatedIndie == False:
                    self.activatedIndie = True
                else:
                    self.activatedIndie = False
                    
            if category == 4:
                
                if self.activatedPuzzle == False:
                    self.gameP1.place(x = 760, y = 150, height = 42, width = 66)
                    self.gameP2.place(x = 760, y = 200, height = 42, width = 66)
                    self.gameP3.place(x = 760, y = 250, height = 42, width = 66)
                    
                elif self.activatedPuzzle == True:
                    self.gameP1.destroy()
                    self.gameP2.destroy()
                    self.gameP3.destroy()

                if self.activatedPuzzle == False:
                    self.activatedPuzzle = True
                else:
                    self.activatedPuzzle = False
                

            if category == 5:

                if self.activatedSports == False:
                    self.gameS1.place(x = 860, y = 150, height = 42, width = 66)
                    self.gameS2.place(x = 860, y = 200, height = 42, width = 66)
                    self.gameS3.place(x = 860, y = 250, height = 42, width = 66)
                    
                elif self.activatedSports == True:
                    self.gameS1.destroy()
                    self.gameS2.destroy()
                    self.gameS3.destroy()

                if self.activatedSports == False:
                    self.activatedSports = True
                else:
                    self.activatedSports = False

            
        def intolist(gameID):
            #adds selected games into global list for selected games that will be submited for searching
            inGameList = binarySearch(selectedGameList, gameID)
            if self.listCount<7 and not inGameList:
                selectedGameList.append(gameID)
                self.listCount+=1
            
        def displayList():
            #prints on screen(shopping list) selected games
            global imageDict
            posx = 1024/2-450
            posy = 800/2-270
            alist = []
            alist=[self.game1L, 
            self.game2L,
            self.game3L,
            self.game4L,
            self.game5L, 
            self.game6L,
            self.game7L,
            self.game8L,
            self.game9L,
            self.game10L,
            self.game11L,
            self.game12L,
            self.game13L ,
            self.game14L ,
            self.game15L,
            self.game16L,
            self.game17L]
            
            for game in selectedGameList:
                gameLabel = tk.Label(canvas3, image = alist[game-1])
                gameLabel.place(x = posx, y = posy)
                posy = posy + 70             

        def confirm():
            #makes 'confirm' button available only when game list is not empty and starting point is selected
            if len(selectedGameList)>0:
                confirmButton.config(state = 'normal')
#############################################################################################################

class Node:
    """Class used to store an x and y coordanates of each  node in the map for a* algorithm"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return ((self.x, self.y) ==
                (other.x, other.y))
    
    def __hash__(self):
        return hash((self.x, self.y))

class PathFind:
    """ class that finds a path between two points on the map (graph), must specify bounds of the map, map should be in 0 and 1's"""
    
    def __init__(self, array, boundsx, boundsy):
        self.boundsx = boundsx
        self.boundsy = boundsy
        self.array = array
   
    def AStar(self, start, goal):
    	# takes start and goal positions of the object and creates most optimal path between them, uses lists to store child nodes 

        array = self.array
        closedSet = []
        
        openSet = [start]

        cameFrom = {}

        gScore = {}
        gScore[start] = 0

        fScore = {}
        fScore[start] = self.heuristic_cost_estimate(start, goal)

        
        while openSet != [] :
            
            current = self.lowestValue(openSet, fScore)
            if current.x == goal.x and current.y == goal.y:
                return self.reconstructPath(cameFrom, goal)
            
            openSet.remove(current)
            closedSet.append(current)

            neighbourNodes = []
            if current.x > 0:
                if array[current.x -1][current.y] == 0:
                    neighbourNodes.append(Node(current.x -1, current.y))
                    
            if current.y > 0:
                if array[current.x][current.y - 1] == 0:
                    neighbourNodes.append(Node(current.x, current.y - 1))

            if current.x != self.boundsx - 1:
                if array[current.x + 1][current.y] == 0:
                        neighbourNodes.append(Node(current.x + 1, current.y))

            if current.y != self.boundsy - 1:    
                if array[current.x][current.y + 1] == 0:
                        neighbourNodes.append(Node(current.x, current.y + 1))
                        
            for neighbour in neighbourNodes:
                if self.linearSearch(closedSet, neighbour):
                    continue
                
                tentative_gScore = gScore[current] + 1

                if not self.linearSearch(openSet, neighbour):
                    openSet.append(neighbour)
                elif tentative_gScore >= gScore[neighbour]:
                    continue
                
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_gScore
                fScore[neighbour] = gScore[neighbour] + self.heuristic_cost_estimate(neighbour, goal)
             
        return False
            
            

    def heuristic_cost_estimate(self, start, end):
        
        x = abs( start.x - end.x)
        y = abs(start.y - end.y)

        return x + y
    
    def linearSearch(self, array, val):
        pos = 0
        while pos < len (array):
            if array[pos] == val:
                return True
            pos = pos + 1
        return False

    def lowestValue(self, openSet, dic):
        lowestVal = None
        lowestKey = ""

        for value in openSet:
            score = dic[value]
            if lowestVal == None or score < lowestVal:
                lowestKey = value
                lowestVal = score
                
        return lowestKey

    def reconstructPath(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)
        total_path.reverse()
        return total_path
            


def array():
   
    Matrix =[	[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[ 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
		[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
 
   
    return Matrix
    

def getPath(startx, starty, finishx,finishy):
    # returns path as a list created by A*
    print(str(startx)+' ' +str(starty)+' ' +str( finishy)+' '+str(finishx))
    listcoord = []
    c= 0
    Path = PathFind(array(),27, 27)
    path = Path.AStar(Node(startx,starty), Node(finishy,finishx))
    for point in path:   
        coo = point.x, point.y
        listcoord.append(coo)
        c+=1
    return(listcoord)

##############################################################################################################
class GamePage(tk.Frame):
    ''' class for creating objects and managing them of the actual game'''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.gameBackground = openImage('shop1.png')
        self.playerIcon = openImage('gamer.jpg')
        var = tk.IntVar()
        var2 = tk.IntVar()
        self.dec = int()
        self.dec = 0
        self.increasing = True
        self.budget = randint(70,100)
        self.rating = 0
        #default sorting options (according game price, in increasing order, using shell sort
        self.sortBy = 2
        self.sortIn = 1
        self.sortA = 1

        itemDict = {1:iGame1, 2:iGame2, 3:iGame3, 4:iGame4,
                    5:iGame5, 6:iGame6, 7:iGame7, 8:iGame8,
                    9:iGame9, 10:iGame10, 11:iGame11, 12:iGame12,
                    13:iGame13, 14:iGame14, 15:iGame15, 16:iGame16, 17:iGame17}

        self.game1 = openImage(imageDict[1])
        self.game2 = openImage(imageDict[2])
        self.game3 = openImage(imageDict[3])
        self.game4 = openImage(imageDict[4])
        self.game5 = openImage(imageDict[5])
        self.game6 = openImage(imageDict[6])
        self.game7 = openImage(imageDict[7])
        self.game8 = openImage(imageDict[8])
        self.game9 = openImage(imageDict[9])
        self.game10 = openImage(imageDict[10])
        self.game11 = openImage(imageDict[11])
        self.game12 = openImage(imageDict[12])
        self.game13 = openImage(imageDict[13])
        self.game14 = openImage(imageDict[14])
        self.game15 = openImage(imageDict[15])
        self.game16 = openImage(imageDict[16])
        self.game17 = openImage(imageDict[17])

        pictureDict = {1:self.game1, 2:self.game2, 3:self.game3,
                       4:self.game4, 5:self.game5, 6:self.game6,
                       7:self.game7, 8:self.game8, 9:self.game9,
                       10:self.game10, 11:self.game11, 12:self.game12,
                       13:self.game13, 14:self.game14, 15:self.game15,
                       16:self.game16,17:self.game17}
        
        canvas4 = tk.Canvas(self, width = 1024, height = 768, bg = "white")
        canvas4.create_image(1024/2,768/2,image = self.gameBackground)
        canvas4.pack()
        
        startButton = tk.Button(canvas4, text = "START", font = ("fixedsys",18),state = 'disabled', command = lambda: combine_funcs(setTime(),sound(), self.minutes.destroy(), self.seconds.destroy(),placeGamesToCollect(), showTime(), movePlayer(),startButton.destroy()), cursor = 'hand2',borderwidth=3,foreground= "white", bg = "forest green", activebackground= "lime green", activeforeground= "white")
        startButton.place(x = 512, y = 694, height = 57, width = 292, anchor = 'n')
        
        timeLabel = tk.Label(canvas4, font = ("fixedsys",48),activebackground='grey10', activeforeground='white',background= 'grey10', foreground= 'white',justify= 'center')
        timeLabel.place(x = 550, y = 600)
        
        selectSorting1 = tk.Radiobutton(canvas4,variable = var, value = 1,selectcolor = 'grey8', text="Shell sort", font = ("fixedsys",12), bg = 'grey10', command = lambda: setTypeA(1), fg = 'white', cursor = 'hand2')
        selectSorting1.place (x = 700, y = 610)
        selectSorting2 = tk.Radiobutton(canvas4,variable = var,value = 2, selectcolor= 'grey8', text="Merge sort", font = ("fixedsys",12), bg = 'grey10', command = lambda: setTypeA(2), fg = 'white', cursor = 'hand2')
        selectSorting2.place (x = 700, y = 640)
        selectSorting4 = tk.Radiobutton(canvas4,variable = var2, value = 1,selectcolor = 'grey8', text="Name sort", font = ("fixedsys",12), bg = 'grey10', command = lambda: setTypeBy(1), fg = 'white', cursor = 'hand2')
        selectSorting4.place (x = 850, y = 610)
        selectSorting5 = tk.Radiobutton(canvas4,variable = var2, value = 2, selectcolor = 'grey8', text="Price sort", font = ("fixedsys",12), bg = 'grey10', command = lambda: setTypeBy(2), fg = 'white',cursor = 'hand2')
        selectSorting5.place (x = 850, y = 640)
        selectSorting6 = tk.Radiobutton(canvas4,variable = var2,value = 3, selectcolor= 'grey8', text="Rating sort", font = ("fixedsys",12), bg = 'grey10', command = lambda: setTypeBy(3), fg = 'white', cursor = 'hand2')
        selectSorting6.place (x = 850, y = 670)
        
        selectDec = tk.Checkbutton(canvas4, text = 'Decreasing', variable = self.dec, onvalue = 1, offvalue = 0, command = lambda: setTypeIn(2), font = ("fixedsys",12), fg = 'white', bg = 'grey10',cursor = 'hand2',selectcolor= 'grey10')
        selectDec.place (x = 765, y = 710)
       
        self.minutes = tk.Spinbox (canvas4, from_=0, to = 10,cursor = 'hand2', fg = 'grey8', font = ("fixedsys",32), width = 2, command = lambda: startButton.config(state='normal'))
        self.minutes.place(x = 370, y = 620)
        self.seconds = tk.Spinbox (canvas4, from_=0, to = 59, cursor = 'hand2', fg = 'grey8', font = ("fixedsys",32), width = 2, command = lambda: startButton.config(state='normal'))
        self.seconds.place(x = 525, y = 620)
        
        self.gamesToBuy = selectedGameList
        self.collectedGames = []
            
        
        def placeGamesToCollect():
            #creates images on canvas that will be collected
            self.gamesToBuy = selectedGameList
            self.coordList = [(133,224-32),(261,288-32),(421,96-32),(581,288-32),(709,96-32),(901,96-32),(485,192-32),(133,288-32),(325,288-32),(514,96-32),(261,160-32),(453,288-32),(613,128-32),(837,288-32),(709,288-32),(901,192-32),(805,192-32)]
            self.coordDict = {}
            self.additionalDict = {}
            for game in self.gamesToBuy:
                self.coordDict[game] = self.coordList[game-1]
            for game in self.gamesToBuy:
                
                if game == 1:
                    self.inGame1 = tk.Label(canvas4, image = self.game1)
                    self.inGame1.place(x = iGame1.X, y = iGame1.Y)
                    self.additionalDict[game] = self.inGame1
                if game == 2:
                    self.inGame2 = tk.Label(canvas4, image = self.game2)
                    self.inGame2.place(x =  iGame2.X, y =  iGame2.Y)
                    self.additionalDict[game] = self.inGame2
                if game == 3:
                    self.inGame3 = tk.Label(canvas4, image = self.game3)
                    self.inGame3.place(x =  iGame3.X, y = iGame3.Y)
                    self.additionalDict[game] =self.inGame3
                if game == 4:
                    self.inGame4 = tk.Label(canvas4, image = self.game4)
                    self.inGame4.place(x =  iGame4.X, y =  iGame4.Y)
                    self.additionalDict[game] = self.inGame4
                if game == 5:
                    self.inGame5 = tk.Label(canvas4, image = self.game5)
                    self.inGame5.place(x =  iGame5.X, y = iGame5.Y)
                    self.additionalDict[game] = self.inGame5
                if game == 6:
                    self.inGame6 = tk.Label(canvas4, image = self.game6)
                    self.inGame6.place(x =  iGame6.X, y =  iGame6.Y)
                    self.additionalDict[game] = self.inGame6
                if game == 7:
                    self.inGame7 = tk.Label(canvas4, image = self.game7)
                    self.inGame7.place(x = iGame7.X, y =  iGame7.Y)
                    self.additionalDict[game] = self.inGame7
                if game == 8:
                    self.inGame8 = tk.Label(canvas4, image = self.game8)
                    self.inGame8.place(x =  iGame8.X, y =  iGame8.Y)
                    self.additionalDict[game] = self.inGame8
                if game == 9:
                    self.inGame9 = tk.Label(canvas4, image = self.game9)
                    self.inGame9.place(x =  iGame9.X, y =  iGame9.Y)
                    self.additionalDict[game] = self.inGame9
                if game == 10:
                    self.inGame10 = tk.Label(canvas4, image = self.game10)
                    self.inGame10.place(x = iGame10.X, y =  iGame10.Y)
                    self.additionalDict[game] = self.inGame10
                if game == 11:
                    self.inGame11 = tk.Label(canvas4, image = self.game11)
                    self.inGame11.place(x =  iGame11.X, y =  iGame11.Y)
                    self.additionalDict[game] = self.inGame11
                if game == 12:
                    self.inGame12 = tk.Label(canvas4, image = self.game12)
                    self.inGame12.place(x = iGame12.X, y =  iGame12.Y)
                    self.additionalDict[game] = self.inGame12
                if game == 13:
                    self.inGame13 = tk.Label(canvas4, image = self.game13)
                    self.inGame13.place(x =  iGame13.X, y = iGame13.Y)
                    self.additionalDict[game] = self.inGame13
                if game == 14:
                    self.inGame14 = tk.Label(canvas4, image = self.game14)
                    self.inGame14.place(x = iGame14.X,  y =iGame14.Y)
                    self.additionalDict[game] = self.inGame14
                if game == 15:
                    self.inGame15 = tk.Label(canvas4, image = self.game15)
                    self.inGame15.place(x =  iGame15.X, y =  iGame15.Y)
                    self.additionalDict[game] = self.inGame15
                if game == 16:
                    self.inGame16 = tk.Label(canvas4, image = self.game16)
                    self.inGame16.place(x =  iGame16.X, y =  iGame16.Y)
                    self.additionalDict[game] = self.inGame16
                if game == 17:
                    self.inGame17 = tk.Label(canvas4, image = self.game17)
                    self.inGame17.place(x =  iGame17.X, y =  iGame17.Y)
                    self.additionalDict[game] = self.inGame17

            self.player = tk.Label(canvas4, image = self.playerIcon)

        def shellSort(increasing,name, price):

            if increasing == True:
                inc = len(price) // 2
                while inc:
                    for i in range(len(price)):
                        j = i
                        temp = price[i]
                        temp2= name[i]
                        #add here if need to be sorted
                        while j >= inc and price[j-inc] > temp:
                            price[j] = price[j - inc]
                            name[j] = name[j- inc]
                            #add here if need to be sorted
                            j -= inc
                        price[j] = temp
                        name[j] = temp2
                        #add here if need to be sorted
                    inc = inc//2 if inc//2 else (0 if inc==1 else 1)
            else:

                inc = len(price) // 2
                while inc:
                    for i in range(len(price)):
                        j = i
                        temp = price[i]
                        temp2= name[i]
                        #add here if need to be sorted
                        while j >= inc and price[j-inc] < temp:
                            price[j] = price[j - inc]
                            name[j] = name[j- inc]
                            #add here if need to be sorted
                            j -= inc
                        price[j] = temp
                        name[j] = temp2
                        #add here if need to be sorted
                    inc = inc//2 if inc//2 else (0 if inc==1 else 1)


        def  _ItComparator(x ,y):return x>y

        def  _ItComparatorDec(x ,y):return x<y


        def mergeSort(increasing,price,name, comparator):#add here
            if len(price)>1:
                mid = int(len(price)//2)
                lefthalf = price[:mid]
                righthalf = price[mid:]
                lefthalf2 = name[:mid]
                righthalf2 = name[mid:]
                #add here

                mergeSort(increasing,lefthalf,lefthalf2, comparator)#add here
                mergeSort(increasing,righthalf,righthalf2, comparator)#add here

                i=0
                lefthalfi=0
                righthalfi=0
                lefthalf2i=0
                righthalf2i=0
                while True:
                    if lefthalfi>=len(lefthalf):price[i:]=  righthalf[righthalfi:]; break
                    if righthalfi >= len(righthalf):price[i:]= lefthalf[lefthalfi:]; break
                    if comparator(lefthalf[lefthalfi],righthalf[righthalfi]):
                        price[i]=lefthalf[lefthalfi]
                        lefthalfi += 1
                    else:
                        price[i]=righthalf[righthalfi]
                        righthalfi+=1
                    i+=1
                    
        def quickSort(data):
           quickSortHelper(data,0,len(data)-1)

        def quickSortHelper(data,first_value,last_value):
           if first_value < last_value:

           split_data = partition(data,first_value,last_value)

           quickSortHelper(data,first_value,split_data-1)
           quickSortHelper(data,split_data+1,last_value)


        def partition(data,first_value,last_value):
           pivot = data[first_value]

           left_pivot = first_value+1
           right_pivot = last_value

           done = False
           while not done:

               while left_pivot <= right_pivot and data[left_pivot] <= pivot:
                   left_pivot = left_pivot + 1

               while data[right_pivot] >= pivot and right_pivot >= left_pivot:
                   right_pivot = right_pivot -1

               if right_pivot < left_pivot:
                   done = True
               else:
                   temp = data[left_pivot]
                   data[left_pivot] = data[right_pivot]
                   data[right_pivot] = temp

           temp = data[first_value]
           data[first_value] = data[right_pivot]
           data[right_pivot] = temp


           return right_pivot

            
        def setTypeIn(x): #sorting by : increasing / decreasing order
            self.sortIn = x
        
        def setTypeA(x): #sorting using shell / merge algorithm
            self.sortA = x

        def setTypeBy(x):# sorting by : name / price / rating         
            self.sortBy = x

        def sortCollectedGames(alist,nameList, priceList, ratingList):
            localList = []
            
            if self.sortBy ==  1:#name
                if self.sortIn == 1:#increasing
                    if self.sortA == 1:#shellsort
                        shellSort(True,alist, nameList)
                        localList = alist
                    
                    elif self.sortA == 2:#mergesort
                        mergeSort(True,alist,nameList,comparator = _ItComparator)
                        localList = alist

                elif self.sortIn ==2:#decreaing
                    if self.sortA == 1:#shellsort
                        shellSort(False,alist, nameList)
                        localList = alist
                   
                    elif self.sortA == 2:#mergesort
                        mergeSort(False,alist,nameList,comparator = _ItComparatorDec)
                        localList = alist

                
            elif self.sortBy == 2:#price
                if self.sortIn == 1:#increasing
                    if self.sortA == 1:#shellsort
                        shellSort(True,alist, priceList)
                        localList = alist
                   
                    elif self.sortA == 2:#mergesort
                        mergeSort(True,alist,priceList,comparator = _ItComparator)
                        localList = alist

                elif self.sortIn ==2:#decreaing
                    if self.sortA == 1:#shellsort
                        shellSort(False,alist, priceList)
                        localList = alist
                    
                    elif self.sortA == 2:#mergesort
                        mergeSort(False,alist,priceList,comparator = _ItComparatorDec)
                        localList = alist

                
            elif self.sortBy == 3:
                if self.sortIn == 1:#increasing
                    if self.sortA == 1:#shellsort
                        shellSort(True,alist, ratingList)
                        localList = alist
                   
                    elif self.sortA == 2:#mergesort
                        mergeSort(True,alist,ratingList,comparator = _ItComparator)
                        localList = alist

                elif self.sortIn ==2:#decreaing
                    if self.sortA == 1:#shellsort
                        shellSort(False,alist, ratingList)
                        localList = alist
                   
                    elif self.sortA == 2:#mergesort
                        mergeSort(False,alist,ratingList,comparator = _ItComparatorDec)
                        localList = alist
            
            localx = 150
            localy = 500

            for i in localList:
                img = pictureDict[i]
                canvas4.create_image(localx,localy, image = img)
                localx += 120
                canvas4.update()
        
            

         
        def setTime():
            global sec
            m = int(self.minutes.get())
            print(str(m))
            s = int(self.seconds.get())
            print(str(s))
            sec = m*60+s

        def showTime():
            global sec
            if sec >0 :
                sec-=1
                timeLabel['text'] = sec
            else:
                sec = 1
            
            canvas4.create_text(505,665,text = "Time Left:       s" ,font = ("fixedsys",24),fill = 'white',justify= 'center')

        def walk(path):
            #draws player on canvas
            i= 0
            while i < len(path) and sec>0 :
                Y,X= path[i]
                self.player.place(x= X*32+101,y = Y*32 +32)
                canvas4.update()
                gamer.updatePos(Y,X)
                sleep(0.5)
                i+=1
                canvas4.after(500, showTime)


        def movePlayer():

            nameList = []
            priceList = []
            ratingList = []
            self.rating = 0
            lenght = len(self.gamesToBuy)
            if self.budget >0:
                for i in range(lenght):
                    if gamer.startPos == (1,0):
                        toFind = min(self.coordDict, key = self.coordDict.get)
                    else:
                        toFind = max(self.coordDict, key = self.coordDict.get)
                        
                    fx, fy = self.coordDict[toFind]
                    self.coordDict.pop(toFind)
                    fx = (fx - 101)//32
                    fy = (fy - 32)//32
                    path = getPath(gamer.xpos,gamer.ypos, fx,fy)
                    walk(path)
                    item = itemDict[toFind]
                    self.budget = self.budget - item.price
                    if self.budget >=0:
                        self.rating += item.rating
                        nameList.append(item.name)
                        priceList.append(item.price)
                        ratingList.append(item.rating)
                        self.additionalDict[toFind].destroy()
                        self.collectedGames.append(toFind)
                    else:
                        self.budget += item.price
                        continue

                    
                    sortCollectedGames(self.collectedGames, nameList, priceList, ratingList)
                    collectedStatus['text'] = 'Collected: ' + str(len(self.collectedGames)) + ' / '+ str(len(self.gamesToBuy))
                    budgetStatus['text'] = 'Budget: '+ str(self.budget)
                    ratingStatus['text'] = 'Avg Rating: '+ str(round(int(self.rating)/len(self.collectedGames),2))
                    
            if len(self.collectedGames) != len(self.gamesToBuy):
                canvas4.create_text(500, 380, text = 'GAME OVER', font = ('fixedsys',52), fill = 'red', justify= 'center')
                startButton.destroy()
            else:
                canvas4.create_text(500, 380, text = 'CONGRATULATIONS!', font = ('fixedsys',52), fill = 'gold', justify= 'center')
                startButton.destroy()
                
            resultButton = tk.Button(canvas4, text = "EXIT GAME",font = ("fixedsys",18), command = lambda: combine_funcs(sound(),app.destroy() ), cursor = 'hand2', borderwidth= 3,foreground= "white", bg = "firebrick4", activebackground= "firebrick3", activeforeground= "white")
            resultButton.place(x = 512, y = 694, height = 57, width = 292, anchor = 'n')



            

        collectedStatus = tk.Label(canvas4, text =( 'Collected: ' + str(len(self.collectedGames)) + ' / '+ str(len(self.gamesToBuy))),font = ("fixedsys",24),activebackground='grey10', activeforeground='white',background= 'grey10',foreground= 'white')
        collectedStatus.place(x =50,y= 610)
        budgetStatus = tk.Label(canvas4, text = ('Budget: '+ str(self.budget)),font = ("fixedsys",24),activebackground='grey10', activeforeground='white',background= 'grey10',foreground= 'white')
        budgetStatus.place(x =50,y= 650)
        ratingStatus = tk.Label(canvas4, text = ('Avg Rating: '+ str(0)),font = ("fixedsys",24),activebackground='grey10', activeforeground='white',background= 'grey10',foreground= 'white')
        ratingStatus.place(x =50,y= 690)
        timeLabel = tk.Label(canvas4, font = ("fixedsys",48),activebackground='grey10', activeforeground='white',background= 'grey10', foreground= 'white',justify= 'center')
        timeLabel.place(x = 545, y = 610)
#############################################################################################################################################################################

class Player():
    '''keeps player image and position'''
    def __init__(self, image, startingPosition = (0,0)):
        self.image = image
        self.startPos = startingPosition
        self.xpos = startingPosition[0]
        self.ypos =  startingPosition[1]

    def updatePos(self, xnew, ynew):
        self.xpos = xnew
        self.ypos = ynew


        


##############################################################################################################################################

gamer = Player('gamer.jpg')
iGame1 = Game(1, 'BattleField', 'Action', 23, 5,'game1.gif', 'lbl1.png', 133, 192)
iGame2 = Game(2,'GTA 5', 'Action', 40, 5, 'game2.png','lbl2.png',261,256)
iGame3 = Game(3,'XCOM2', 'Action', 20, 4, 'game3.png','lbl3.png', 421,64)
iGame4 = Game(4,'Call Of Duty','Action', 10, 3,'game4.gif','lbl4.png', 581, 256)
iGame5 = Game(5,'Sonic','Adventure', 4, 3,'game5.png','lbl5.png', 709, 64)
iGame6 = Game(6,'DayZ', 'Adventure',20, 2, 'game6.png','lbl6.png', 901,64)
iGame7 = Game(7,'Witcher 3', 'Adventure',50, 4, 'game7.gif','lbl7.png',485,160)
iGame8 = Game(8, 'Fall Out 4','Adventure', 40, 5, 'game8.png','lbl8.png', 133,256)
iGame9 = Game(9, 'Limbo' ,'Indie',3,4,'game9.png','lbl9.png',325, 256)
iGame10 = Game(10,'Undertale', 'Indie', 5, 4, 'game10.png','lbl10.png', 482,64)
iGame11 = Game(11,'To The Moon','Indie', 2, 3, 'game11.png','lbl11.png',261,160)
iGame12 = Game(12,'Little Big Planet','Puzzle', 6, 2 , 'game12.png','lbl12.png',453,256)
iGame13 = Game(13,'Infra', 'Puzzle',11,2, 'game13.png','lbl13.png',613,96)
iGame14 = Game(14,'Puzzle Stages','Puzzle', 1,1,'game14.png','lbl14.png',837,256)
iGame15 = Game(15,'The Crew', 'Sports',13, 3, 'game15.png','lbl15.png', 709,256)
iGame16 = Game(16,'Fifa 15','Sports', 25, 4, 'game16.gif','lbl16.png',901, 160)
iGame17 = Game(17,'Need for Speed','Sports', 5, 4, 'game17.gif','lbl17.png', 805,160)


app = GameShop()
app.mainloop()
        
