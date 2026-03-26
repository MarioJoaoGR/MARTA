
import pytest
from multiprocessing import Pool

def wrapped_method(func, *args, **kwargs):
    with Pool(processes=4) as pool:
        result = pool.apply(func, args=args, kwds=kwargs)
        return result

def test_none_input():
    # Test handling None input gracefully
    with pytest.raises(TypeError):
        wrapped_method(None)
