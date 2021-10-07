import tkinter as tk
from selectPage import SelectPage
from vars import Vars

class HomePage(SelectPage):
    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        label = tk.Label(self, text = "Runoff & Drought Estimation Tool ", font = Vars.LARGE_FONT,bg='cyan')
        label.place(x =100,y=100,w=800)
        
        description="The hydrological cycle has many interconnected components, with runoff connecting precipitation to bodies of water.\
                    Surface runoff is precipitation that does not infiltrate into the soil and runs across the land surface into surface waters (streams, rivers, lakes or other reservoirs).\
                    Surface runoff varies by time and location, with about one-third of the precipitation \
                    that falls on land turning into runoff; the other two-thirds is evaporated, transpired, or infiltrated into the soil.\
                    By returning excess precipitation to the oceans and controlling how much\
                    water flows into stream systems, runoff is important in balancing the hydrological cycle.\
                    Runoff models visualize what occurs in water systems due to changes in pervious surfaces, vegetation, and meteorological events.\
                    The main goal of our too is to automate the process of Rainfall-Runoff , we present the following techniques\n \
                    1. Support Vector Machines\n \
                    2. Linear Regression\n \
                    3. Random Forest\n  \
                    4. Decision Tree\n \
                    5. Gradient Boost\n \n    \
                    Apart from this we also have modelled Drought Index , using SPI and SPIE\
                    which analyses the precipitation and temperature accross the time\ "
                
        msg = tk.Message(self,text = description,justify=tk.LEFT)
        msg.config(bg='white', font=Vars.SMALL_FONT)
        msg.place(x=300,y=200)
