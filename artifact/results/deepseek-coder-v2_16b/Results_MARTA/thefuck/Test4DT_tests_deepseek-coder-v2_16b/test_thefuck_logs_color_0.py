
import pytest
from thefuck.logs import color

def test_valid_input_colored_output_enabled():
    settings = type('Settings', (), {'no_colors': False})()
    assert color('red') == 'red'
