from decimal import Decimal
from re import S
import tkinter as tk
import tkinter.font as font
from unicodedata import decimal
import math
import constBase


class Standard:
    def __init__(self, root):
        self.window = root
        self.mainFrame = self.create_main_frame()
        self.total_expression = ''
        self.current_expression = []
        self.cal_expression = []
        self.digits = constBase.DIGITS
        self.operation = constBase.OPERATION

        self.display_frame = self.create_display_frame()
        self.current_label, self.total_label = self.create_display_labels()

        self.buttons_frame = self.create_buttons_frame()
        self.configButton()
        self.create_digits_button()
        self.create_operation_buttons()
        self.create_special_buttons()
        self.state = 0

    def configButton(self):
        for x in range(0, 4):
            self.buttons_frame.columnconfigure(x, weight=1)
        for x in range(0, 6):
            self.buttons_frame.rowconfigure(x, weight=1)

    def create_main_frame(self):
        frame = tk.Frame(self.window)
        return frame

    def get_frame(self):
        return self.mainFrame

    def create_display_frame(self):
        frame = tk.Frame(self.mainFrame, height=constBase.DISPLAY_FRAME_HEIGHT)
        frame.pack(expand=True, fill="both")
        frame.pack_propagate(0)
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(
            self.mainFrame, height=constBase.BUTTONS_FRAME_HEIGHT, bg="blue")
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(0)
        return frame

    def create_digits_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=constBase.WHITE, fg=constBase.LABEL_COLOR,
                               borderwidth=0, font=constBase.FONT, command=lambda x=digit: self.add_value_label(x))
            button.grid(row=grid_value[0]+2,
                        column=grid_value[1], sticky=tk.NSEW)
            button['font'] = font.Font(size=17)

    def create_display_labels(self):
        current_label = tk.Label(self.display_frame, text=''.join(self.total_expression),
                                 font=constBase.SMALL_FONT_STYLE, fg=constBase.LABEL_COLOR, anchor=tk.E)
        current_label.pack(expand=1, fill="both", side=tk.TOP)

        total_label = tk.Label(self.display_frame, text=''.join(self.current_expression),
                               font=constBase.LARGE_FONT_STYLE, fg=constBase.LABEL_COLOR, anchor=tk.E, height=10, bg="red", width=200)
        total_label.pack(expand=1, fill="both", side=tk.BOTTOM)
        total_label.pack_propagate(0)

        return current_label, total_label

    def create_operation_buttons(self):
        i = 1
        for operator, symbol in self.operation.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0,
                               command=lambda symbol_label=operator: self.add_value_label(symbol_label))
            button.grid(row=i, column=3, sticky=tk.NSEW)
            button['font'] = font.Font(size=17)
            i += 1

    def create_negate_button(self):
        button = tk.Button(self.buttons_frame, text="±", bg=constBase.WHITE,
                           fg=constBase.LABEL_COLOR, borderwidth=0, command=self.negate)
        button.grid(row=5, column=0, sticky=tk.NSEW)
        button['font'] = font.Font(size=17)

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=constBase.LIGHT_BLUE,
                           fg=constBase.LABEL_COLOR, borderwidth=0, command=self.equal_button_click)
        button.grid(row=5, column=3, sticky=tk.NSEW)
        button['font'] = font.Font(size=17)

    def create_clear_buttons(self):
        button_clear_all = tk.Button(self.buttons_frame, text="C", bg=constBase.OFF_WHITE,
                                     fg=constBase.LABEL_COLOR, borderwidth=0, command=self.clear_all_display)
        button_clear_all.grid(row=0, column=2, sticky=tk.NSEW)
        button_clear_all['font'] = font.Font(size=17)

        button_backspace = tk.Button(self.buttons_frame, text="⌫", bg=constBase.OFF_WHITE,
                                     fg=constBase.LABEL_COLOR, borderwidth=0, command=lambda: self.back_space())
        button_backspace.grid(row=0, column=3, sticky=tk.NSEW)
        button_backspace['font'] = font.Font(size=17)

    def create_some_special_operation_buttons(self):
        button_open_parenthese = tk.Button(
            self.buttons_frame, text="(", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0,
            command=lambda symbol_label="(": self.add_value_label(symbol_label))
        button_open_parenthese.grid(row=0, column=0, sticky=tk.NSEW)
        button_open_parenthese['font'] = font.Font(size=17)

        button_close_parenthese = tk.Button(self.buttons_frame, text=")", bg=constBase.OFF_WHITE,
                                            fg=constBase.LABEL_COLOR, borderwidth=0,
                                            command=lambda symbol_label=")": self.add_value_label(symbol_label))
        button_close_parenthese.grid(row=0, column=1, sticky=tk.NSEW)
        button_close_parenthese['font'] = font.Font(size=17)

        button_inverse = tk.Button(
            self.buttons_frame, text="⅟𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.click_inverse)
        button_inverse.grid(row=1, column=0, sticky=tk.NSEW)
        button_inverse['font'] = font.Font(size=17)

        button_sqr = tk.Button(self.buttons_frame, text="𝓍²",
                               bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.click_sqr)
        button_sqr.grid(row=1, column=1, sticky=tk.NSEW)
        button_sqr['font'] = font.Font(size=17)

        button_sqrt = tk.Button(
            self.buttons_frame, text="√𝓍", bg=constBase.OFF_WHITE, fg=constBase.LABEL_COLOR, borderwidth=0, command=self.click_sqrt)
        button_sqrt.grid(row=1, column=2, sticky=tk.NSEW)
        button_sqrt['font'] = font.Font(size=17)

    def create_special_buttons(self):
        self.create_equal_button()
        self.create_negate_button()
        self.create_clear_buttons()
        self.create_some_special_operation_buttons()

    def update_total_label(self):
        x = len(self.total_expression)

        if (x > 24):
            self.total_expression = constBase.TEXT_ERROR
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

    def update_current_label(self):
        self.current_label.config(text=''.join(self.current_expression))

    def add_value_label(self, value):
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
        self.update_current_label()

    def back_space(self):
        try:
            self.current_expression.pop()
            self.cal_expression.pop()
        except:
            pass
        self.update_current_label()

    def clear_all_display(self):
        self.total_expression = ''
        self.current_expression.clear()
        self.cal_expression.clear()
        self.update_total_label()
        self.update_current_label()

    def equal_button_click(self):
        try:
            a = str(eval(''.join(self.cal_expression)))
            # x = len(str(int(a)))
            # a = str(round(a, constBase.MAXLENGTH - x))
        except Exception as e:
            if (("math" in str(e)) or ("zero" in str(e))):
                self.total_expression = constBase.MATH_ERROR_TEXT
            else:
                self.total_expression = constBase.SYNTAX_ERROR_TEXT
            pass
        try:
            self.total_expression = a.rstrip('0').rstrip(
                '.') if '.' in a else a  # ???
        except:
            pass

        if (self.total_expression == ''):
            self.total_expression = '0'
        self.update_total_label()

        self.state = 1

    def negate(self):
        a = str(Decimal(''.join(self.current_expression)) * -1)

        self.update_total_label()

    def click_sqr(self):
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
        self.update_current_label()

    def click_sqrt(self):
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
        self.update_current_label()

    def click_inverse(self):
        self.current_expression.append('1/(')
        self.cal_expression.append('1/(')
        self.update_current_label()

    def pack(self):
        self.mainFrame.pack(expand=True, fill="both")

    def unpack(self):
        self.mainFrame.pack_forget()

    def run(self):
        self.window.mainloop()
