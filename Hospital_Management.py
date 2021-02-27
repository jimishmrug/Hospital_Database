from tkinter import *
import sqlite3
import tkinter.messagebox




con = sqlite3.connect('hospital.db')
c = con.cursor()

class Application:
    def __init__(self,master):
        self.master = master

        self.heading = Label(self.master, text="ABC Hospital", font=("Ariel 40 bold"), bg = "steel blue").place(x=200,y=0)
        self.name = Label(self.master, text="Name", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=80)
        self.age = Label(self.master, text="Age", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=130)
        self.gender = Label(self.master, text="Gender", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=180)
        self.mobno = Label(self.master, text="Mobile Number", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=230)
        self.address = Label(self.master, text="Address", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=280)
        self.disease = Label(self.master, text="Disease", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=330)
        self.symptoms = Label(self.master, text="Symptoms", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=380)
        self.medicalhistory = Label(self.master, text="Medical History", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=430)

        self.name_ent = Entry(self.master, width=50)
        self.name_ent.place(x=250,y=80)
        self.age_ent = Entry(self.master, width=50)
        self.age_ent.place(x=250,y=130)
        self.gender_ent = Entry(self.master, width=50)
        self.gender_ent.place(x=250,y=180)
        self.mobno_ent = Entry(self.master, width=50)
        self.mobno_ent.place(x=250,y=230)
        self.address_ent = Entry(self.master, width=50)
        self.address_ent.place(x=250,y=280)
        self.disease_ent = Entry(self.master, width=50)
        self.disease_ent.place(x=250,y=330)
        self.symptoms_ent = Entry(self.master, width=50)
        self.symptoms_ent.place(x=250,y=380)
        self.medicalhistory_ent = Entry(self.master, width=50)
        self.medicalhistory_ent.place(x=250,y=430)

        self.submit = Button(self.master, text="Add", font=("Ariel 20 bold"), command=self.add_patient).place(x=400,y=500)

    def add_patient(self):
        self.name1 = self.name_ent.get()
        self.age1 = self.age_ent.get()
        self.gender1 = self.gender_ent.get()    
        self.mobno1 = self.mobno_ent.get()    
        self.address1 = self.address_ent.get()    
        self.disease1 = self.disease_ent.get()     
        self.symptoms1 = self.symptoms_ent.get()    
        self.medicalhistory1 = self.medicalhistory_ent.get() 
            
        if (self.name1=='' or self.age1=='' or self.gender=='' or len(self.mobno1)!=10 or self.address1=='' or self.disease1=='' or self.symptoms1=='') :   
            tkinter.messagebox.showinfo("Error","Please enter all the details")
        else :
            c.execute("INSERT INTO patient_details VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.name1, self.age1, self.gender1, self.mobno1, self.address1, self.disease1, self.symptoms1, self.medicalhistory1))
            con.commit()
            self.done = Label(self.master, text="Details stored in the Database Successfully", font=("Ariel 20 bold"), bg = "steel blue").place(x=150,y=580)

root = Tk()
b = Application(root)

root.geometry('800x800')

root.configure(bg = "Steel Blue")

root.mainloop()

