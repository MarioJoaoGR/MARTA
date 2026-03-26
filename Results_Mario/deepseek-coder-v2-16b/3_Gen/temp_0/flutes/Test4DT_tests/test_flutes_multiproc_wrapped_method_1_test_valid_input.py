
import pytest
from multiprocessing import Pool

def multiply(a, b):
    return a * b

def wrapped_method(func, *args, **kwargs):
    with Pool(processes=4) as pool:
        result = pool.apply(func, args=args, kwds=kwargs)
        return result

@pytest.mark.parametrize("a, b, expected", [
    (5, 10, 50),
    (2, 3, 6),
    (7, 8, 56),
])
def test_valid_input(a, b, expected):
    result = wrapped_method(multiply, a, b=b)
    assert result == expected
