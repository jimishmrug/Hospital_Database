from tkinter import *


class Application:
    def __init__(self,master):
        self.master = master

        self.heading = Label(self.master, text="ABC Hospital", font=("Ariel 40 bold"), bg = "steel blue").place(x=200,y=0)
        self.name = Label(self.master, text="Name", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=80)
        self.age = Label(self.master, text="Age", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=160)
        self.gender = Label(self.master, text="Gender", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=240)
        self.mobno = Label(self.master, text="Mobile Number", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=320)
        self.address = Label(self.master, text="Address", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=400)
        self.disease = Label(self.master, text="Disease", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=480)
        self.symptomps = Label(self.master, text="Symptoms", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=560)
        self.medicalhistory = Label(self.master, text="Medical History", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=630)

        self.name_ent = Entry(self.master, width=50)
        self.name_ent.place(x=250,y=80)
        self.age_ent = Entry(self.master, width=50)
        self.age_ent.place(x=250,y=160)
        self.gender_ent = Entry(self.master, width=50)
        self.gender_ent.place(x=250,y=240)
        self.mobno_ent = Entry(self.master, width=50)
        self.mobno_ent.place(x=250,y=320)
        self.address_ent = Entry(self.master, width=50)
        self.address_ent.place(x=250,y=400)
        self.disease_ent = Entry(self.master, width=50)
        self.disease_ent.place(x=250,y=480)
        self.symptomps_ent = Entry(self.master, width=50)
        self.symptomps_ent.place(x=250,y=560)
        self.medicalhistory_ent = Entry(self.master, width=50)
        self.medicalhistory_ent.place(x=250,y=630)

        self.submit = Button(self.master, text="Add", font=("Ariel 20 bold")).place(x=400,y=700)


root = Tk()
b = Application(root)

root.geometry('800x800')

root.configure(bg = "Steel Blue")

root.mainloop()
