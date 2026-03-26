
import pytest
from sty import register

class EfRegister:
    """
    A class for creating and managing text effects such as bold, italic, underline, etc., using ANSI escape codes.
    
    This class provides instances that can be used to apply various text styling options directly in print statements or other contexts where the escape sequences are recognized.
    
    Attributes:
        b (Style): An instance of Style with Sgr(1), which applies bold effect.
        bold (Style): Alias for `b`, providing the same functionality.
        dim (Style): An instance of Style with Sgr(2), which applies dim or faint effect.
        i (Style): An instance of Style with Sgr(3), which applies italic effect.
        italic (Style): Alias for `i`, providing the same functionality.
        u (Style): An instance of Style with Sgr(4), which applies underline effect.
        underl (Style): Alias for `u`, providing the same functionality.
        blink (Style): An instance of Style with Sgr(5), which applies blinking effect.
        inverse (Style): An instance of Style with Sgr(7), which inverts the foreground and background colors.
        hidden (Style): An instance of Style with Sgr(8), which hides the text.
        strike (Style): An instance of Style with Sgr(9), which applies strikethrough effect.
        rs (Style): A composite instance of Style that resets all effects applied by this class, using Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), and Sgr(29).
    
    Usage:
    ------
        ef = EfRegister()
        print(f"{ef.bold}Bold Text{ef.rs}")  # Prints "Bold Text" in bold font.
        print(f"{ef.italic}Italic Text{ef.rs}")  # Prints "Italic Text" in italic font.
    
    Note:
    -----
    The `Sgr` class is used internally to define the specific style or formatting using ANSI escape codes. Ensure that the SGR numbers are valid and supported by your terminal for expected results.
    """
    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr

        self.b = Style(Sgr(1))
        self.bold = Style(Sgr(1))
        self.dim = Style(Sgr(2))
        self.i = Style(Sgr(3))
        self.italic = Style(Sgr(3))
        self.u = Style(Sgr(4))
        self.underl = Style(Sgr(4))
        self.blink = Style(Sgr(5))
        self.inverse = Style(Sgr(7))
        self.hidden = Style(Sgr(8))
        self.strike = Style(Sgr(9))

        # Reset all effects (Unfortunately there is no single Escape Sequence for this)
        self.rs = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        ef = register.EfRegister(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_EfRegister___init___0_test_invalid_inputs
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:38:8: E1101: Instance of 'EfRegister' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:38:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:38:32: E0602: Undefined variable 'renderfunc' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:40:17: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:40:23: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:41:20: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:41:26: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:42:19: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:42:25: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:43:17: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:43:23: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:44:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:44:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:45:17: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:45:23: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:46:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:46:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:47:21: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:47:27: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:48:23: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:48:29: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:49:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:49:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:50:22: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:50:28: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:18: E0602: Undefined variable 'Style' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:24: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:33: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:42: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:51: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:60: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:69: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:53:78: E0602: Undefined variable 'Sgr' (undefined-variable)
sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_invalid_inputs.py:58:13: E1121: Too many positional arguments for constructor call (too-many-function-args)


"""