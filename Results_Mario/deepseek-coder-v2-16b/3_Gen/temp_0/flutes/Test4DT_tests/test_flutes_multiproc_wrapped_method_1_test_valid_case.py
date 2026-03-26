
import pytest
from multiprocessing import Pool

def multiply(a, b):
    return a * b

def wrapped_method(func, *args, **kwargs):
    with Pool(processes=4) as pool:
        result = pool.apply(func, args=args, kwds=kwargs)
        return result

@pytest.mark.parametrize("a, b, expected", [(5, 10, 50), (3, 7, 21)])
def test_valid_case(a, b, expected):
    assert wrapped_method(multiply, a, b=b) == expected
