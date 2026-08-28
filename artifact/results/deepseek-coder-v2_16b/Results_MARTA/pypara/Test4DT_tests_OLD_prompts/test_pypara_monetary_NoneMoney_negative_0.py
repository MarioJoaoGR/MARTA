
import pytest
from pypara.monetary import NoneMoney



def test_negative_operation():
    nm = NoneMoney()
    negated_nm = nm.negative()
    assert isinstance(negated_nm, NoneMoney), "Negative operation should return the same instance"