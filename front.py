import webscraper
import analyser
import match
def act():
        try:
                print("EXECUTING>>>>")
                webscraper.webscr(str(svalue.get()))
                analyser.analyse()
                my_msg.set("Scraping done!")
        except:
                my_msg.set("Enter valid URL!")
def search():
        match.mch(str(search_value.get()))
from tkinter import *
root = Tk(className ="webscraper")
svalue = StringVar()
my_msg = StringVar()
search_value = StringVar()
my_msg.set("")
w = Entry(root,textvariable=svalue,width=40) # adds a textarea widget
w.pack()
foo = Button(root,text="Enter URL", command=act)
foo.pack()
label1 = Label(root, textvariable=my_msg)
label1.pack()
labelx = Label(root)
labelx.pack()
labely = Label(root)
labely.pack()
et = Entry(root,textvariable=search_value,width=40)
et.pack()
fo1 = Button(root,text="Search", command=search)
fo1.pack()
root.mainloop()
