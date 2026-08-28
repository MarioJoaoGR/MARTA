
import pytest
from pypara.monetary import NonePrice, SomePrice



def test_invalid_input():
    with pytest.raises(NameError):
        raise NameError("This is a test error")