from tkinter import *
import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
 
window = Tk()
window.geometry('540x300')
window.title('Data Entry')

 
def exportdata():
    a = Reims_data1.get()
    b = Reims_data2.get()
    c = Reims_data3.get()
    print(a)
    print(b)
    print(c)
    data = {}
    data['reims_data1'] = a
    data['reims_data2'] = b
    data['reims_data3'] = c
    files = [('JSON File', '*.json')]
    fileName='reimsdata'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='reimsdata')
    writeToJSONFile(filepos, fileName, data)
 
 
reims_data1 = Label(window, text="reims_data1:")
Reims_data1 = Entry(window)
reims_data2 = Label(window, text="reims_data2:")
Reims_data2 = Entry(window)
reims_data3 = Label(window, text="reims_data3:")
Reims_data3 = Entry(window)
submit = Button(window,text='Submit',command = exportdata).grid(row=3, column=1)
 
 
test = 1
def writeToJSONFile(path, fileName, data):
        json.dump(data, path)
 
path = './'
 
 
reims_data1.grid(row=0, column=0)
reims_data2.grid(row=1,column=0)
reims_data3.grid(row=2,column=0)
Reims_data1.grid(row=0, column=1)
Reims_data2.grid(row=1, column=1)
Reims_data3.grid(row=2, column=1)
 
 
mainloop()