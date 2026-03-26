
from sty import Style, Sgr, EightbitBg, RgbBg, renderfunc

class BgRegister(Style):
    """
    A class for creating text with colored backgrounds using ANSI escape codes.
    
    This class provides methods to set and get different types of background colors, including classic terminal colors and less supported 8-bit colors. It also supports RGB color settings which are least supported.
    
    Attributes:
        black (Style): Style object for text with a black background.
        red (Style): Style object for text with a red background.
        green (Style): Style object for text with a green background.
        yellow (Style): Style object for text with a yellow background.
        blue (Style): Style object for text with a blue background.
        magenta (Style): Style object for text with a magenta background.
        cyan (Style): Style object for text with a cyan background.
        li_grey (Style): Style object for text with a light grey background.
        rs (Style): Style object for resetting the background to default.
        da_grey (Style): Style object for text with a dark grey background.
        li_red (Style): Style object for text with a light red background.
        li_green (Style): Style object for text with a light green background.
        li_yellow (Style): Style object for text with a light yellow background.
        li_blue (Style): Style object for text with a light blue background.
        li_magenta (Style): Style object for text with a light magenta background.
        li_cyan (Style): Style object for text with a light cyan background.
        white (Style): Style object for text with a white background.
        da_black (Style): Style object for text with a dark black background, which is equivalent to setting the foreground color to black and the background color to default.
        da_red (Style): Style object for text with a dark red background.
        da_green (Style): Style object for text with a dark green background.
        da_yellow (Style): Style object for text with a dark yellow background.
        da_blue (Style): Style object for text with a dark blue background.
        da_magenta (Style): Style object for text with a dark magenta background.
        da_cyan (Style): Style object for text with a dark cyan background.
        grey (Style): Style object for text with a grey background, which is equivalent to setting the foreground color to default and the background color to light grey.
    
    Methods:
        None directly callable from this class; instead, instances of `BgRegister` are used in format strings within print statements or other contexts where ANSI escape codes are supported.
    
    Example usage:
        bg = BgRegister()
        print(f"{bg.red}Text with red background{bg.rs}")  # Prints "Text with red background" with a red background.
        print(f"{bg.green}Text with green background{bg.rs}")  # Prints "Text with green background" with a green background.
    
    Note: The `Style` objects returned by this class are used in format strings to apply the respective color backgrounds, and `rs` is used for resetting the style back to default.
    """
    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitBg] = renderfunc.eightbit_bg
        self.renderfuncs[RgbBg] = renderfunc.rgb_bg

        self.set_eightbit_call(EightbitBg)
        self.set_rgb_call(RgbBg)

        # Classic terminal background color preset.
        # These are well supported.
        self.black = Style(Sgr(40))
        self.red = Style(Sgr(41))
        self.green = Style(Sgr(42))
        self.yellow = Style(Sgr(43))
        self.blue = Style(Sgr(44))
        self.magenta = Style(Sgr(45))
        self.cyan = Style(Sgr(46))
        self.li_grey = Style(Sgr(47))

        self.rs = Style(Sgr(49))

        # These are less supported.
        self.da_grey = Style(Sgr(100))
        self.li_red = Style(Sgr(101))
        self.li_green = Style(Sgr(102))
        self.li_yellow = Style(Sgr(103))
        self.li_blue = Style(Sgr(104))
        self.li_magenta = Style(Sgr(105))
        self.li_cyan = Style(Sgr(106))
        self.white = Style(Sgr(107))

        # These are least supported.
        self.da_black = Style(EightbitBg(0))
        self.da_red = Style(EightbitBg(88))
        self.da_green = Style(EightbitBg(22))
        self.da_yellow = Style(EightbitBg(58))
        self.da_blue = Style(EightbitBg(18))
        self.da_magenta = Style(EightbitBg(89))
        self.da_cyan = Style(EightbitBg(23))
        self.grey = Style(EightbitBg(249))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_BgRegister___init___0_test_valid_inputs
sty/Test4DT_tests/test_sty_register_BgRegister___init___0_test_valid_inputs.py:50:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___0_test_valid_inputs.py:51:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___0_test_valid_inputs.py:52:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___0_test_valid_inputs.py:54:8: E1101: Instance of 'BgRegister' has no 'set_eightbit_call' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___0_test_valid_inputs.py:55:8: E1101: Instance of 'BgRegister' has no 'set_rgb_call' member (no-member)


"""