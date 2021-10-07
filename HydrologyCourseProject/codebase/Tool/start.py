import tkinter as tk

from homePage import HomePage
from task_One import SupportVectorMachine
from task_Two import LinearRegression
from task_Three import NeuralNet
from task_Four import  DecisionTree
from task_Five import GradientBoost
from task_Six import BoxPlotAnalysis
from task_Seven import GLDAS
from task_Eight import DroughtIndex

from selectPage import SelectPage

LARGE_FONT = ("Verdana", 40)
LABEL_FONT = ("Verdana", 15)

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        self.wm_title("Runoff & Drought Modelling Tool ")
        self.geometry("1550x800")
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for Frame in (HomePage,SupportVectorMachine,LinearRegression,NeuralNet,DecisionTree,GradientBoost,BoxPlotAnalysis,DroughtIndex,GLDAS):            
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomePage)    


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


if __name__=='__main__':
    app =App()
    app.mainloop()