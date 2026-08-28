
import pytest
from flutes.iterator import drop

def test_drop_negative_n():
    """Test that passing a negative value for n raises a ValueError."""
    with pytest.raises(ValueError):
        list(drop(-1, [1, 2, 3]))

def test_drop_negative_n_with_string():
    """Test that passing a negative value for n raises a ValueError with a string iterable."""
    with pytest.raises(ValueError):
        ''.join(drop(-5, "hello"))

def test_drop_negative_n_with_range():
    """Test that passing a negative value for n raises a ValueError with a range iterable."""
    with pytest.raises(ValueError):
        list(drop(-3, range(10)))

def test_drop_negative_n_with_generator_expression():
    """Test that passing a negative value for n raises a ValueError with a generator expression."""
    gen = (x * x for x in range(10))
    with pytest.raises(ValueError):
        list(drop(-2, gen))
