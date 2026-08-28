
import pytest
from flutils.txtutils import len_without_ansi
from typing import Sequence, List, Tuple

# Scenario 1: Test standard input with a string containing ANSI escape codes
def test_valid_input_string():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Scenario 2: Test standard input with a list of strings containing ANSI escape codes
def test_valid_input_list_of_strings():
    text = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6

# Scenario 3: Test standard input with a string without ANSI escape codes
def test_valid_input_string_without_ansi():
    text = 'foobar'
    assert len_without_ansi(text) == 6

# Scenario 4: Test edge case with an empty string
def test_empty_input():
    text = ''
    assert len_without_ansi(text) == 0

# Scenario 5: Test error handling for None input
def test_none_input():
    text = None
    with pytest.raises(TypeError):
        len_without_ansi(text)
