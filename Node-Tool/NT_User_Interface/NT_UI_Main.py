#import libraies
import tkinter as tk

#Import all sub-UIs that can be called from the main window
from NT_User_Interface.NT_UI_Node_Add import AddNodeGui
from NT_User_Interface.NT_UI_Node_Remove import RemoveNodeGui
from NT_User_Interface.NT_UI_Node_Modify import ModifyNodeGui
from NT_User_Interface.NT_UI_Graph import DrawGraph
from NT_User_Interface.NT_UI_Error import ErrorGUI
from NT_User_Interface.NT_UI_Node_Connections import NodeConnectionsGui

#function to prevent the window from moving on refresh
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

#Node modifying functions should not be usable untill at least one node is present
def RemoveNode(UI,windowLocation,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to remove")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        RemoveNodeGui(windowLocation,nodes)

def ModifyNode(UI,windowLocation,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to modify")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        ModifyNodeGui(windowLocation,nodes)

def ModifyNodeConnections(UI,windowLocation,nodes):
    if (len(nodes)<1):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No nodes to modify")
    else:
        UpdateWindowLocation(UI,windowLocation)
        UI.destroy(),
        NodeConnectionsGui(windowLocation,nodes)



#Main user interface for program
def MainGUI(windowLocation,nodes):    #Tkinter GUI

    #Create instance of GUI class
    UI = tk.Tk()
    #Set window location based on starting/updated position
    UI.geometry("+"+str(windowLocation[0])+"+"+str(windowLocation[1]))

    #Configure Windows
    UI.title('Node-tool')

    #List of the node names that exist in the list, used to display information to the user
    nodeList = []
    
    #varible used to set the amount of columns used by the UI, used for formatting purposes
    totalColums = 6

    #Information regarding network is displayed to the user in the primary UI
    UI.nodeListHeadder = tk.Label(UI, text="Current Nodes")
    UI.nodeListHeadder.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)

    for node in nodes:
        nodeList.append(node.name)
    if (len(nodeList) ==0):
        nodeList = "No nodes have been created"

    UI.nodeList = tk.Label(UI, text=str(nodeList))
    UI.nodeList.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)

    buttonWidth = 20

    #Buttons that trigger the various functions of the app
    UI.button = tk.Button(UI,width=buttonWidth , text="Add Node", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                               UI.destroy(),
                                                               AddNodeGui(windowLocation,nodes)))
    UI.button.grid(row = 3, column = 0,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth , text="Remove Node", command=lambda:RemoveNode(UI,UpdateWindowLocation(UI,windowLocation),nodes))
    UI.button.grid(row = 3, column = 1,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Modify Node", command=lambda:ModifyNode(UI,UpdateWindowLocation(UI,windowLocation),nodes))
    UI.button.grid(row = 3, column = 2,pady = 2)

    UI.button = tk.Button(UI, width=buttonWidth ,text="Change Node Connections", command=lambda:ModifyNodeConnections(UI,UpdateWindowLocation(UI,windowLocation),nodes))
    UI.button.grid(row = 4, column = 0,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Draw Network Graph", command=lambda:DrawGraph(UI,nodes))
    UI.button.grid(row = 4, column = 1,pady = 2)

    UI.button = tk.Button(UI,width=buttonWidth ,text="Close Program", command=lambda:(UpdateWindowLocation(UI,windowLocation),ConfirmClose(windowLocation,UI)))
    UI.button.grid(row = 4, column = 2,pady = 2)