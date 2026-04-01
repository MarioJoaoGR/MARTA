
import pytest
from multiprocessing import Pool, DummyPool
from typing import List, Callable, Iterable, Mapping, Any, Set, Optional, Tuple, Type
import inspect
import functools
import mp

class StatefulPool:
    _pool: 'PoolType'
    _state_class: Type[State]
    _class_methods: Set[int]
    
    def __init__(self, pool_class: Type['PoolType'], state_class: Type[State], state_init_args: Tuple[Any, ...],
                 args: Tuple[Any, ...], kwargs: Dict[str, Any]):
        self._state_class = state_class
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
    
    def __init__(self, pool_class: Type['PoolType'], state_class: Type[State], state_init_args: Tuple[Any, ...],
                 args: Tuple[Any, ...], kwargs: Dict[str, Any]):
        self._state_class = state_class
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
    
    def broadcast(self, fn: Callable[[State], R], *, args: Iterable[Any] = (), kwds: Mapping[str, Any] = {}) -> List[R]:
        r"""Broadcast a function to each pool worker, and gather results.

        :param fn: The function to broadcast.
        :param args: Positional arguments to apply to the function.
        :param kwds: Keyword arguments to apply to the function.
        :return: The broadcast result from each worker process. Order is arbitrary.
        """
        if self._pool._state != mp.pool.RUN:
            raise ValueError("Pool not running")
        _ = self._wrap_fn(fn, allow_function=False)  # ensure that the function is an unbound method
        if isinstance(self._pool, DummyPool):
            return [fn(self._pool._process_state, *args, **kwds)]
        assert isinstance(self._pool, Pool)
        
        received_ids: Set[int] = set()
        n_processes = self._pool._processes
        broadcast_init_fn = functools.partial(_pool_fn_with_state, self._init_broadcast)
        while len(received_ids) < n_processes:
            init_ids: List[int] = self._pool.map(broadcast_init_fn, range(n_processes))  # type: ignore[arg-type]
            received_ids.update(init_ids)
        
        broadcast_results = []
        broadcast_handler_fn = functools.partial(_pool_fn_with_state, self._apply_broadcast)
        while len(received_ids) < n_processes:
            results: List[Optional[Tuple[R, int]]] = self._pool.map(
                broadcast_handler_fn, [fn] * n_processes, args=args, kwds=kwds)  # type: ignore[arg-type]
            for result in results:
                if result is not None:
                    ret, worker_id = result
                    received_ids.add(worker_id)
                    broadcast_results.append(ret)
        return broadcast_results

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:3:0: E0611: No name 'DummyPool' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:7:0: E0401: Unable to import 'mp' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:11:23: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:14:71: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:15:48: E0602: Undefined variable 'Dict' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:37:42: E0602: Undefined variable '_pool_state_init' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:41:44: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:54:29: E1101: Instance of 'StatefulPool' has no '_define_method' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:57:4: E0102: method already defined line 14 (function-redefined)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:57:71: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:58:48: E0602: Undefined variable 'Dict' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:80:42: E0602: Undefined variable '_pool_state_init' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:84:44: E0602: Undefined variable '_chain_fns' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:97:29: E1101: Instance of 'StatefulPool' has no '_define_method' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:100:38: E0602: Undefined variable 'State' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:100:46: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:100:117: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:110:12: E1101: Instance of 'StatefulPool' has no '_wrap_fn' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:117:46: E0602: Undefined variable '_pool_fn_with_state' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:117:67: E1101: Instance of 'StatefulPool' has no '_init_broadcast' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:123:49: E0602: Undefined variable '_pool_fn_with_state' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:123:70: E1101: Instance of 'StatefulPool' has no '_apply_broadcast' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_0_test_edge_case.py:125:41: E0602: Undefined variable 'R' (undefined-variable)


"""