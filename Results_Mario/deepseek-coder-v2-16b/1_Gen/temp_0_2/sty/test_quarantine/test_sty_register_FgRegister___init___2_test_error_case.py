
from sty.register import Register, Style
import renderfunc

class FgRegister(Register):
    """
    A class for creating and managing foreground color registers in a terminal or console application using ANSI escape codes.
    
    This class inherits from the `Register` base class, which provides functionality for setting up different render types for colors. It supports classic terminal colors as well as less supported and least supported 8-bit colors.
    
    Attributes:
        black (Style): A Style object with SGR parameter set to 30 for black foreground color.
        red (Style): A Style object with SGR parameter set to 31 for red foreground color.
        green (Style): A Style object with SGR parameter set to 32 for green foreground color.
        yellow (Style): A Style object with SGR parameter set to 33 for yellow foreground color.
        blue (Style): A Style object with SGR parameter set to 34 for blue foreground color.
        magenta (Style): A Style object with SGR parameter set to 35 for magenta foreground color.
        cyan (Style): A Style object with SGR parameter set to 36 for cyan foreground color.
        li_grey (Style): A Style object with SGR parameter set to 37 for light grey foreground color.
        rs (Style): A Style object with SGR parameter set to 39 for reset style, which restores default terminal settings.
        da_grey (Style): A Style object with SGR parameter set to 90 for dark grey foreground color.
        li_red (Style): A Style object with SGR parameter set to 91 for light red foreground color.
        li_green (Style): A Style object with SGR parameter set to 92 for light green foreground color.
        li_yellow (Style): A Style object with SGR parameter set to 93 for light yellow foreground color.
        li_blue (Style): A Style object with SGR parameter set to 94 for light blue foreground color.
        li_magenta (Style): A Style object with SGR parameter set to 95 for light magenta foreground color.
        li_cyan (Style): A Style object with SGR parameter set to 96 for light cyan foreground color.
        white (Style): A Style object with SGR parameter set to 97 for white foreground color.
    
    Examples:
        To print text in red, you can use the following code snippet:
        
        ```python
        print(f"{fg.red}Red Text{fg.rs}")
        ```
        
        This will output "Red Text" with a red foreground color according to the ANSI escape codes defined by `fg.red`.
    """
    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitFg] = renderfunc.eightbit_fg
        self.renderfuncs[RgbFg] = renderfunc.rgb_fg

        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)

        # Classic terminal foreground color preset.
        # These are well supported.
        self.black = Style(Sgr(30))
        self.red = Style(Sgr(31))
        self.green = Style(Sgr(32))
        self.yellow = Style(Sgr(33))
        self.blue = Style(Sgr(34))
        self.magenta = Style(Sgr(35))
        self.cyan = Style(Sgr(36))
        self.li_grey = Style(Sgr(37))

        self.rs = Style(Sgr(39))

        # These are less supported.
        self.da_grey = Style(Sgr(90))
        self.li_red = Style(Sgr(91))
        self.li_green = Style(Sgr(92))
        self.li_yellow = Style(Sgr(93))
        self.li_blue = Style(Sgr(94))
        self.li_magenta = Style(Sgr(95))
        self.li_cyan = Style(Sgr(96))
        self.white = Style(Sgr(97))

        # These are least supported.
        self.da_black = Style(EightbitFg(0))
        self.da_red = Style(EightbitFg(88))
        self.da_green = Style(EightbitFg(22))
        self.da_yellow = Style(EightbitFg(58))
        self.da_blue = Style(EightbitFg(18))
        self.da_magenta = Style(EightbitFg(89))
        self.da_cyan = Style(EightbitFg(23))
        self.grey = Style(EightbitFg(249))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___2_test_error_case
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:3:0: E0401: Unable to import 'renderfunc' (import-error)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:42:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:43:25: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:44:25: E0602: Undefined variable 'RgbFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:46:31: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:47:26: E0602: Undefined variable 'RgbFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:51:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:52:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:53:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:54:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:55:26: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:56:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:57:26: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:58:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:60:24: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:63:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:64:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:65:30: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:66:31: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:67:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:68:32: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:69:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:70:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:73:30: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:74:28: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:75:30: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:76:31: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:77:29: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:78:32: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:79:29: E0602: Undefined variable 'EightbitFg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_error_case.py:80:26: E0602: Undefined variable 'EightbitFg' (undefined-variable)


"""