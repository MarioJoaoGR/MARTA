
import pytest
from flutes.multiproc import StatefulPool
from multiprocessing import Pool

def test_edge_case():
    with pytest.raises(TypeError):
        pool = StatefulPool(None, None, (None,), (), {})
