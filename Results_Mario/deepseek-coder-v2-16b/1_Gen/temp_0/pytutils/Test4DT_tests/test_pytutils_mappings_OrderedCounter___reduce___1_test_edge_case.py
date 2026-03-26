
import pytest
from collections import OrderedDict, Counter

class OrderedCounter(OrderedDict):
    """
    An ordered dictionary can be combined with the Counter class so that the counter remembers the order elements are first encountered.
    
    From Python stdlib in `collections`.
    """
    def __reduce__(self):
        return self.__class__, (OrderedDict(self), )

def test_edge_case():
    oc = OrderedCounter()
    assert isinstance(oc, OrderedCounter)
