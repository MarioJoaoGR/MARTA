
# Module: sty.primitive
# test_sty_primitive.py
from sty.primitive import Register, Style

def test_register_initialization():
    register = Register()
    assert hasattr(register, 'renderfuncs') and isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert hasattr(register, 'is_muted') and not register.is_muted, "Expected is_muted to be False initially"
    assert callable(register.eightbit_call) and register.eightbit_call('test') == 'test', "Expected eightbit_call to be a lambda function that returns its argument unchanged"
    assert callable(register.rgb_call) and register.rgb_call(1, 2, 3) == (1, 2, 3), "Expected rgb_call to be a lambda function that returns its arguments as a tuple"

def test_style_initialization():
    class StylingRule: pass
    class RenderType(StylingRule):
        def __init__(self, args: tuple):
            self.args = args
    class Style(str):
        def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
            new_cls = super().__new__(cls, value)  # type: ignore
            setattr(new_cls, "rules", rules)
            return new_cls
    
    register = Register()
    style = Style(RenderType((1,)), value="Hello")
    assert isinstance(style, Style), "Expected the instance to be of type Style"
    assert hasattr(style, 'rules') and len(style.rules) == 1, "Expected rules to be a list with one element"
    assert all(isinstance(rule, RenderType) for rule in style.rules), "All elements in rules should be instances of RenderType"
    assert str(style) == "Hello", "Expected the string representation to be 'Hello'"

def test_setattr_when_muted():
    register = Register()
    register.is_muted = True
    
    class StylingRule: pass
    class Style(str):
        def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
            new_cls = super().__new__(cls, value)  # type: ignore
            setattr(new_cls, "rules", rules)
            return new_cls
    
    style = Style(StylingRule(), value="Hello")
    assert str(style) == "Hello", "Expected the string representation to be 'Hello' without any modifications"

def test_setattr_when_not_muted():
    register = Register()
    register.is_muted = False
    
    class StylingRule: pass
    class Style(str):
        def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
            new_cls = super().__new__(cls, value)  # type: ignore
            setattr(new_cls, "rules", rules)
            return new_cls
    
    style = Style(StylingRule(), value="Hello")
    assert str(style) == "\x1B[0mHello\x1B[0m", "Expected the string representation to be 'Hello' with ANSI escape codes applied"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register___setattr___0
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:27:43: E1101: Instance of 'Style' has no 'rules' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register___setattr___0.py:28:56: E1101: Instance of 'Style' has no 'rules' member (no-member)

"""