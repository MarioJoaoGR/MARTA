
import pytest

class UnavailableSource:
    def __getitem__(self, i):
        return u'SOURCE IS UNAVAILABLE'

def test_getitem_with_string_index():
    unavailable = UnavailableSource()
    assert unavailable["some_string"] == u'SOURCE IS UNAVAILABLE'

def test_getitem_with_none_index():
    unavailable = UnavailableSource()
    assert unavailable[None] == u'SOURCE IS UNAVAILABLE'

def test_getitem_with_float_index():
    unavailable = UnavailableSource()
    assert unavailable[3.14] == u'SOURCE IS UNAVAILABLE'

def test_getitem_with_integer_index():
    unavailable = UnavailableSource()
    assert unavailable[0] == u'SOURCE IS UNAVAILABLE'

def test_getitem_with_negative_integer_index():
    unavailable = UnavailableSource()
    assert unavailable[-1] == u'SOURCE IS UNAVAILABLE'
