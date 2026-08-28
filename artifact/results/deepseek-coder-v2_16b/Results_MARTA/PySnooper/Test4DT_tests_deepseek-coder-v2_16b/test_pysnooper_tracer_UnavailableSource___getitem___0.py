
import pytest
from pysnooper.tracer import Tracer

class UnavailableSource:
    def __getitem__(self, i):
        return u'SOURCE IS UNAVAILABLE'

@pytest.fixture(scope="module")
def unavailable_source():
    return UnavailableSource()

def test_unavailable_source_getitem(unavailable_source):
    assert unavailable_source[0] == 'SOURCE IS UNAVAILABLE'
    assert unavailable_source[1] == 'SOURCE IS UNAVAILABLE'
    assert unavailable_source[100] == 'SOURCE IS UNAVAILABLE'
