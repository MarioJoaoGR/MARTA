
import pytest
from pypara.monetary import SomePrice


def test_error_case_different_class_input():
    class DifferentClass:
        pass
    
    with pytest.raises(TypeError):
        price1 = SomePrice(100, 2)