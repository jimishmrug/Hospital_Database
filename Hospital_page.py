from tkinter import *
from Hospital_Management import *
from Search_report import *
from update import *

class App:
     def __init__(self,master):
          self.master = master
          self.heading = Label(master, text="ABC Hospital", font="Ariel 50 bold", bg = "steel blue").place(x=200,y=0)
          self.button1 = Button(master, text="Add A patient", command=call_for_add, width=20).place(x=100,y=200)
          self.button2 = Button(master, text = "Search for patient", width = 20, command=search).place(x=300,y=200)
          self.button3 = Button(master, text = "Update patient info", width = 20, command= update).place(x=500,y=200)

root1 = Tk()
root1.geometry('800x800')
root1.configure(bg="Steel Blue")
App(root1)


root1.mainloop()
