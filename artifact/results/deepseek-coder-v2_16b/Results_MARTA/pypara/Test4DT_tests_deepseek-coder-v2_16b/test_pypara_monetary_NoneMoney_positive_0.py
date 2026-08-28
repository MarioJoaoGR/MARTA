
import pytest
from pypara.monetary import NoneMoney

def test_positive_method():
    nm = NoneMoney()
    result = nm.positive()
    assert isinstance(result, NoneMoney), "Expected a return type of NoneMoney"
    assert result == nm, "Expected the same instance to be returned as positive"
