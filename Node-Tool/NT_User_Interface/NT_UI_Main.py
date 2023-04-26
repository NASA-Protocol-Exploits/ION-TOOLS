#import libraies
from tkinter import ttk
import tkinter as tk

from NT_User_Interface.NT_UI_Node_Add import AddNodeGui
from NT_User_Interface.NT_UI_Node_Remove import RemoveNodeGui
from NT_User_Interface.NT_UI_Node_Update import UpdateNodeGui
from NT_User_Interface.NT_UI_Graph import DrawGraph
from NT_User_Interface.NT_UI_Error import ErrorGUI
from NT_User_Interface.NT_UI_Node_Connections import NodeConnectionsGui

def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return windowLocation

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


def RemoveNode(UI,windowLocation,networkMap,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to remove")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        RemoveNodeGui(windowLocation,networkMap,nodes)

def UpdateNode(UI,windowLocation,networkMap,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to update")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        UpdateNodeGui(windowLocation,networkMap,nodes)

def ModifyNodeConnections(UI,windowLocation,networkMap,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to modify")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        NodeConnectionsGui(windowLocation,networkMap,nodes)
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
    
    totalColums = 6

    UI.nodeListHeadder = tk.Label(UI, text="Current Nodes")
    UI.nodeListHeadder.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)

    for node in nodes:
        nodeList.append(node.name)
    if (len(nodeList) ==0):
        nodeList = "No nodes have been created"

    UI.nodeList = tk.Label(UI, text=str(nodeList))
    UI.nodeList.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)

    buttonWidth = 20

    UI.button = tk.Button(UI,width=buttonWidth , text="Add Node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                               UI.destroy(),
                                                               AddNodeGui(windowLocation,networkMap,nodes)))
    UI.button.grid(row = 3, column = 0,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth , text="Remove Node", command=lambda:RemoveNode(UI,windowLocation,networkMap,nodes))
    UI.button.grid(row = 3, column = 1,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Update Node", command=lambda:UpdateNode(UI,windowLocation,networkMap,nodes))
    UI.button.grid(row = 3, column = 2,pady = 2)

    UI.button = tk.Button(UI, width=buttonWidth ,text="Modify Node Connections", command=lambda:ModifyNodeConnections(UI,windowLocation,networkMap,nodes))
    UI.button.grid(row = 4, column = 0,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Draw Network Graph", command=lambda:DrawGraph(UI,networkMap))
    UI.button.grid(row = 4, column = 1,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Close Program", command=lambda:(UpdateWindowLocation(UI,windowLocation),ConfirmClose(windowLocation,UI)))
    UI.button.grid(row = 4, column = 2,pady = 2)