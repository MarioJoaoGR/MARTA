
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPoolType

@pytest.fixture(scope="module")
def pool():
    return StatefulPoolType()

def test_invalid_input(pool):
    with pytest.raises(TypeError):
        # This should raise a TypeError because the function does not take any arguments
        results = pool.imap(lambda state, x: x * 2)
