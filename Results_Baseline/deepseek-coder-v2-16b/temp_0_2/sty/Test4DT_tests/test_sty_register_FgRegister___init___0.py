# Module: sty.register
import pytest
from sty import FgRegister, Style, Sgr, EightbitFg, RgbFg

# Create an instance of FgRegister
fg = FgRegister()

def test_red_text():
    assert f"{fg.red}Red Text{fg.rs}" == "\033[31mRed Text\033[39m"

def test_green_text():
    assert f"{fg.green}Green Text{fg.rs}" == "\033[32mGreen Text\033[39m"

def test_blue_text():
    assert f"{fg.blue}Blue Text{fg.rs}" == "\033[34mBlue Text\033[39m"

def test_yellow_text():
    assert f"{fg.yellow}Yellow Text{fg.rs}" == "\033[33mYellow Text\033[39m"

def test_magenta_text():
    assert f"{fg.magenta}Magenta Text{fg.rs}" == "\033[35mMagenta Text\033[39m"

def test_cyan_text():
    assert f"{fg.cyan}Cyan Text{fg.rs}" == "\033[36mCyan Text\033[39m"

def test_light_grey_text():
    assert f"{fg.li_grey}Light Grey Text{fg.rs}" == "\033[37mLight Grey Text\033[39m"

def test_dark_grey_text():
    assert f"{fg.da_grey}Dark Grey Text{fg.rs}" == "\033[90mDark Grey Text\033[39m"

def test_white_text():
    assert f"{fg.white}White Text{fg.rs}" == "\033[97mWhite Text\033[39m"

# Add more tests for other colors if necessary
