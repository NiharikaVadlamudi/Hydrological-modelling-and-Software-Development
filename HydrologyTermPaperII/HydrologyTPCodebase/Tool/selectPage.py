import tkinter as tk
import pandas as pd
from vars import Vars



class SelectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background = '#D6E9D2')
        self.initUI(parent, controller)

    def initUI(self, parent, controller):
        
        from homePage import HomePage
        from task_One import SupportVectorMachine
        from task_Two import LinearRegression
        from task_Three import NeuralNet
        from task_Four import DecisionTree
        from task_Five import GradientBoost

        
        HomeButton = self.customButton(text = "Home", 
        command =  lambda: controller.show_frame(HomePage))
        HomeButton.place(x = 10, y = 10, width = 100, height = 35)

       
        TaskOneButton = self.customButton(text = "SVM", 
        command =  lambda: controller.show_frame(SupportVectorMachine))
        TaskOneButton.place(x =120, y = 10, width = 100, height = 35)

        TaskTwoButton = self.customButton(text = "Linear Regression", 
        command =  lambda: controller.show_frame(LinearRegression))
        TaskTwoButton.place(x =230, y = 10, width = 200, height = 35)

        TaskThreeButton = self.customButton(text = "Neural Network", 
        command =  lambda: controller.show_frame(NeuralNet))
        TaskThreeButton.place(x =450, y = 10, width = 200, height = 35)


        TaskFourButton = self.customButton(text = "Decision Tree", 
        command =  lambda: controller.show_frame(DecisionTree))
        TaskFourButton.place(x =660, y = 10, width = 140, height = 35)

        TaskFiveButton = self.customButton(text = "Gradient Boost", 
        command =  lambda: controller.show_frame(GradientBoost))
        TaskFiveButton.place(x =820, y = 10, width = 160, height = 35)



    def customButton(self, text, command):
        return tk.Button(self, text = text, 
        command =  command, 
        padx = 10,
        pady = 10)
