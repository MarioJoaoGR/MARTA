
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool
from typing import Type, Any, Tuple, Dict, Set, Type as TypeType
import inspect
import functools

class MyState(object):
    def initializer_function(self, arg1, arg2):
        pass

def _pool_state_init(state_class, *args, **kwargs):
    return state_class(*args, **kwargs)

def _chain_fns(*args, **kwargs):
    fn = kwargs.get('fns', [])[0]
    return fn(*args, **kwargs)

@pytest.mark.parametrize("pool_class, state_class, state_init_args, args, kwargs", [
    (Pool, MyState, ("arg1", "arg2"), ("args_for_pool",), {"kwarg1": "value1"}),
    (int, MyState, ("arg1", "arg2"), ("args_for_pool",), {"kwarg1": "value1"})  # Invalid pool class type
])
def test_invalid_input(pool_class, state_class, state_init_args, args, kwargs):
    with pytest.raises(TypeError):
        StatefulPool(pool_class, state_class, state_init_args, args, kwargs)
