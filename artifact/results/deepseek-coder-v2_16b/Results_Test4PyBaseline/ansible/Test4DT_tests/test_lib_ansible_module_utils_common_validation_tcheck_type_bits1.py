
# Module: ansible.module_utils.common.validation
# test_validation.py
import re
import pytest
from ansible.module_utils.common.validation import check_type_bits

def human_to_bytes(human, isbits=False):
    """Convert number in string format into bytes (ex: '2K' => 2048) or using unit argument.

    example: human_to_bytes('10M') <=> human_to_bytes(10, 'M').

    When isbits is False (default), converts bytes from a human-readable format to integer.
        example: human_to_bytes('1MB') returns 1048576 (int).
        The function expects 'B' (uppercase) as a byte identifier passed
        as a part of 'name' param string or 'unit', e.g. 'MB'/'KB'/etc.
        (except when the identifier is single 'b', it is perceived as a byte identifier too).
        if 'Mb'/'Kb'/... is passed, the ValueError will be raised.

    When isbits is True, converts bits from a human-readable format to integer.
        example: human_to_bytes('1Mb', isbits=True) returns 1048576 (int) -
        string bits representation was passed and return as a number or bits.
        The function expects 'b' (lowercase) as a bit identifier, e.g. 'Mb'/'Kb'/etc.
        if 'MB'/'KB'/... is passed, the ValueError will be raised.
    """
    m = re.search(r'^\s*(\d*\.?\d*)\s*([A-Za-z]+)?', str(human), flags=re.IGNORECASE)
    if not m:
        raise ValueError("human_to_bytes() can't interpret following string: %s" % human)
    try:
        num = float(m.group(1))
    except Exception:
        raise ValueError("human_to_bytes() can't interpret following number: %s (original input string: %s)" % (m.group(1), human))

    unit = m.group(2)
    suffix_dict = {'b': 1, 'kb': 1024, 'mb': 1024**2, 'gb': 1024**3}
    if isbits:
        suffix_dict = {'b': 1, 'kb': 1024, 'mb': 1024**2, 'gb': 1024**3}
    else:
        suffix_dict = {'b': 1, 'k': 1024, 'm': 1024**2, 'g': 1024**3}
    
    if unit and unit[0].lower() in suffix_dict:
        return int(num * suffix_dict[unit[0].lower()])
    else:
        raise ValueError("Invalid unit")

# Test cases for check_type_bits function
def test_check_type_bits_valid():
    assert check_type_bits('1Mb') == 1048576