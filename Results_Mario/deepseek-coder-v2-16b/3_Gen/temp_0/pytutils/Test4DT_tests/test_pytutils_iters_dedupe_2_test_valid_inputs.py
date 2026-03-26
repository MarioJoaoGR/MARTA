
import pytest
from pytutils.iters import dedupe_iter

def test_valid_inputs():
    def my_func():
        return [1, 2, 3, 2, 1]
    
    @pytest.mark.parametrize("input_list", [[1, 2, 3, 2, 1], [1, 2, 3]])
    def test_dedupe(input_list):
        gen = my_func()
        deduped_gen = dedupe_iter(gen)
        assert list(deduped_gen) == [1, 2, 3]
