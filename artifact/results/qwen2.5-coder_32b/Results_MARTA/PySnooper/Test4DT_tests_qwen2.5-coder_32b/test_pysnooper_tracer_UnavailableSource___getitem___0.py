
import pytest
from pysnooper.tracer import Tracer

class UnavailableSource:
    def __getitem__(self, i):
        return u'SOURCE IS UNAVAILABLE'

def test_getitem_returns_correct_string():
    unavailable = UnavailableSource()
    assert unavailable[0] == 'SOURCE IS UNAVAILABLE'

def test_getitem_with_positive_index():
    unavailable = UnavailableSource()
    assert unavailable[10] == 'SOURCE IS UNAVAILABLE'

def test_getitem_with_negative_index():
    unavailable = UnavailableSource()
    assert unavailable[-1] == 'SOURCE IS UNAVAILABLE'
