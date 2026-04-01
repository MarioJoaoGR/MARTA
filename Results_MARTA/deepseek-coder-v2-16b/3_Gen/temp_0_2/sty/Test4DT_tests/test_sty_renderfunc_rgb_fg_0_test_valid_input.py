
import pytest
from sty import renderfunc

def test_valid_input():
    assert renderfunc.rgb_fg(0, 255, 0) == '\x1b[38;2;0;255;0m'
    assert renderfunc.rgb_fg(255, 0, 0) == '\x1b[38;2;255;0;0m'
    assert renderfunc.rgb_fg(0, 0, 255) == '\x1b[38;2;0;0;255m'
    assert renderfunc.rgb_fg(255, 255, 0) == '\x1b[38;2;255;255;0m'
    assert renderfunc.rgb_fg(0, 255, 255) == '\x1b[38;2;0;255;255m'
    assert renderfunc.rgb_fg(255, 0, 255) == '\x1b[38;2;255;0;255m'
    assert renderfunc.rgb_fg(255, 255, 255) == '\x1b[38;2;255;255;255m'
    assert renderfunc.rgb_fg(128, 128, 128) == '\x1b[38;2;128;128;128m'
