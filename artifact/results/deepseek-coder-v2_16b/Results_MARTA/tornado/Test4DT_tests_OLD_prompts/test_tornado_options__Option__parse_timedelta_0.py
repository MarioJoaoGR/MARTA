
import pytest
from unittest.mock import patch, MagicMock
from typing import Any, Optional, Callable
import datetime
import re

class _Option:
    UNSET = object()
    _DATETIME_FORMATS = ['%a %b %d %H:%M:%S %Y', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%dT%H:%M', '%Y%m%d %H:%M:%S', '%Y%m%d %H:%M', '%Y-%m-%d', '%Y%m%d', '%H:%M:%S', '%H:%M']
    _TIMEDELTA_ABBREV_DICT = {'h': 'hours', 'm': 'minutes', 'min': 'minutes', 's': 'seconds', 'sec': 'seconds', 'ms': 'milliseconds', 'us': 'microseconds', 'd': 'days', 'w': 'weeks'}
    _FLOAT_PATTERN = '[-+]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][-+]?\\d+)?'
    _TIMEDELTA_PATTERN = re.compile('\\s*(%s)\\s*(\\w*)\\s*' % _FLOAT_PATTERN, re.IGNORECASE)
    
    def __init__(self, name: str, default: Any = None, type: Optional[type] = None, help: Optional[str] = None, metavar: Optional[str] = None, multiple: bool = False, file_name: Optional[str] = None, group_name: Optional[str] = None, callback: Optional[Callable[[Any], None]] = None) -> None:
        if default is None and multiple:
            default = []
        self.name = name
        if type is None:
            raise ValueError("type must not be None")
        self.type = type
        self.help = help
        self.metavar = metavar
        self.multiple = multiple
        self.file_name = file_name
        self.group_name = group_name
        self.callback = callback
        self.default = default
        self._value = _Option.UNSET  # type: Any
    
    def _parse_timedelta(self, value: str) -> datetime.timedelta:
        try:
            sum = datetime.timedelta()
            start = 0
            while start < len(value):
                m = self._TIMEDELTA_PATTERN.match(value, start)
                if not m:
                    raise Exception()
                num = float(m.group(1))
                units = m.group(2) or "seconds"
                units = self._TIMEDELTA_ABBREV_DICT.get(units, units)
                sum += datetime.timedelta(**{units: num})
                start = m.end()
            return sum
        except Exception:
            raise

# Test for _Option initialization with default value and type check
def test__Option_init_with_default_and_type():
    opt = _Option(name="example_option", type=int, default=10)
    assert opt.name == "example_option"
    assert isinstance(opt.default, int)
    assert opt.default == 10
    with pytest.raises(ValueError):
        _Option(name="example_option", type=None)

# Test for parsing a timedelta string
def test__Option_parse_timedelta():
    opt = _Option(name="duration", type=str)
    parsed_delta = opt._parse_timedelta("2 hours 30 minutes")
    assert isinstance(parsed_delta, datetime.timedelta)
    assert parsed_delta.total_seconds() == 2 * 3600 + 30 * 60

# Test for handling invalid timedelta strings
def test__Option_parse_invalid_timedelta():
    opt = _Option(name="duration", type=str)
    with pytest.raises(Exception):
        opt._parse_timedelta("invalid input")
