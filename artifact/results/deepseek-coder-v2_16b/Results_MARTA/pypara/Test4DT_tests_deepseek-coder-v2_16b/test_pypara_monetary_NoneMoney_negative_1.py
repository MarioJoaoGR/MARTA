
import pytest
from pypara.monetary import NoneMoney


def test_negative_method():
    nm = NoneMoney()
    negated_nm = nm.negative()
    assert isinstance(negated_nm, NoneMoney), "The negative method should return the same instance of NoneMoney"


def test_float_method():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        float(nm)
