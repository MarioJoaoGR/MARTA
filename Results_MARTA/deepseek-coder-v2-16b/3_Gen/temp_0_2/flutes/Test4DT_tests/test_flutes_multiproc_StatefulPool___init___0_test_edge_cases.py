
import pytest
from multiprocessing import Pool
from typing import Type, Any, Tuple, Dict
from flutes.multiproc import StatefulPool

@pytest.mark.parametrize("pool_class", [None, 123, "Pool"])
@pytest.mark.parametrize("state_class", [None, 123, "State"])
@pytest.mark.parametrize("state_init_args", [(None,), (123,), ("arg1", "arg2")])
@pytest.mark.parametrize("args", [(), (1,), (1, 2)])
@pytest.mark.parametrize("kwargs", [{}, {"key": "value"}])
def test_edge_cases(pool_class, state_class, state_init_args, args, kwargs):
    with pytest.raises(TypeError):
        StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
