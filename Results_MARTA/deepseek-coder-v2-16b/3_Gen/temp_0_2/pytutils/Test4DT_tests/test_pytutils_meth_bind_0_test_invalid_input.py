
import pytest
from pytutils.meth import bind

def test_invalid_input():
    instance = 123
    func = lambda self: getattr(self, 'x') * getattr(self, 'y')
    as_name = 'multiply'

    with pytest.raises(AttributeError):
        bind(instance, func, as_name)
