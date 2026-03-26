
# Module: pytutils.lazy.lazy_regex
# test_lazy_regex.py
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_creation():
    msg = "The provided pattern does not match any known format."
    invalid_pattern = InvalidPattern(msg)
    assert invalid_pattern.msg == msg, f"Expected message to be '{msg}', but got '{invalid_pattern.msg}'"

def test_invalid_pattern_format():
    msg = "Missing required fields in the input data."
    invalid_pattern = InvalidPattern(msg)
    formatted_message = invalid_pattern._fmt % {'msg': invalid_pattern.msg}