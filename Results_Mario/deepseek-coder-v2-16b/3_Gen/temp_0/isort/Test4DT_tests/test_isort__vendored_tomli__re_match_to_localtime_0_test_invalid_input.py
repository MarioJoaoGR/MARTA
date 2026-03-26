
import re
from time import time

def match_to_localtime(match: "re.Match") -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), int(sec_str), micros)

def test_invalid_input():
    pattern = r'(\d{2}):(\d{2}):(\d{2})\.(\d{6})'
    match_obj = re.match(pattern, 'invalid input')
    assert match_obj is None
