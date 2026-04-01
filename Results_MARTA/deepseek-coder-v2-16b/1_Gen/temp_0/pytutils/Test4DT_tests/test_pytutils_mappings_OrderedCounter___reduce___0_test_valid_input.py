
import pytest
from collections import OrderedDict, Counter

class OrderedCounter(OrderedDict):
    """
    An ordered dictionary can be combined with the Counter class so that the counter remembers the order elements are first encountered.
    
    From Python stdlib in `collections`.
    """
    def __reduce__(self):
        return self.__class__, (OrderedDict(self), )

def test_valid_input():
    oc = OrderedCounter()
    oc['a'] = 1
    oc['b'] = 2
    
    # Serialize the OrderedCounter instance
    import pickle
    serialized_oc = pickle.dumps(oc)
    
    # Deserialize the instance
    deserialized_oc = pickle.loads(serialized_oc)
    
    # Assert that the deserialized instance is equal to the original
    assert isinstance(deserialized_oc, OrderedCounter)
    assert dict(deserialized_oc) == {'a': 1, 'b': 2}
