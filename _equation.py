import tkinter as tk
import constBase
import math


class Equation(object):

    def __init__(self, root):
        self.window = root
        self.mainFrame = self.createMainFrame()
        self.buttonFrame = self.createButtonFrame()
        self.displayFrame = self.createDisplayFrame()
        self.digits = constBase.DIGITS
        self.operation = constBase.OPERATION
        self.configButtonFrame()
        self.createButton()
        self.state = {
            "currentEquation": constBase.QUADRATIC_EQUATION,
        }
        self.equationLabel = self.createEquationLabel()
        self.display1 = self.createDisplay1()
        self.display2 = self.createDisplay2()
        self.configDisplay1()
        self.configDisplay2()

        self.coefficientList = []
        self.calExpression = []
        self.expressionLabel, self.total = self.createExpressionLabel()

    def createMainFrame(self):
        frame = tk.Frame(self.window, bg="red")
        return frame

    def createButtonFrame(self):
        frame = tk.Frame(
            self.mainFrame, height=constBase.BUTTONS_FRAME_HEIGHT, bg="blue")
        frame.grid_propagate(0)
        frame.pack(expand=True, fill="both", side=tk.BOTTOM)
        return frame

    def createButton(self):
        self.createDigitButton()
        self.createClearButton()
        self.createEqualButton()
        self.createBackSpaceButton()
        self.createEquationToggle()
        self.createOperationButton()
        self.createSomeSpecialOperationButtons()

    def configButtonFrame(self):
        for x in range(0, 4):
            self.buttonFrame.columnconfigure(x, weight=1, uniform='third')
        for x in range(0, 6):
            self.buttonFrame.rowconfigure(x, weight=1, uniform='third')

    def createDigitButton(self):
        for digit, grid_position in self.digits.items():
            button = tk.Button(self.buttonFrame, text=str(digit), bg=constBase.WHITE, fg=constBase.LABEL_COLOR,
                               borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
            button.grid(row=grid_position[0] + 2,
                        column=grid_position[1], sticky=tk.NSEW)

    def createClearButton(self):
        buttonClear = tk.Button(self.buttonFrame, text='C', bg=constBase.LIGHT_RED, fg=constBase.LABEL_COLOR,
                                borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        buttonClear.grid(row=0, column=2, sticky=tk.NSEW)

    def createBackSpaceButton(self):
        buttonBS = tk.Button(self.buttonFrame, text="⌫", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR,
                             borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        buttonBS.grid(row=0, column=3, sticky=tk.NSEW)

    def createEqualButton(self):
        buttonEq = tk.Button(self.buttonFrame, text="=", bg=constBase.LIGHT_BLUE, fg=constBase.LABEL_COLOR,
                             borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        buttonEq.grid(row=5, column=3, sticky=tk.NSEW)

    def createSomeSpecialOperationButtons(self):
        button_open_parenthese = tk.Button(
            self.buttonFrame, text="(", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        button_open_parenthese.grid(row=0, column=0, sticky=tk.NSEW)

        button_close_parenthese = tk.Button(self.buttonFrame, text=")", bg=constBase.OFF_WHITE,
                                            fg=constBase.LABEL_COLOR, borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        button_close_parenthese.grid(row=0, column=1, sticky=tk.NSEW)

        button_inverse = tk.Button(
            self.buttonFrame, text="⅟𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        button_inverse.grid(row=1, column=0, sticky=tk.NSEW)

        button_sqr = tk.Button(self.buttonFrame, text="𝓍²",
                               bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        button_sqr.grid(row=1, column=1, sticky=tk.NSEW)

        button_sqrt = tk.Button(
            self.buttonFrame, text="√𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
        button_sqrt.grid(row=1, column=2, sticky=tk.NSEW)

    def createOperationButton(self):
        i = 1
        for operation, text in self.operation.items():
            button = tk.Button(self.buttonFrame, text=text, bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR,
                               borderwidth=0, font=constBase.BUTTON_FONT_STYLE)
            button.grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

    def createEquationToggle(self):
        buttonToggle = tk.Button(self.buttonFrame, text="Tg", bg=constBase.TOGGLE_COLOR, fg=constBase.LABEL_COLOR,
                                 borderwidth=0, font=constBase.BUTTON_FONT_STYLE, command=self.toggleEquation)
        buttonToggle.grid(row=5, column=0, sticky=tk.NSEW)

    def createDisplayFrame(self):
        frame = tk.Frame(
            self.mainFrame, height=constBase.DISPLAY_FRAME_HEIGHT, bg=constBase.COLOR1)
        frame.pack_propagate(0)
        frame.pack(expand=True, fill="both", side=tk.TOP)
        return frame

    def toggleEquation(self):
        self.state["currentEquation"] = constBase.CUBIC_EQUATION if self.state["currentEquation"].id == 2 else constBase.QUADRATIC_EQUATION
        self.configDisplay1()
        self.equationLabelUpdate()

    def createEquationLabel(self):
        label = tk.Label(
            self.displayFrame, text=self.state["currentEquation"].text, bg=constBase.COLOR1)
        label.pack(side=tk.TOP)
        return label

    def equationLabelUpdate(self):
        self.equationLabel.config(text=self.state["currentEquation"].text)

    def createDisplay1(self):
        frame = tk.Frame(self.displayFrame, bg="", height=50)

        frame.pack(expand=True, fill="both", side=tk.TOP)
        frame.grid_propagate(0)

        return frame

    def createDisplay2(self):
        frame = tk.Frame(self.displayFrame, bg="black", height=140)

        frame.pack(expand=True, fill="both", side=tk.BOTTOM)
        frame.grid_propagate(0)

        return frame

    def configDisplay2(self):
        for i in range(0, 3):
            self.display2.rowconfigure(i, weight=1)

        self.display2.columnconfigure(0, weight=1)

    def createExpressionLabel(self):
        label1 = tk.Label(self.display2, text='A', font=constBase.SMALL_FONT_STYLE,
                          fg=constBase.LABEL_COLOR, anchor=tk.E)
        label1.grid(row=0, column=0)
        label = tk.Label(self.display2, text='1', font=constBase.SMALL_FONT_STYLE,
                         fg=constBase.LABEL_COLOR, anchor=tk.E)
        label.grid(row=1, column=0)
        return label1, label

    def destroyDisplay2(self):
        for widgets in self.display2.winfo_children():
            widgets.destroy()

    def configDisplay1(self):

        for widgets in self.display1.winfo_children():
            widgets.grid_forget()

        for i in range(0, 12):
            self.display1.columnconfigure(i, weight=1, uniform='third')

        self.controlDisplay1()

    def controlDisplay1(self):
        data = ["a", "b", "c", "d", "e"]
        n = self.state["currentEquation"].id

        for i in range(0, n + 1):
            self.display1.columnconfigure(i, weight=1, uniform='third')
            label = tk.Label(self.display1, text=data[i], bg=constBase.COLOR1)
            label.grid(row=0, column=math.floor(i * (12 / (n + 1))),
                       columnspan=math.floor(12 / (n + 1)), sticky=tk.NSEW)

    def unpack(self):
        self.mainFrame.pack_forget()

    def pack(self):
        self.mainFrame.pack(expand=True, fill="x")
