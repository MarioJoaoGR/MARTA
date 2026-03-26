
# Module: pytutils.lazy.lazy_regex
# test_lazy_regex.py
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_creation():
    msg = "Invalid character found in pattern."
    exception = InvalidPattern(msg)
    assert isinstance(exception, InvalidPattern), "Exception should be an instance of InvalidPattern"
    assert exception.msg == msg, f"Expected message to be '{msg}', but got '{exception.msg}'"

def test_invalid_pattern_formatting():
    msg = "Invalid character found in pattern."
    expected_error_message = 'Invalid pattern(s) found. Invalid character found in pattern.'
    exception = InvalidPattern(msg)