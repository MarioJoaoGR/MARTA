
import pytest
from pytutils.iters import dedupe_iter

def test_dedupe():
    # Define a sample function to be decorated
    def sample_func():
        return [1, 2, 3, 2, 1]
    
    # Apply the decorator and check the output
    @pytest.mark.parametrize("f, args, expected", [(sample_func, (), [1, 2, 3])])
    def test_dedupe(f, args, expected):
        gen = f(*args)
        deduped_gen = dedupe_iter(gen)
        assert list(deduped_gen) == expected
