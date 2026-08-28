
import pytest
from thefuck.types import Command

def test_invalid_option_s():
    with pytest.raises(TypeError):
        command = Command("echo -s 'Hello, World!'", "Hello, World!", output="Error: invalid option -- s")

def test_invalid_option_u():
    with pytest.raises(TypeError):
        command = Command("echo -u 'Hello, World!'", "Hello, World!", output="Error: invalid option -- u")

def test_invalid_option_r():
    with pytest.raises(TypeError):
        command = Command("echo -r 'Hello, World!'", "Hello, World!", output="Error: invalid option -- r")

def test_invalid_option_q():
    with pytest.raises(TypeError):
        command = Command("echo -q 'Hello, World!'", "Hello, World!", output="Error: invalid option -- q")

def test_invalid_option_f():
    with pytest.raises(TypeError):
        command = Command("echo -f 'Hello, World!'", "Hello, World!", output="Error: invalid option -- f")

def test_invalid_option_d():
    with pytest.raises(TypeError):
        command = Command("echo -d 'Hello, World!'", "Hello, World!", output="Error: invalid option -- d")

def test_invalid_option_v():
    with pytest.raises(TypeError):
        command = Command("echo -v 'Hello, World!'", "Hello, World!", output="Error: invalid option -- v")

def test_invalid_option_t():
    with pytest.raises(TypeError):
        command = Command("echo -t 'Hello, World!'", "Hello, World!", output="Error: invalid option -- t")
