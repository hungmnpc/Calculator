from tkinter import *
from _standard import Standard
from _equation import Equation
import constBase


class App:
    def __init__(self):
        self.window = Tk()
        self.configWindow()
        self.frameStandard = Standard(self.window)
        self.frameEquation = Equation(self.window)
        self.frameStandard.pack()
        self.createMenu()

    def configWindow(self):
        self.window.resizable(0, 0)
        self.window.geometry(str(constBase.SCREENWIDTH) +
                             'x' + str(constBase.SCREENHEIGHT))
        self.window.title('Calculator')

    def createMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        submenu = Menu(menubar)
        menubar.add_cascade(label="Menu", menu=submenu)
        submenu.add_command(label="Standard", command=self.clickStandard)
        submenu.add_command(label="Equation", command=self.clickEquation)

    def clickStandard(self):
        self.frameEquation.unpack()
        self.frameStandard.pack()

    def clickEquation(self):
        self.frameStandard.unpack()
        self.frameEquation.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
