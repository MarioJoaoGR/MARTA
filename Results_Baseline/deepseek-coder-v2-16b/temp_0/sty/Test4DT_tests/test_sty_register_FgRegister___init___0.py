# Module: sty.register
import pytest
from sty import FgRegister, Sgr, EightbitFg, RgbFg, Style, renderfunc

# Fixture to create an instance of FgRegister for each test
@pytest.fixture
def fg_register():
    return FgRegister()

# Test case to check if the FgRegister instance is created correctly
def test_fg_register_instance(fg_register):
    assert isinstance(fg_register, FgRegister)

# Test case to print red text using the FgRegister instance
def test_print_red_text(capsys, fg_register):
    print(f"{fg_register.red}Red Text{fg_register.rs}")
    captured = capsys.readouterr()
    assert "Red Text" in captured.out

# Test case to print green text using the FgRegister instance
def test_print_green_text(capsys, fg_register):
    print(f"{fg_register.green}Green Text{fg_register.rs}")
    captured = capsys.readouterr()
    assert "Green Text" in captured.out

# Test case to print blue text using the FgRegister instance
def test_print_blue_text(capsys, fg_register):
    print(f"{fg_register.blue}Blue Text{fg_register.rs}")
    captured = capsys.readouterr()
    assert "Blue Text" in captured.out

# Test case to print multiple colored texts using the FgRegister instance
def test_print_multiple_colored_texts(capsys, fg_register):
    colors = [fg_register.red, fg_register.green, fg_register.blue, fg_register.yellow]
    texts = ["Red Text", "Green Text", "Blue Text", "Yellow Text"]
    for color, text in zip(colors, texts):
        print(f"{color}{text}{fg_register.rs}")
    captured = capsys.readouterr()
    assert all([text in captured.out for text in texts])
