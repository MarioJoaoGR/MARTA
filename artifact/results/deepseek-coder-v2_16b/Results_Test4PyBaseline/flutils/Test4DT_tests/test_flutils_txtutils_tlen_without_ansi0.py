
import pytest
from typing import Sequence
from flutils.txtutils import len_without_ansi

# Test case 1: With a string containing ANSI escape codes
def test_len_without_ansi_string():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

# Test case 2: With a list of strings, each potentially containing ANSI escape codes
def test_len_without_ansi_list():
    text_list = ['\x1b[38;5;209mfoo', 'bar\x1b[0m']
    assert len_without_ansi(text_list) == 6

# Test case 3: With a tuple of strings, each potentially containing ANSI escape codes
def test_len_without_ansi_tuple():
    text_tuple = ('\x1b[38;5;209mfoo', 'bar\x1b[0m')
    assert len_without_ansi(text_tuple) == 6

# Test case 4: With a string that does not contain ANSI escape codes
def test_len_without_ansi_no_ansi():
    text = 'foobar'
    assert len_without_ansi(text) == 6

# Test case 5: With an empty sequence, should return 0
def test_len_without_ansi_empty_sequence():
    seq = []
    assert len_without_ansi(seq) == 0

# Test case 7: With a string that contains multiple ANSI escape codes
def test_len_without_ansi_multiple_ansi():
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;196mbar\x1b[0m'