from tkinter import * 
import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

def search():
	root1 = Tk()
	root1.geometry('800x500')

	root1.configure(bg = "Steel Blue")

	def call():
		patient_accessing = name_ent.get()
		rows = cursor.execute("SELECT name , age , gender , mobno , address , disease , symptoms , medicalhistory   FROM  patient_details  WHERE name = ? ", (patient_accessing ,)).fetchall()
		for i in rows :
			name_value = i[0]
			age_value  = i[1]
			gender_value = i[2]
			mobno_value  = i[3]
			address_value = i[4]
			disease_value = i[5]
			symptoms_value = i[6]
			medicalhistory_value = i[7]



		def report (name_value, age_value, gender_value, mobno_value, address_value, disease_value, symptoms_value, medicalhistory_value):
			
			root = Tk()
			root.geometry('800x800')

			root.configure(bg = "Steel Blue")
		
			report = Label ( root , text = "Report" ,  font=("Ariel 30 bold underline"), bg = "steel blue").place(x = 0,y = 70)

			heading = Label(root, text="ABC Hospital", font=("Ariel 40 bold underline"), bg = "steel blue").place(x=250,y=0)
			name = Label(root, text="Name", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=150)
			age = Label(root, text="Age", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=230)
			gender = Label(root, text="Gender", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=310)
			mobno = Label(root, text="Mobile Number", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=390)
			address = Label(root, text="Address", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=470)
			disease = Label(root, text="Disease", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=550)
			symptomps = Label(root, text="Symptoms", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=630)
			medicalhistory = Label(root, text="Medical History", font=("Ariel 20 bold"), bg = "steel blue").place(x=0,y=710)


			name_value1 = Label(root, text=name_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=150)
			age_value1 = Label(root, text=age_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=230)
			gender_value1 = Label(root, text=gender_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=310)
			mobno_value1 = Label(root, text=mobno_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=390)
			address_value1 = Label(root, text=address_value ,  font=("Verdana 15"), bg = "steel blue").place(x=300,y=470)
			disease_value1 = Label(root, text=disease_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=550)
			symptoms_value1 = Label(root, text=symptoms_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=630)
			medicalhistory_value1 = Label(root, text=medicalhistory_value, font=("Verdana 15"), bg = "steel blue").place(x=300,y=710)

			root.mainloop()

		report(name_value, age_value, gender_value, mobno_value, address_value, disease_value, symptoms_value, medicalhistory_value)

	heading = Label(root1 , text="ABC Hospital", font=("Ariel 30 bold underline"), bg = "steel blue").place(x=200,y=0)
	patient_accessing1 = Label(root1, text="enter the name of the patient ?", font=("Verdana 15"), bg = "steel blue").place(x=0,y=250)
	name_ent = Entry(root1, width=50)
	name_ent.place(x=340,y=260)

	search = Button(root1, text="Submit", width = 30, command= call)
	search.place(x=200, y=350)



	root1.mainloop()