from tkinter import *
import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
 
window = Tk()
window.geometry('800x800')
window.title('Data Entry')

 
def exportdata():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()
    g = e7.get()
    h = e8.get()
    i = e9.get()
    j = e10.get()
    k = e11.get()
    l = e12.get()

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print(j)
    print(k)
    print(l)
    
    data = {}
    data['CORSOrigins'] = a
    data['AllowedHosts'] = b
    data['Name'] = c
    data['OpenApiTitle'] = d 
    data['OpenApiVersion'] = e
    data['TermsOfSerOAvice'] = f
    data['OpenApiDesc'] = g
    data['OpenApiContactEmail'] = h
    data['OpenApiContactName'] = i
    data['OpenApiContactUrl'] = j
    data['OpenApiLicenseName'] = k
    data['OpenApiLicenseUrl'] = l

    files = [('JSON File', '*.json')]
    fileName='reimsdata'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='reimsdata')
    writeToJSONFile(filepos, fileName, data)
 
 
s1= Label(window, text="CORSOrigins :")
e1 = Entry(window,width=50)
e1.insert(END,'http://aimdev.ril.com,http://rpmg1dev.ril.com,http://aimapilocal.ril.com:4200,http://ridelocal.ril.com:4200,http://aimdev1.ril.com,*')
print("\n")
s2 = Label(window, text="AllowedHosts :")
e2 = Entry(window)
e2.insert(END,'*')
s3 = Label(window, text="Name :")
e3 = Entry(window)
e3.insert(END,'datamodel')
s4 = Label(window, text="OpenApiTitle :")
e4 = Entry(window)
e4.insert(END,'AIMAPI_NC_RCowServiceIntegration')
s5 = Label(window, text="OpenApiVersion :")
e5 = Entry(window)
e5.insert(END,'1.0.0')
s6 = Label(window, text="TermsOfSerOAvice :")
e6 = Entry(window)
e6.insert(END,'http://ril.com')
s7 = Label(window, text="OpenApiDesc :")
e7 = Entry(window)
e7.insert(END,'Api description')
s8 = Label(window, text="OpenApiContactEmail :")
e8 = Entry(window)
e8.insert(END,'rikun.patel@ril.com')
s9 = Label(window, text="OpenApiContactName :")
e9 = Entry(window)
e9.insert(END,'Rikun Patel')
s10 = Label(window, text="OpenApiContactUrl :")
e10 = Entry(window)
e10.insert(END,'http://ril.com')
s11 = Label(window, text="OpenApiLicenseName :")
e11 = Entry(window)
e11.insert(END,'Apache License Version 2.0')
s12 = Label(window, text="OpenApiLicenseUrl :")
e12 = Entry(window)
e12.insert(END,'http://www.apache.org/licenses/LICENSE-2.0')

submit = Button(window,text='Submit',command = exportdata).grid(row=20, column=1)
 
 
test = 1
def writeToJSONFile(path, fileName, data):
        json.dump(data, path)
 
path = './'
 
 
s1.grid(row=0, column=0)
s2.grid(row=1,column=0)
s3.grid(row=2,column=0)
s4.grid(row=3,column=0)
s5.grid(row=4,column=0)
s6.grid(row=5,column=0)
s7.grid(row=6,column=0)
s8.grid(row=7,column=0)
s9.grid(row=8,column=0)
s10.grid(row=9,column=0)
s11.grid(row=10,column=0)
s12.grid(row=11,column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
e8.grid(row=7,column=1)
e9.grid(row=8,column=1)
e10.grid(row=9,column=1)
e11.grid(row=10,column=1)
e12.grid(row=11,column=1) 

 
mainloop()