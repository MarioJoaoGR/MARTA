
import pytest
from pymonet.lazy import Lazy
from decimal import Decimal

def square(x):
    return x * x

class TestLazy:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.lazy = Lazy(square)
        self.result = None

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            # Attempt to call get() method with invalid input type (e.g., a string instead of an integer)
            result = self.lazy.get("invalid")
