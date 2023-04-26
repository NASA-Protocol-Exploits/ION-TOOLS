#import libraies
from tkinter import ttk
import tkinter as tk
import NT_User_Interface.NT_UI_Main

#function to prevent the window from moving on refresh
def UpdateWindowLocation(UI,windowLocation):
    windowLocation[0],windowLocation[1]=UI.winfo_x(),UI.winfo_y()

#Define a function to close the window with confirmation window
def RemoveNodeGui(windowLocation,nodes):
    #Create Higher level Window
    removeNodeWindow = tk.Toplevel()
    windowX = str(windowLocation[0])
    windowY = str(windowLocation[1])
    removeNodeWindow.geometry("300x80"+"+"+windowX+"+"+windowY)
    removeNodeWindow.title('Remove Node')
    windowMessage = tk.Label(removeNodeWindow,text = "Choose Node to remove")
    windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    combo = ttk.Combobox(removeNodeWindow,state="readonly",values = nodeList)
    combo.pack()

    def RemoveNode(nodes,nodeName):
        for node in nodes:
            if(node.name==nodeName):
                nodes.remove(node)
                break

    deleteButton = tk.Button(removeNodeWindow, width=20 ,text="Delete", command=lambda:(RemoveNode(nodes,combo.get()),
                                                                                        UpdateWindowLocation(removeNodeWindow,windowLocation),
                                                                                        removeNodeWindow.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    deleteButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(removeNodeWindow, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(removeNodeWindow,windowLocation),
                                                                                        removeNodeWindow.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    cancelButton.pack(side=tk.LEFT)