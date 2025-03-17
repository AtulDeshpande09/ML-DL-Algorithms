from tkinter import *
import json
import requests
url = 'http://127.0.0.1:5000'
class UserInterface:
    def __init__(self):
        window = Tk()
        window.title("House Price")

        #left side labels ie column = 1
        Label(window,text="Bedrooms : ").grid(row=1,column=1,sticky=W)
        Label(window,text="Bathrooms : ").grid(row=2,column=1,sticky=W)
        Label(window,text="SQFT_Living : ").grid(row=3,column=1,sticky=W)
        Label(window,text="Age of House : ").grid(row=4,column=1,sticky=W)
        Label(window,text="Expected Value : ").grid(row=5,column=1,sticky=W)

        # take inputs
        self.bedroomVar = StringVar()
        Entry(window,textvariable=self.bedroomVar , justify =RIGHT).grid(row=1,column=2)

        self.bathroomVar = StringVar()
        Entry(window, textvariable= self.bathroomVar,justify=RIGHT).grid(row=2,column=2)

        self.sqftLiving = StringVar()
        Entry(window,textvariable=self.sqftLiving,justify=RIGHT).grid(row=3,column=2)

        self.Ageofhouse = StringVar()
        Entry(window,textvariable = self.Ageofhouse ,justify=RIGHT).grid(row=4,column=2)

        # Variable for prediction
        self.prediction = StringVar()
        lblPred = Label(window, textvariable=self.prediction).grid(row=5,column=2,sticky=E)

        btPred= Button(window,text= 'Get Prediction' , command=self.get_prediction).grid(row=6,column=2)

        window.mainloop()

    def get_prediction(self):

        data = {'bedrooms' : int(self.bedroomVar.get()),'bathrooms': int(self.bathroomVar.get()),'sqft_living' :int(self.sqftLiving.get()) ,'age_of_house':int(self.Ageofhouse.get())}
        
        response = requests.post(f'{url}/predict',json= data)
        result = response.json()['prediction']
        self.prediction.set(format(result, '10.2f'))
UserInterface()
