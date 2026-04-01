
import pytest
from multiprocessing import Pool, PoolState
from typing import Type, List, Tuple, Dict, Any, Set, Callable
import inspect
import functools

class StatefulPool:
    _pool: 'PoolType'
    _state_class: Type[State]
    _class_methods: Set[int]

    def __init__(self, pool_class: Type['PoolType'], state_class: Type[State], state_init_args: Tuple[Any, ...],
                 args: Tuple[Any, ...], kwargs: Dict[str, Any]):
        self._state_class = state_class

        # Store the IDs of all methods of the `PoolState` subclass.
        self._class_methods = set()
        for attr_name in dir(self._state_class):
            attr_val = getattr(self._state_class, attr_name)
            if inspect.isfunction(attr_val):
                self._class_methods.add(id(attr_val))

        def get_arg(pos: int, name: str, default=None):
            if len(args) > pos + 1:
                return args[pos]
            if name in kwargs:
                return kwargs[name]
            return default

        def set_arg(pos: int, name: str, val):
            nonlocal args
            if len(args) > pos + 1:
                args = args[:pos] + (val,) + args[(pos + 1):]
            else:
                kwargs[name] = val

        state_init_fn = functools.partial(_pool_state_init, state_class)
        # If there's a user-defined initializer function...
        initializer = get_arg(1, "initializer", None)
        init_args = get_arg(2, "initargs", ())
        if initializer is not None:
            initializer = functools.partial(_chain_fns, fns=[state_init_fn, initializer])
            init_args = [(state_init_args, {}), (init_args, {})]
        else:
            initializer = state_init_fn
            init_args = state_init_args
        set_arg(1, "initializer", initializer)
        set_arg(2, "initargs", init_args)

        self._pool = pool_class(*args, **kwargs)

        for name in ["imap", "imap_unordered", "map", "map_async", "starmap", "starmap_async",
                     "apply", "apply_async", "gather"]:
            pool_method = getattr(self._pool, name)
            wrapped_method = self._define_method(pool_method)
            setattr(self, name, wrapped_method)

    def get_states(self) -> List[State]:
        r"""Return the states of each pool worker.

        :return: A list of state for each worker process. Order is arbitrary.
        """
        return self.broadcast(self._state_class.__return_state__)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:10:23: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:13:71: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:38:42: E0602: Undefined variable '_pool_state_init' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:43:44: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:56:29: E1101: Instance of 'StatefulPool' has no '_define_method' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:59:33: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_get_states_0_test_edge_cases.py:64:15: E1101: Instance of 'StatefulPool' has no 'broadcast' member (no-member)


"""