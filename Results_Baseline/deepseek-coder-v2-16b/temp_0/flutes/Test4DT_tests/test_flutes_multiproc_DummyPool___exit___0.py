
# Test case  

# Test case  
# Module: flutes.multiproc
import pytest
from multiprocessing import Pool
import flutes.multiproc

# Test creating a DummyPool instance with zero processes
def test_dummy_pool_zero_processes():
    pool = flutes.multiproc.DummyPool(processes=0)
    assert isinstance(pool, flutes.multiproc.DummyPool)

# Test using the Pool to map a function over an iterable
def my_function(x):
    return x * 2

@pytest.mark.parametrize("test_input, expected", [(i, i*2) for i in range(5)])
def test_map(test_input, expected):
    pool = flutes.multiproc.DummyPool(processes=0)
    results = pool.map(my_function, [test_input])
    assert results[0] == expected

# Test applying a function asynchronously
@pytest.mark.parametrize("test_input, expected", [(i, i*2) for i in range(5)])
def test_apply_async(test_input, expected):
    pool = flutes.multiproc.DummyPool(processes=0)
    result = pool.apply_async(my_function, args=(test_input,))
    assert result.get() == expected

# Test using starmap to apply a function over tuples of arguments
@pytest.mark.parametrize("test_input, expected", [((i, 2), i*2) for i in range(5)])
def test_starmap(test_input, expected):
    pool = flutes.multiproc.DummyPool(processes=0)
    results = pool.starmap(lambda x, y: x * y, [test_input])
    assert results[0] == expected

# Test using imap to apply a function lazily
@pytest.mark.parametrize("test_input, expected", [(i, i*2) for i in range(5)])
def test_imap(test_input, expected):
    pool = flutes.multiproc.DummyPool(processes=0)
    results = list(pool.imap(lambda x: x * 2, [test_input]))
    assert results[0] == expected

# Test using imap_unordered to apply a function unorderedly
@pytest.mark.parametrize("test_input, expected", [(i, i*2) for i in range(5)])
def test_imap_unordered(test_input, expected):
    pool = flutes.multiproc.DummyPool(processes=0)
    results = list(pool.imap_unordered(lambda x: x * 2, [test_input]))