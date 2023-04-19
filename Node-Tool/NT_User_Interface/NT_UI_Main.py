#import libraies
from tkinter import ttk
import tkinter as tk

from NT_User_Interface.NT_UI_Node_Add import AddNodeGui
from NT_User_Interface.NT_UI_Node_Remove import RemoveNodeGui
from NT_User_Interface.NT_UI_Node_Update import UpdateNodeGui
from NT_User_Interface.NT_UI_Graph import DrawGraph

def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    #UI.destroy() 

#Define a function to close the window with confirmation window
def ConfirmClose(windowLocation,UI):
    windowX = str(windowLocation[0]+80)
    windowY = str(windowLocation[1]+20)

    #Create Higher level Window
    closeWindow = tk.Toplevel()
    closeWindow.title('Confirm Exit')
    closeWindow.geometry("+"+windowX+"+"+windowY)
    warningMessage = tk.Label(closeWindow, text="Close Program Y/N?")
    warningMessage.pack()
    noButton = tk.Button(closeWindow, width=20 ,text="No", command=lambda:closeWindow.destroy())
    noButton.pack(side=tk.LEFT)
    yesButton = tk.Button(closeWindow, width=20 ,text="Yes", command=lambda:(closeWindow.destroy(),UI.quit()))
    yesButton.pack(side=tk.LEFT)

#Main user interface for program
def MainGUI(windowLocation,networkMap,nodes):    #Tkinter GUI

    #Create instance of GUI class
    UI = tk.Tk()

    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("+"+windowX+"+"+windowY)

    #Configure Windows
    UI.title('Node-tool')
    nodeList = []

    UI.nodeListHeadder = tk.Label(UI, text="Current Nodes")
    UI.nodeListHeadder.pack()

    for node in nodes:
        nodeList.append(node.name)
    if (len(nodeList) ==0):
        nodeList = "No nodes have been created"

    UI.nodeList = tk.Label(UI, text=str(nodeList))
    UI.nodeList.pack()

    UI.button = tk.Button(UI, text="Add Node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                               UI.destroy(),
                                                               AddNodeGui(windowLocation,networkMap,nodes)))
    UI.button.pack(side=tk.LEFT)
    UI.button = tk.Button(UI, text="Remove Node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                  UI.destroy(),
                                                                  RemoveNodeGui(windowLocation,networkMap,nodes)))
    UI.button.pack(side=tk.LEFT)
    UI.button = tk.Button(UI, text="Update Node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                  UI.destroy(),
                                                                  UpdateNodeGui(windowLocation,networkMap,nodes)))
    UI.button.pack(side=tk.LEFT)
    UI.button = tk.Button(UI, text="Draw Network Graph", command=lambda:DrawGraph(UI,networkMap))
    UI.button.pack(side=tk.LEFT)
    UI.button = tk.Button(UI, text="Close Program", command=lambda:(UpdateWindowLocation(UI,windowLocation),ConfirmClose(windowLocation,UI)))
    UI.button.pack(side=tk.LEFT)