import tkinter as tk
import tkinter.font as font
import constBase
import math


class Standard:
    def __init__(self, root):
        self.window = root
        self.mainFrame = self.createMainFrame()
        self.total_expression = ''
        self.current_expression = []
        self.cal_expression = []
        self.digits = constBase.DIGITS
        self.operation = constBase.OPERATION

        self.display_frame = self.createDisplayFrame()
        self.current_label, self.total_label = self.createDisplayLabels()
        self.buttons_frame = self.createButtonsFrame()
        self.configButton()
        self.createDigitsButton()
        self.createOperationButtons()
        self.createSpecialButton()
        self.answer = ''
        self.state = 0

    # _________Create Frame Layout____________________________

    def createMainFrame(self):
        frame = tk.Frame(self.window)
        return frame

    def createDisplayFrame(self):
        frame = tk.Frame(self.mainFrame, height=constBase.DISPLAY_FRAME_HEIGHT)
        frame.pack(expand=True, fill="both")
        frame.pack_propagate(0)
        return frame

    def createButtonsFrame(self):
        frame = tk.Frame(
            self.mainFrame, height=constBase.BUTTONS_FRAME_HEIGHT, bg="blue")
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(0)
        return frame
    # __________________________________________________________

    # _____________Create Label__________________________________
    def createDisplayLabels(self):
        current_label = tk.Label(self.display_frame, text=''.join(self.total_expression),
                                 font=constBase.SMALL_FONT_STYLE, fg=constBase.LABEL_COLOR, anchor=tk.E)
        current_label.pack(expand=1, fill="both", side=tk.TOP)

        total_label = tk.Label(self.display_frame, text=''.join(self.current_expression),
                               font=constBase.LARGE_FONT_STYLE, fg=constBase.LABEL_COLOR, anchor=tk.E, height=10, bg=constBase.DiSPLAY_COLOR, width=200)
        total_label.pack(expand=1, fill="both", side=tk.BOTTOM)
        total_label.pack_propagate(0)

        return current_label, total_label
    # ____________________________________________________________

    # ___________________________Create Button__________________________________

    def createOperationButtons(self):
        i = 1
        for operator, symbol in self.operation.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0,
                               command=lambda symbol_label=operator: self.addValueLabel(symbol_label))
            button.grid(row=i, column=3, sticky=tk.NSEW)
            button['font'] = font.Font(size=17)
            i += 1

    def createEqualButton(self):
        button = tk.Button(self.buttons_frame, text="=", bg=constBase.LIGHT_BLUE,
                           fg=constBase.LABEL_COLOR, borderwidth=0, command=self.equalButtonClick)
        button.grid(row=5, column=3, sticky=tk.NSEW)
        button['font'] = font.Font(size=17)

    def createSomeSpecialOperationButton(self):
        button_open_parenthese = tk.Button(
            self.buttons_frame, text="(", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0,
            command=lambda symbol_label="(": self.addValueLabel(symbol_label))
        button_open_parenthese.grid(row=0, column=0, sticky=tk.NSEW)
        button_open_parenthese['font'] = font.Font(size=17)

        button_close_parenthese = tk.Button(self.buttons_frame, text=")", bg=constBase.OFF_WHITE,
                                            fg=constBase.LABEL_COLOR, borderwidth=0,
                                            command=lambda symbol_label=")": self.addValueLabel(symbol_label))
        button_close_parenthese.grid(row=0, column=1, sticky=tk.NSEW)
        button_close_parenthese['font'] = font.Font(size=17)

        button_inverse = tk.Button(
            self.buttons_frame, text="⅟𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clickInverse)
        button_inverse.grid(row=1, column=0, sticky=tk.NSEW)
        button_inverse['font'] = font.Font(size=17)

        button_sqr = tk.Button(self.buttons_frame, text="𝓍²",
                               bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clickSqr)
        button_sqr.grid(row=1, column=1, sticky=tk.NSEW)
        button_sqr['font'] = font.Font(size=17)

        button_sqrt = tk.Button(
            self.buttons_frame, text="√𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clickSqrt)
        button_sqrt.grid(row=1, column=2, sticky=tk.NSEW)
        button_sqrt['font'] = font.Font(size=17)

    def createClearButton(self):
        button_clear_all = tk.Button(self.buttons_frame, text="C", bg=constBase.LIGHT_RED,
                                     fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clearAllDisplay)
        button_clear_all.grid(row=0, column=2, sticky=tk.NSEW)
        button_clear_all['font'] = font.Font(size=17)

        button_backspace = tk.Button(self.buttons_frame, text="⌫", bg=constBase.OFF_WHITE,
                                     fg=constBase.LABEL_COLOR, borderwidth=0, command=lambda: self.backSpace())
        button_backspace.grid(row=0, column=3, sticky=tk.NSEW)
        button_backspace['font'] = font.Font(size=17)

    def createDigitsButton(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=constBase.WHITE, fg=constBase.LABEL_COLOR,
                               borderwidth=0, font=constBase.FONT, command=lambda x=digit: self.addValueLabel(x))
            button.grid(row=grid_value[0]+2,
                        column=grid_value[1], sticky=tk.NSEW)
            button['font'] = font.Font(size=17)

    def createAnsButton(self):
        button = tk.Button(self.buttons_frame, text="Ans", bg=constBase.WHITE,
                           fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clickAnsBt)
        button.grid(row=5, column=0, sticky=tk.NSEW)
        button['font'] = font.Font(size=17)

    def createSpecialButton(self):
        self.createEqualButton()
        self.createAnsButton()
        self.createClearButton()
        self.createSomeSpecialOperationButton()

    # _____________________________________________________________________

    # _________________________Update Screen_______________________________

    def updateTotalLabel(self):
        x = len(self.total_expression)

        if (x > 24):
            self.total_expression = constBase.MEM_ERROR_TEXT
            self.total_label.config(
                text=self.total_expression, font=("Arial", 16, "bold"))
            self.total_expression = ''
            return
        x = len(self.total_expression)
        fontSize = constBase.FONT_SIZE_TOTAL if x < 12 else int((
            12 / x) * constBase.FONT_SIZE_TOTAL)

        fontSize = 17 if fontSize <= 16 else fontSize
        self.total_label.config(
            text=self.total_expression, font=("Arial", fontSize, "bold"))

    def updateCurrentLabel(self):
        self.current_label.config(text=''.join(self.current_expression))

    # _____________________________________________________________________

    def configButton(self):
        for x in range(0, 4):
            self.buttons_frame.columnconfigure(x, weight=1, uniform='third')
        for x in range(0, 6):
            self.buttons_frame.rowconfigure(x, weight=1, uniform='third')

    # _______________________Handle click button_____________________________

    def addValueLabel(self, value):
        if(self.state == 1):
            self.current_expression.clear()

            self.cal_expression.clear()
            x = list(str(self.total_expression))
            for digit in x:
                self.cal_expression.append(str(digit))
                self.current_expression.append(str(digit))
            self.state = 0

        self.current_expression.append(str(value))
        self.cal_expression.append(str(value))
        self.updateCurrentLabel()

    def backSpace(self):
        try:
            self.current_expression.pop()
            self.cal_expression.pop()
        except:
            pass
        self.updateCurrentLabel()

    def clearAllDisplay(self):
        self.total_expression = ''
        self.current_expression.clear()
        self.cal_expression.clear()
        self.updateTotalLabel()
        self.updateCurrentLabel()
        self.state = 0

    def equalButtonClick(self):
        try:
            a = str(eval(''.join(self.cal_expression)))
        except Exception as e:
            if (("math" in str(e)) or ("zero" in str(e))):
                self.total_expression = constBase.MATH_ERROR_TEXT
                self.state = 0
                self.updateTotalLabel()
                return
            else:
                self.total_expression = constBase.SYNTAX_ERROR_TEXT
                self.state = 0
                self.updateTotalLabel()
                return
            pass
        try:
            self.total_expression = a.rstrip('0').rstrip(
                '.') if '.' in a else a
        except:
            pass

        if (self.total_expression == ''):
            self.total_expression = '0'
        self.answer = self.total_expression
        self.updateTotalLabel()

        self.state = 1

    def clickAnsBt(self):
        x = list(self.answer)
        for value in x:
            self.cal_expression.append(str(value))
            self.current_expression.append(str(value))
        self.updateCurrentLabel()

    def clickSqr(self):
        if(self.state == 1):
            self.current_expression.clear()
            self.cal_expression.clear()
            x = list(str(self.total_expression))
            for digit in x:
                self.cal_expression.append(str(digit))
                self.current_expression.append(str(digit))
            self.current_expression.append('^')
            self.cal_expression.append('**')
            self.state = 0
        else:
            self.current_expression.append('^')
            self.cal_expression.append('**')
        self.updateCurrentLabel()

    def clickSqrt(self):
        if(self.state == 1):
            self.current_expression.clear()
            self.current_expression.append('√(')
            self.cal_expression.clear()
            self.cal_expression.append('math.sqrt(')
            x = list(str(self.total_expression))
            for digit in x:
                self.cal_expression.append(str(digit))
                self.current_expression.append(str(digit))
            self.state = 0
        else:
            self.current_expression.append('√(')
            self.cal_expression.append('math.sqrt(')
        self.updateCurrentLabel()

    def clickInverse(self):
        if(self.state == 1):
            self.current_expression.clear()
            self.current_expression.append('1/(')
            self.cal_expression.clear()
            self.cal_expression.append('1/(')
            x = list(str(self.total_expression))
            for digit in x:
                self.cal_expression.append(str(digit))
                self.current_expression.append(str(digit))
            self.state = 0
        else:
            self.current_expression.append('1/(')
            self.cal_expression.append('1/(')

        self.updateCurrentLabel()

    # _________________________________________________________

    def pack(self):
        self.mainFrame.pack(expand=True, fill="both")

    def unpack(self):
        self.mainFrame.pack_forget()

    def run(self):
        self.window.mainloop()
