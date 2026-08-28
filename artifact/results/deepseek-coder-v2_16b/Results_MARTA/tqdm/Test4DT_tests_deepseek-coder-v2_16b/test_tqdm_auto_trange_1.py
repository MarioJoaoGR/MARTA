
import pytest
from tqdm.auto import trange

def test_edge_cases():
    with pytest.raises(TypeError):
        for i in trange(None):
            pass

def test_invalid_inputs():
    with pytest.raises(TypeError):
        for i in trange("string"):
            pass

def test_trange_with_list():
    with pytest.raises(TypeError):
        for i in trange([]):
            pass
