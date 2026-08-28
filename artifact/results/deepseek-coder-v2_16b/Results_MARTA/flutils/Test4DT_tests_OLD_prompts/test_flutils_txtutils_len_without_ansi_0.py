
import pytest
from flutils.txtutils import len_without_ansi
from typing import Sequence, List, Tuple
from unittest.mock import patch

# Test scenarios
def test_valid_input_string():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

def test_valid_input_list_of_strings():
    text: List[str] = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text) == 6

def test_valid_input_string_no_ansi():
    text = 'foobar'
    assert len_without_ansi(text) == 6

def test_empty_input():
    text = ''
    assert len_without_ansi(text) == 0

def test_none_input():
    with pytest.raises(TypeError):
        len_without_ansi(None)
