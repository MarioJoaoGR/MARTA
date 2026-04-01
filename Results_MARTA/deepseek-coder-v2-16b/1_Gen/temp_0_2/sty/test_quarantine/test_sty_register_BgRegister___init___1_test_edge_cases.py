
import pytest
from sty import register

class BgRegister:
    """
    A class for creating and managing background colors in a terminal or console application using ANSI escape codes.
    
    This class provides methods to set up different types of color calls, including 8-bit and RGB color modes. It allows you to create styled text with various backgrounds by setting the appropriate styles.
    
    Attributes:
        black (Style): Style object for black background.
        red (Style): Style object for red background.
        green (Style): Style object for green background.
        yellow (Style): Style object for yellow background.
        blue (Style): Style object for blue background.
        magenta (Style): Style object for magenta background.
        cyan (Style): Style object for cyan background.
        li_grey (Style): Style object for light grey background.
        rs (Style): Style object to reset the style, returning to default terminal settings.
        da_grey (Style): Style object for dark grey background.
        li_red (Style): Style object for light red background.
        li_green (Style): Style object for light green background.
        li_yellow (Style): Style object for light yellow background.
        li_blue (Style): Style object for light blue background.
        li_magenta (Style): Style object for light magenta background.
        li_cyan (Style): Style object for light cyan background.
        white (Style): Style object for white background.
        da_black (Style): Style object for dark black (or grey) background.
        da_red (Style): Style object for dark red background.
        da_green (Style): Style object for dark green background.
        da_yellow (Style): Style object for dark yellow background.
        da_blue (Style): Style object for dark blue background.
        da_magenta (Style): Style object for dark magenta background.
        da_cyan (Style): Style object for dark cyan background.
        grey (Style): Style object for medium grey background.
    
    Methods:
        None explicitly documented, but the class inherits methods from its parent classes as per Python's inheritance rules.
    
    Example usage:
    --------------
    ```python
    bg = BgRegister()
    print(f"{bg.red}Text With Red Background{bg.rs}")
    print(f"{bg.green}Text With Green Background{bg.rs}")
    ```
    
    In this example, `bg` is an instance of `BgRegister`. The `red`, `green`, etc., attributes are used to set the background color for text within a formatted string using f-string literals. After setting the background color, the `rs` attribute resets the style back to default terminal settings.
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

def test_bg_register():
    bg = BgRegister()
    assert isinstance(bg.black, Style)
    assert isinstance(bg.red, Style)
    assert isinstance(bg.green, Style)
    assert isinstance(bg.yellow, Style)
    assert isinstance(bg.blue, Style)
    assert isinstance(bg.magenta, Style)
    assert isinstance(bg.cyan, Style)
    assert isinstance(bg.li_grey, Style)
    assert isinstance(bg.rs, Style)
    assert isinstance(bg.da_grey, Style)
    assert isinstance(bg.li_red, Style)
    assert isinstance(bg.li_green, Style)
    assert isinstance(bg.li_yellow, Style)
    assert isinstance(bg.li_blue, Style)
    assert isinstance(bg.li_magenta, Style)
    assert isinstance(bg.li_cyan, Style)
    assert isinstance(bg.white, Style)
    assert isinstance(bg.da_black, Style)
    assert isinstance(bg.da_red, Style)
    assert isinstance(bg.da_green, Style)
    assert isinstance(bg.da_yellow, Style)
    assert isinstance(bg.da_blue, Style)
    assert isinstance(bg.da_magenta, Style)
    assert isinstance(bg.da_cyan, Style)
    assert isinstance(bg.grey, Style)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_BgRegister___init___1_test_edge_cases
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:54:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:54:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:54:32: E0602: Undefined variable 'renderfunc' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:55:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:55:25: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:55:39: E0602: Undefined variable 'renderfunc' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:56:8: E1101: Instance of 'BgRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:56:25: E0602: Undefined variable 'RgbBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:56:34: E0602: Undefined variable 'renderfunc' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:58:8: E1101: Instance of 'BgRegister' has no 'set_eightbit_call' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:58:31: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:59:8: E1101: Instance of 'BgRegister' has no 'set_rgb_call' member (no-member)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:59:26: E0602: Undefined variable 'RgbBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:63:21: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:63:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:64:19: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:64:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:65:21: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:65:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:66:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:66:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:67:20: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:67:26: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:68:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:68:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:69:20: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:69:26: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:70:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:70:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:72:18: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:72:24: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:75:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:75:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:76:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:76:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:77:24: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:77:30: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:78:25: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:78:31: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:79:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:79:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:80:26: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:80:32: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:81:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:81:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:82:21: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:82:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:85:24: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:85:30: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:86:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:86:28: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:87:24: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:87:30: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:88:25: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:88:31: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:89:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:89:29: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:90:26: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:90:32: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:91:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:91:29: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:92:20: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:92:26: E0602: Undefined variable 'EightbitBg' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:96:32: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:97:30: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:98:32: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:99:33: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:100:31: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:101:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:102:31: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:103:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:104:29: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:105:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:106:33: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:107:35: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:108:36: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:109:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:110:37: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:111:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:112:32: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:113:35: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:114:33: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:115:35: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:116:36: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:117:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:118:37: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:119:34: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_BgRegister___init___1_test_edge_cases.py:120:31: E0602: Undefined variable 'Style' (undefined-variable)


"""