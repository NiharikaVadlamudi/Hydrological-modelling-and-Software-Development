import tkinter as tk
from selectPage import SelectPage
from vars import Vars

class HomePage(SelectPage):
    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        label = tk.Label(self, text = "Flood Prediction via Machine Learning Algorithms", font = Vars.LARGE_FONT,bg='cyan')
        label.place(x =100,y=100,w=800)

        description="Floods are amongst the most frequent and destructive types of disaster, causing significant damage anddisrupting livelihoods throughout the world.There is a wide range of flood risk management methods available  that  can  reduce  this  destruction,  and  managing  flood  risks\n There is requirement of   estimation  of  flood hazards  and its impact\n Proper  estimation  of  risk  is  challenging  and  requirescareful consideration of a number of factors,including watershed properties such as size, topography andland use, the types and characteristics of storms that produce rainfall and flooding in the region, andthe number, location, and types of buildings and other assets that could be damaged\n. Well-conducted flood hazard and risk assessments,on the other hand, can provide valuable support for a range of decisions such as land-use master planning,design of infrastructure, and emergency response preparation\n.Here, in this tool we aim to predict the river runoff using Machine Learning Techniques!"
        msg = tk.Message(self,text = description,justify=tk.CENTER)
        msg.config(bg='white', font=Vars.SMALL_FONT)
        msg.place(x=300,y=200)



