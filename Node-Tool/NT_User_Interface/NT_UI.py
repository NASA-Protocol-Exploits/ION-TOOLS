#import libraies
from tkinter import ttk
import tkinter as tk
import NT_User_Interface.NT_UI_Main
nodes = []
#Window Starting Location
windowLocation = [300,300]

def LoadGUI(networkMap):    #Tkinter GUI

    #Create instance of GUI class
    root = tk.Tk()
    root.withdraw()
    NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,networkMap,nodes)

    return root