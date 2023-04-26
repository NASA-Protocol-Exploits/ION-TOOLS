#import libraies
from re import L
from tkinter import ttk
import tkinter as tk
from xml.dom.minicompat import NodeList
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import NT_User_Interface.NT_UI_Main

from NT_User_Interface.NT_UI_Error import ErrorGUI


def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return windowLocation

class node():
    def __init__(self):
        self.name = ""
        self.IPAddress = []
        self.connectedNodes = []

def AddNode(nodes,node):
    nodes.append(node)

def NodeConstructor():
        return node()

#Define a function to close the window with confirmation window
def ModifyNodeGui(windowLocation,networkMap,nodes,nodeName):
    for node in nodes:
        if( node.name == nodeName):
            targetNode = node
            break    
    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("+"+windowX+"+"+windowY)
    UI.title('Update Node')

    #Node Name Input Section
    totalColums = 7

    UI.windowMessage = tk.Label(UI,text = "Chosen Node")
    UI.windowMessage.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)
    UI.windowMessage = tk.Label(UI,text = targetNode.name)
    UI.windowMessage.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)


    UI.windowMessage3 = tk.Label(UI,text = "Node Name")
    UI.windowMessage3.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)
    nodeName = tk.StringVar(UI, value=str(targetNode.name))
    UI.nodeNameEntry = tk.Entry(UI, textvariable=nodeName, width=20)
    UI.nodeNameEntry.grid(row = 3, columnspan = totalColums, column = 0, pady = 2)



    input_size = 10

    #Ip address Input Section
    UI.IPinputMessage = tk.Label(UI, text="IP address for node")
    UI.IPinputMessage.grid(row = 4, column = 0, columnspan = totalColums, pady = 2)

    oct1 = tk.StringVar(UI, value=str(targetNode.IPAddress[0]))
    UI.IPaddressBit1 = tk.Entry(UI, textvariable=oct1, width=input_size)
    UI.IPaddressBit1.grid(row = 5, column = 0,  pady = 2)

    UI.dot1 = tk.Label(UI,text=".")
    UI.dot1.grid(row = 5, column = 1,  pady = 2)

    oct2 = tk.StringVar(UI, value=str(targetNode.IPAddress[1]))
    UI.IPaddressBit2 = tk.Entry(UI, textvariable=oct2, width=input_size)
    UI.IPaddressBit2.grid(row = 5, column = 2,  pady = 2)

    UI.dot2 = tk.Label(UI,text=".")
    UI.dot2.grid(row = 5, column = 3,  pady = 2)

    oct3 = tk.StringVar(UI, value=str(targetNode.IPAddress[2]))
    UI.IPaddressBit3 = tk.Entry(UI,textvariable=oct3, width=input_size)
    UI.IPaddressBit3.grid(row = 5, column = 4,  pady = 2)

    UI.dot3 = tk.Label(UI,text=".")
    UI.dot3.grid(row = 5, column = 5,  pady = 2)

    oct4 = tk.StringVar(UI, value=str(targetNode.IPAddress[3]))
    UI.IPaddressBit4 = tk.Entry(UI, textvariable=oct4, width=input_size)
    UI.IPaddressBit4.grid(row = 5, column = 6,  pady = 2)

    def inputValdation(UI,nodes):

        nodeList = []
        for node in nodes:
            if(node.name == targetNode.name):
                None
            else:
                nodeList.append(node.name)

        invalid = False
        nodeNameCharacterLimit = 16
        nameInput = UI.nodeNameEntry.get()
        if(len(nameInput)==0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node name not entered")
                return False
            
        for node in nodeList:
            if(node==nameInput):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node "+nameInput+" Allready Exists")
                return False

        if(len(nameInput)>nodeNameCharacterLimit):
            ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Node Name Character limit Exceeded\n Character Limit : "+str(nodeNameCharacterLimit))
            return False
        
        octets = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]

        for octet in octets:
            if(len(octet)==0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"IP address Not entered")
                invalid = True
                break
            elif(not octet.isnumeric()):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"Ip address must only contain numbers")
                invalid = True
                break
            elif(int(octet)>255 or int(octet)<0):
                ErrorGUI(UpdateWindowLocation(UI,windowLocation),"One or more octets are out of range\n Range : 0-255")
                invalid = True
                break

        if(invalid == True):
            return False
        else:
            nodes.remove(targetNode)
            return True

    def CreateNode(UI,nodes):
        if (inputValdation(UI,nodes)):
            octets = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]
            IPaddress = octets
            node = NodeConstructor()
            node.name = UI.nodeNameEntry.get()
            node.IPAddress = IPaddress
            AddNode(nodes,node)
            UpdateWindowLocation(UI,windowLocation)
            UI.destroy()
            NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,networkMap,nodes)

    UI.confirmbutton = tk.Button(UI, width=16, text="Update node", command=lambda:CreateNode(UI,nodes))
    UI.confirmbutton.grid(row = 6, column = 0, columnspan = 3, pady = 2)
    UI.cancelButton = tk.Button(UI, width=16 ,text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                             UI.destroy(),
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,networkMap,nodes)))
    UI.cancelButton.grid(row = 6, column = 4, columnspan = 3, pady = 2)

def CheckIfNullEntry(UI,windowLocation,networkMap,nodes):
    selectedNode = UI.combo.get()
    found = False
    for node in nodes:
        if(node.name == selectedNode):
            found = True
            ModifyNodeGui(UpdateWindowLocation(UI,windowLocation),networkMap,nodes,selectedNode)
            UI.destroy()
            break
    if(not found):
        ErrorGUI(UpdateWindowLocation(UI,windowLocation),"No Node Selected")

#Define a function to close the window with confirmation window
def UpdateNodeGui(windowLocation,networkMap,nodes):
    #Create Higher level Window
    UI = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    UI.geometry("300x80"+"+"+windowX+"+"+windowY)
    UI.title('Update Node')
    UI.windowMessage = tk.Label(UI,text = "Choose Node to Update")
    UI.windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    UI.combo = ttk.Combobox(UI,state="readonly",values = nodeList)
    UI.combo.pack()

    configureButton = tk.Button(UI, width=20 ,text="Update", command=lambda:CheckIfNullEntry(UI,windowLocation,networkMap,nodes))
    configureButton.pack(side=tk.LEFT)

    cancelButton = tk.Button(UI, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(UI,windowLocation),
                                                                                        UI.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,networkMap,nodes)))
    cancelButton.pack(side=tk.LEFT)