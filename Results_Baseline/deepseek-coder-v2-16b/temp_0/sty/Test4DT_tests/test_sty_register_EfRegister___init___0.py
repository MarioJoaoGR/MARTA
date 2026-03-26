
# Module: sty.register
# test_efregister.py
from sty import EfRegister, Style, Sgr, renderfunc

def test_bold_text():
    ef = EfRegister()
    expected_output = "\x1b[1mBold Text\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m"
    assert f"{ef.bold}Bold Text{ef.rs}" == expected_output

def test_italic_text():
    ef = EfRegister()
    expected_output = "\x1b[3mItalic Text\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m"
    assert f"{ef.italic}Italic Text{ef.rs}" == expected_output

def test_underline_text():
    ef = EfRegister()
    expected_output = "\x1b[4mUnderlined Text\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m"
    assert f"{ef.underl}Underlined Text{ef.rs}" == expected_output

def test_blink_text():
    ef = EfRegister()
    expected_output = "\x1b[5mBlinking Text\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m"
    assert f"{ef.blink}Blinking Text{ef.rs}" == expected_output

def test_reset_all_effects():
    ef = EfRegister()
    original_output = "Normal Text " + str(ef.rs)
    assert f"Normal Text {ef.rs}" == original_output
