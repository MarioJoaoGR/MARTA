# Module: ansible.utils.color
import pytest
from ansible.utils.color import stringc

def test_stringc_basic():
    assert stringc("Hello, World!", "color256") == '\033[38;5;256mHello, World!\033[0m'

def test_stringc_multiline():
    multi_line_text = "Line one\nLine two"
    assert stringc(multi_line_text, "rgb24534", wrap_nonvisible_chars=True) == '\001\033[38;5;29m\002Line one\n\001\033[38;5;29m\002Line two'

def test_stringc_gray():
    plain_text = "Gray text"
    assert stringc(plain_text, "gray20", wrap_nonvisible_chars=False) == '\033[38;5;25mGray text\033[0m'

def test_stringc_environment():
    import os
    os.environ['ANSIBLE_COLOR'] = 'True'
    assert stringc("Hello, World!", "color256") == '\033[38;5;256mHello, World!\033[0m'

def test_stringc_no_wrap():
    plain_text = "Gray text"
    assert stringc(plain_text, "gray20", wrap_nonvisible_chars=False) == 'Gray text'

# Add more tests as needed to cover different scenarios and edge cases.
