
import pytest
from mimesis.providers import Internet


def test_invalid_input():
    with pytest.raises(TypeError):
        internet = Internet()
        # Attempting to call a method that should raise TypeError
        invalid_method = internet.random.choice(None)  # Passing None which is not iterable and should raise TypeError