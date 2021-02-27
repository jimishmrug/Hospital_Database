from tkinter import *
import sqlite3

conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()
def update():
    class Application:
        def __init__(self,master):
            self.master = master

            self.heading = Label(self.master, text="ABC Hospital", font=("Ariel 40 bold"), bg = "steel blue").place(x=200,y=0)
            self.name = Label(self.master, text="Name", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=80)
            
            self.name_ent = Entry(self.master, width=50)
            self.name_ent.place(x=250,y=80)
        
            self.submit = Button(self.master, text="Search", font=("Ariel 20 bold"), command=self.update).place(x=300,y=200)

        def update(self):
            
            self.disease = Label(self.master, text="Disease", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=130)
            self.symptoms = Label(self.master, text="Symptoms", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=180)
            self.medicalhistory = Label(self.master, text="Medical History", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=230)


            self.disease_ent = Entry(self.master, width=50)
            self.disease_ent.place(x=250,y=130)
            self.symptoms_ent = Entry(self.master, width=50)
            self.symptoms_ent.place(x=250,y=180)
            self.medicalhistory_ent = Entry(self.master, width=50)
            self.medicalhistory_ent.place(x=250,y=230) 

            
                
            self.button4 = Button(self.master, text = 'Update', font=("Ariel 20 bold"), command = self.change).place(x=400,y=300)

        def change(self):
            self.name1= self.name_ent.get()
            self.disease1 = self.disease_ent.get()     
            self.symptoms1 = self.symptoms_ent.get()    
            self.medicalhistory1 = self.medicalhistory_ent.get()

            if (self.disease1!=''):
                cursor.execute("UPDATE Patient_details SET disease= ? WHERE name=?", (self.disease1,self.name1)).fetchall()
                conn.commit()
            else:
                None    
            if (self.symptoms1!=''):
                cursor.execute("UPDATE Patient_details SET symptoms= ? WHERE name=?", (self.symptoms1,self.name1)).fetchall()
                conn.commit()
            else:
                None    
            if (self.medicalhistory1!=''):
                cursor.execute("UPDATE Patient_details SET medicalhistory= ? WHERE name=?", (self.medicalhistory1,self.name1)).fetchall()
                conn.commit()
            else:
                None

            self.done = Label(self.master, text="Details Updated Successfully", font=("Ariel 20 bold"), bg = "steel blue").place(x=250,y=350)   
            
    root = Tk()
    b = Application(root)

    root.geometry('800x800')

    root.configure(bg = "Steel Blue")

    root.mainloop()

