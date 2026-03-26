
import pytest
from pytutils.meth import bind

def test_edge_case():
    class Foo(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    foo = None  # This should trigger an error since `foo` is not a valid instance
    my_unbound_method = lambda self: self.x * self.y

    with pytest.raises(AttributeError):
        bind(foo, my_unbound_method, 'multiply')
