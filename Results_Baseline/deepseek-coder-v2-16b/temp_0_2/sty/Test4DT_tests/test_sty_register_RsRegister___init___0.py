
# Module: sty.register
import pytest
from sty import RsRegister, fg, bg, Style  # Added Import for Style

# Test instantiation of RsRegister class
def test_rsregister_instantiation():
    rs = RsRegister()
    assert isinstance(rs, RsRegister)

# Test italic attribute
def test_italic_attribute():
    rs = RsRegister()
    expected_output = "\033[23mItalic Text\033[0m"  # ANSI escape codes for italic text
    assert f"{rs.italic}Italic Text{rs.all}" == expected_output

# Test underl attribute
def test_underl_attribute():
    rs = RsRegister()
    expected_output = "\033[24mUnderlined Text\033[0m"  # ANSI escape codes for underlined text
    assert f"{rs.underl}Underlined Text{rs.all}" == expected_output

# Test red foreground color with italic attribute
def test_red_italic_text():
    rs = RsRegister()
    expected_output = "\033[31m\033[23mRed Italic Text\033[0m"  # ANSI escape codes for red foreground and italic text
    assert f"{fg.red}{rs.italic}Red Italic Text{rs.all}" == expected_output

# Test all attributes are correctly instantiated
def test_all_attributes():
    rs = RsRegister()
    assert isinstance(rs.all, Style)
    assert isinstance(rs.fg, Style)
    assert isinstance(rs.bg, Style)
    assert isinstance(rs.ef, Style)
    assert isinstance(rs.bold_dim, Style)
    assert isinstance(rs.dim_bold, Style)
    assert isinstance(rs.i, Style)
    assert isinstance(rs.italic, Style)
    assert isinstance(rs.u, Style)
    assert isinstance(rs.underl, Style)
    assert isinstance(rs.blink, Style)
    assert isinstance(rs.inverse, Style)
    assert isinstance(rs.hidden, Style)
    assert isinstance(rs.strike, Style)
