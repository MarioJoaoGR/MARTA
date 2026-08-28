
import pytest
from ansible.utils.color import parsecolor

def stringc(text, color, wrap_nonvisible_chars=False):
    """String in color."""
    if ANSIBLE_COLOR:
        color_code = parsecolor(color)
        fmt = u"\033[%sm%s\033[0m"
        if wrap_nonvisible_chars:
            fmt = u"\001\033[%sm\002%s\001\033[0m\002"
        return u"\n".join([fmt % (color_code, t) for t in text.split(u'\n')])
    else:
        return text

# Test scenarios
def test_valid_input_happy_path():
    result = stringc("Hello, World!", "color256")
    assert "\033[38;5;256mHello, World!\033[0m" == result

def test_edge_case_none_values():
    with pytest.raises(TypeError):
        stringc(None, 'color256')

def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        stringc("Invalid text", "unsupported_color")
