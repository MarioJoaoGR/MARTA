
import pytest
from pysnooper.tracer import Tracer

class UnavailableSource:
    def __getitem__(self, i):
        return u'SOURCE IS UNAVAILABLE'

def test_none_index():
    unavailable = UnavailableSource()
    result = unavailable[None]
    assert result == 'SOURCE IS UNAVAILABLE'

def test_string_index():
    unavailable = UnavailableSource()
    result = unavailable["some_string"]
    assert result == 'SOURCE IS UNAVAILABLE'

def test_float_index():
    unavailable = UnavailableSource()
    result = unavailable[3.14]
    assert result == 'SOURCE IS UNAVAILABLE'
