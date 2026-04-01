
import pytest
from flutes.multiproc import safe_pool, get_worker_id
from tqdm import tqdm
import time
import random
from typing import List, Iterable, Dict, Any, Optional, Union, overload, Iterator

class ProgressBarManager:
    """A manager for `tqdm <https://tqdm.github.io/>`_ progress bars that allows maintaining multiple bars from multiple worker processes."""
    
    def __init__(self, verbose: bool = True, **kwargs):
        self.verbose = verbose
        if not verbose:
            self._proxy = self._DummyProxy()
            return

        self.manager = mp.Manager()
        self.queue: 'mp.Queue[Event]' = self.manager.Queue(-1)  # type: ignore[assignment]
        self.progress_bars: Dict[Optional[int], 'tqdm'] = {}
        self.worker_id_map: Dict[Optional[int], int] = defaultdict(lambda: len(self.worker_id_map))
        self.bar_kwargs = kwargs.copy()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
        self._proxy = self.Proxy(self.queue)

        from .log import set_console_logging_function, _get_console_logging_function
        self._original_console_logging_fn = _get_console_logging_function()
        set_console_logging_function(self.proxy.write)

    def __enter__(self):
        return self

    class Proxy:
        """Proxy class for the progress bar manager."""
        
        def __init__(self, queue: 'mp.Queue[Event]'):
            self.queue = queue

        @overload
        def new(self, iterable: Iterable[T], update_frequency: Union[int, float]=1, **kwargs) -> Iterator[T]:
            ...
        
        @overload
        def new(self, iterable: Literal[None] = None, update_frequency: Union[int, float] = 1, **kwargs) -> 'tqdm':
            ...
        
        def new(self, iterable=None, update_frequency=1, **kwargs):
            """Construct a new progress bar."""
            length = kwargs.get('total', None)
            ret_val = self
            if iterable is not None:
                try:
                    iter_len = len(iterable)
                    if length is None:
                        length = iter_len
                        kwargs.update(total=iter_len)
                    elif length != iter_len:
                        import warnings
                        warnings.warn(f'Iterable has length {iter_len} but total={length} is specified')
                except TypeError:
                    pass
                if isinstance(update_frequency, float):
                    if length is None:
                        raise ValueError('`iterable` must have valid length, or `total` must be specified if `update_frequency` is float')
                    if not 0.0 < update_frequency <= 1.0:
                        raise ValueError('`update_frequency` must be within the range (0, 1]')
                    ret_val = self._iter_per_percentage(iterable, length, update_frequency)
                else:
                    if not 0 < update_frequency:
                        raise ValueError('`update_frequency` must be positive')
                    ret_val = self._iter_per_elems(iterable, update_frequency)
            self.queue.put_nowait(NewEvent(get_worker_id(), kwargs))
            return ret_val
        
        def _iter_per_elems(self, iterable: Iterable[T], update_frequency: int) -> Iterator[T]:
            prev_index = -1
            next_index = update_frequency - 1
            idx = 0
            for idx, x in enumerate(iterable):
                yield x
                if idx == next_index:
                    self.update(idx - prev_index)
                    next_index += update_frequency
                    prev_index = idx
            if idx > prev_index:
                self.update(idx - prev_index)
        
        def _iter_per_percentage(self, iterable: Iterable[T], length: int, update_frequency: float) -> Iterator[T]:
            update_count = 0
            prev_index = -1
            next_index = max(0, int(update_frequency * length) - 1)
            for idx, x in enumerate(iterable):
                yield x
                if idx == next_index:
                    self.update(idx - prev_index)
                    update_count += 1
                    next_index = max(idx + 1, int(update_frequency * (update_count + 1) * length) - 1)
                    prev_index = idx
            if length > prev_index + 1:
                self.update(length - prev_index - 1)
        
        def update(self, n: int = 0, *, postfix: Optional[Dict[str, Any]] = None) -> None:
            """Update progress for the current progress bar."""
            self.queue.put_nowait(UpdateEvent(get_worker_id(), n, postfix))
        
        def write(self, message: str) -> None:
            """Write a message to console without disrupting the progress bars."""
            self.queue.put_nowait(WriteEvent(get_worker_id(), message))
        
        def close(self) -> None:
            """Close the current progress bar."""
            self.queue.put_nowait(CloseEvent(get_worker_id()))
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.close()
    
    class _DummyProxy(Proxy):
        def __init__(self):
            pass
        
        def new(self, iterable=None, **kwargs):
            if iterable is not None:
                return iterable
            return self
        
        def update(self, n: int = 0, *, postfix: Optional[Dict[str, Any]] = None) -> None:
            pass
        
        def write(self, message: str) -> None:
            pass
        
        def close(self) -> None:
            pass

def test_edge_cases():
    with pytest.raises(ValueError):
        manager = ProgressBarManager(verbose=False)  # Initialize the manager without verbose mode
        assert isinstance(manager._proxy, ProgressBarManager._DummyProxy)
        
        # Test None input
        with pytest.raises(TypeError):
            run(None, bar=manager.proxy)
        
        # Test empty list
        run([], bar=manager.proxy)
        
        # Test boundary values (e.g., very small or large lists)
        run_fn = functools.partial(run, bar=manager.proxy)
        with flutes.safe_pool(4) as pool:
            for idx, _ in enumerate(pool.imap_unordered(run_fn, [list(range(10)), list(range(1000))])):
                pass
        
        # Test verbose mode enabled
        manager = ProgressBarManager(verbose=True)  # Initialize the manager with verbose mode enabled
        assert not isinstance(manager._proxy, ProgressBarManager._DummyProxy)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:18:23: E0602: Undefined variable 'mp' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:21:55: E0602: Undefined variable 'defaultdict' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:23:22: E0602: Undefined variable 'threading' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:23:46: E1101: Instance of 'ProgressBarManager' has no '_run' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:28:8: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:30:37: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:42:41: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:42:106: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:46:32: E0602: Undefined variable 'Literal' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:74:34: E0602: Undefined variable 'NewEvent' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:77:53: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:77:92: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:90:58: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:90:112: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:106:34: E0602: Undefined variable 'UpdateEvent' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:110:34: E0602: Undefined variable 'WriteEvent' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:114:34: E0602: Undefined variable 'CloseEvent' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:147:12: E0602: Undefined variable 'run' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:147:26: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:150:8: E0602: Undefined variable 'run' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:150:20: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:153:17: E0602: Undefined variable 'functools' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:153:35: E0602: Undefined variable 'run' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:153:44: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___2_test_edge_cases.py:154:13: E0602: Undefined variable 'flutes' (undefined-variable)


"""