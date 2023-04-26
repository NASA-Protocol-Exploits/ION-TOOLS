#import libraies
import tkinter as tk
import NT_User_Interface.NT_UI_Main

#Varible for storing array of nodes used thoughout the application
nodes = []
#Window Starting Location
windowLocation = [300,300]

#Loads the initial graphical user interface
def LoadGUI():

    #Create instance of GUI class
    root = tk.Tk()
    root.withdraw()
    #Call function to draw primary user interface
    NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)

    return root