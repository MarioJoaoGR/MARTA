
import pytest
from ansible.utils.color import colorize
import os

# Test cases for the colorize function
def test_basic_usage():
    assert colorize("Result", 42, "green") == 'Result=42'

def test_non_zero_numerical_value_with_color():
    assert colorize("Value", -1, "red") == '\033[38;5;196mValue=-1\033[0m'

def test_zero_numerical_value_without_color():
    os.environ['ANSIBLE_COLOR'] = 'False'  # Assuming this environment variable is set to False
    assert colorize("Result", 0, "blue") == 'Result=0'

def test_using_environment_variable_for_colorization():
    os.environ['ANSIBLE_COLOR'] = 'True'  # Assuming this environment variable is set to True
    assert colorize("Value", 1, "yellow") == '\033[38;5;226mValue=1\033[0m'

def test_explicitly_setting_ansible_color():
    os.environ['ANSIBLE_COLOR'] = 'False'  # Assuming this environment variable is set to False
    assert colorize("Value", 1, "yellow") == 'Value=1'
