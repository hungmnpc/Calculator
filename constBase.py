SCREENWIDTH = 320
SCREENHEIGHT = 500
DISPLAY_FRAME_HEIGHT = 200
BUTTONS_FRAME_HEIGHT = 330
LABEL_COLOR = "#000000"
LIGHT_BLUE = "#99ccff"
LIGHT_RED = "#FFA1A1"
DiSPLAY_COLOR = "#DDDDDD"
WHITE = "#FFFFFF"
TOGGLE_COLOR = "#EEE4AB"
OFF_WHITE = "#DBDBDB"
SMALL_FONT_STYLE = ("Arial", 16)
BUTTON_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 30, "bold")
FONT = ("Arial")
MAXLENGTH = 24
FONT_SIZE_TOTAL = 30
MEM_ERROR_TEXT = "Overlong.\nTry another calculation."
MATH_ERROR_TEXT = "Math Error!"
SYNTAX_ERROR_TEXT = "Syntax Error!"
COEFFICIENT_FONT_DEFAULT = 12
EQUATION_HAS_NO_SOLUTION = "the equation has no solution"


COLOR1 = "#B1BCE6"
DIGITS = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    0: (3, 1),
    '.': (3, 2),
}


class SIMPLE_EQUATION(object):
    id = 1
    text = 'Phương trình bậc nhất: ax + b = 0'


class QUADRATIC_EQUATION(object):
    id = 2
    text = 'Phương trình bậc 2: ax\u00b2 + bx + c = 0'


class CUBIC_EQUATION(object):
    id = 3
    text = 'Phương trình bậc 3: ax\u00b3 + bx\u00b2 + cx + d = 0'


class QUARTIC_EQUATION(object):
    id = 4
    text = 'Phương trình bậc 4: ax\u2074 + bx\u00b3 + cx\u00b2 + dx + e = 0'


OPERATION = {"/": "÷", "*": "×", "+": "＋", "-": "-"}
