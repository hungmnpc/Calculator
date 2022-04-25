import tkinter as tk
import tkinter.font as font



SCREENWIDTH = 320
SCREENHEIGHT = 500
DISPLAY_FRAME_HEIGHT = 170
BUTTONS_FRAME_HEIGHT = 330
LABEL_COLOR = "#000000"
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 49
LIGHT_BLUE = "#99ccff"


WHITE = "#FFFFFF"
OFF_WHITE = "#DBDBDB"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
FONT = ("Arial")






class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(str(SCREENWIDTH) + 'x' + str(SCREENHEIGHT))
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expression = "0"
        self.current_expression = "0"
        self.FONT_SYMBOL = font.Font(size=17)
        self.digits = {
            7:(2, 0),
            8:(2, 1),
            9:(2, 2),
            4:(3, 0),
            5:(3, 1),
            6:(3, 2),
            1:(4, 0),
            2:(4, 1),
            3:(4, 2),
            0:(5, 1),
            '.':(5, 2),
        }
        self.operation = {"/": "÷", "*": "×", "+": "＋", "-": "-"}
        
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        

        
        
        self.buttons_frame = self.create_buttons_frame()
        for x in range(0, 4):
            self.buttons_frame.columnconfigure(x, weight=1)
        for x in range(0, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
        self.create_digits_button()
        self.create_operation_buttons()
        self.create_special_buttons()
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=DISPLAY_FRAME_HEIGHT)
        frame.pack(expand=True, fill="both")
        frame.pack_propagate(0)
        return frame
    

    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window, height=BUTTONS_FRAME_HEIGHT, bg="blue")
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(0)
        return frame
    
    def create_digits_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, borderwidth=0, font=FONT)
            button.grid(row= grid_value[0], column= grid_value[1], sticky=tk.NSEW)
            button['font'] = self.FONT_SYMBOL
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, font=SMALL_FONT_STYLE, fg=LABEL_COLOR,anchor=tk.E, padx=24)
        total_label.pack(expand=1, fill="both")
        
        
        label = tk.Label(self.display_frame, text = self.current_expression, font=LARGE_FONT_STYLE, fg=LABEL_COLOR,anchor=tk.E, padx=24, bg="red")
        label.pack(expand=1, fill="both")
        
        return total_label, label
    
    def create_operation_buttons(self):
        i = 1
        for operator, symbol in self.operation.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, borderwidth=0)
            button.grid(row=i, column=3, sticky=tk.NSEW)
            button['font'] = self.FONT_SYMBOL
            i += 1
            
    def create_negate_button(self):
        button = tk.Button(self.buttons_frame, text= "±", bg=WHITE, fg=LABEL_COLOR, borderwidth= 0)
        button.grid(row=5, column=0, sticky=tk.NSEW)
        button['font'] = self.FONT_SYMBOL
    
    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text= "=", bg=LIGHT_BLUE, fg=LABEL_COLOR, borderwidth=0)
        button.grid(row=5, column=3, sticky=tk.NSEW)
        button['font'] = self.FONT_SYMBOL
    
    def create_clear_buttons(self):
        button_clear_all = tk.Button(self.buttons_frame, text="C", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_clear_all.grid(row=0, column=2, sticky=tk.NSEW)
        button_clear_all['font'] = self.FONT_SYMBOL
        
        button_clear_element = tk.Button(self.buttons_frame, text="CE", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_clear_element.grid(row=0, column=1, sticky=tk.NSEW)
        button_clear_element['font'] = self.FONT_SYMBOL
        
        button_backspace = tk.Button(self.buttons_frame, text="⌫", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_backspace.grid(row=0, column=3, sticky=tk.NSEW)
        button_backspace['font'] = self.FONT_SYMBOL
        
    def create_some_special_operation_buttons(self):
        button_percent = tk.Button(self.buttons_frame, text="%", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_percent.grid(row=0, column=0, sticky=tk.NSEW)
        button_percent['font'] = self.FONT_SYMBOL
        
        button_inverse = tk.Button(self.buttons_frame, text="⅟𝓍", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_inverse.grid(row=1, column=0, sticky=tk.NSEW)
        button_inverse['font'] = self.FONT_SYMBOL
        
        button_sqr = tk.Button(self.buttons_frame, text="𝓍²", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_sqr.grid(row=1, column=1, sticky=tk.NSEW)
        button_sqr['font'] = self.FONT_SYMBOL
        
        button_sqrt = tk.Button(self.buttons_frame, text="√𝓍", bg= OFF_WHITE, fg= LABEL_COLOR, borderwidth=0)
        button_sqrt.grid(row=1, column=2, sticky=tk.NSEW)
        button_sqrt['font'] = self.FONT_SYMBOL
        
            
        
    def create_special_buttons(self):
        self.create_equal_button()
        self.create_negate_button()
        self.create_clear_buttons()
        self.create_some_special_operation_buttons()
        

        
    
        
        
    def run(self):
        self.window.mainloop()
        
        
if __name__ == "__main__":
    calc = Calculator()
    calc.run()