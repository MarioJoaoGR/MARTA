
import functools
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator, overload
import multiprocessing as mp
import threading
from collections import defaultdict
from tqdm import tqdm
from flutes.multiproc import ProgressBarManager, Event, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent

class ProgressBarManager:
    """A manager for `tqdm <https://tqdm.github.io/>`_ progress bars that allows maintaining multiple bars from multiple worker processes.
    
    The class provides a way to create and manage progress bars across different threads or processes, ensuring that updates are handled correctly even when running in parallel environments. It supports both manual and automatic updating of progress based on the length of the iterable provided.
    
    Args:
        verbose (bool): If ``False``, all progress bars are disabled. Defaults to ``True``.
        kwargs: Default arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
        
    Examples:
        To use the ProgressBarManager, you can create an instance and then use its methods to manage progress bars in different worker processes or threads. Here's a basic example of how to set up and use it:
        
        ```python
        import time
        import random
        from tqdm import tqdm
        from flutes import ProgressBarManager, safe_pool
        
        def run(xs, bar):
            # Create a new progress bar for the current worker.
            bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
            result = 0
            for idx, x in enumerate(xs):
                result += x
                time.sleep(random.uniform(0.01, 0.2))
                bar.update(1, postfix={"sum": result})  # update progress
                if (idx + 1) % 100 == 0:
                    flutes.log(f"Processed {idx + 1} samples")
            return result
        
        manager = ProgressBarManager()
        run_fn = functools.partial(run, bar=manager.proxy)
        with safe_pool(4) as pool:
            for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
                flutes.log(f"Processed {idx + 1} arrays")
        ```
        
        In this example, `ProgressBarManager` is used to manage progress bars across multiple worker processes. The `run` function is designed to be run in parallel and updates its progress bar accordingly.
    """
    
    def __init__(self, verbose: bool = True, **kwargs):
        self.verbose = verbose
        if not verbose:
            self._proxy: 'ProgressBarManager.Proxy' = self._DummyProxy()
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

    def _run(self):
        from tqdm import tqdm
        while True:
            try:
                event = self.queue.get()
                if isinstance(event, NewEvent):
                    position = self.worker_id_map[event.worker_id]
                    self._close_bar(event.worker_id)
                    kwargs = {**self.bar_kwargs, **event.kwargs, "leave": False, "position": position}
                    bar = tqdm(**kwargs)
                    self.progress_bars[event.worker_id] = bar
                elif isinstance(event, UpdateEvent):
                    bar = self.progress_bars[event.worker_id]
                    if event.postfix is not None:
                        # Only force refresh if we're only setting the postfix.
                        bar.set_postfix(event.postfix, refresh=event.n == 0)
                    bar.update(event.n)
                elif isinstance(event, WriteEvent):
                    tqdm.write(event.message)
                elif isinstance(event, CloseEvent):
                    self._close_bar(event.worker_id)
                elif isinstance(event, QuitEvent):
                    break
                else:
                    assert False
            except (KeyboardInterrupt, SystemExit):
                raise
            except (EOFError, BrokenPipeError):
                break
            except:
                traceback.print_exc(file=sys.stderr)
                
    class Proxy:
        """Proxy class for the progress bar manager. Subprocesses should communicate with the progress bar manager through this class."""
    
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:12:0: E0102: class already defined line 10 (function-redefined)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:68:8: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:70:37: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:79:20: E1101: Instance of 'ProgressBarManager' has no '_close_bar' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:92:20: E1101: Instance of 'ProgressBarManager' has no '_close_bar' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:102:16: E1101: Class 'traceback' has no 'print_exc' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:102:16: E0602: Undefined variable 'traceback' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:102:41: E0602: Undefined variable 'sys' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:111:41: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:111:106: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:143:43: E0602: Undefined variable 'get_worker_id' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:146:53: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:146:92: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:159:58: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:159:112: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:175:46: E0602: Undefined variable 'get_worker_id' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:179:45: E0602: Undefined variable 'get_worker_id' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_valid_inputs.py:183:45: E0602: Undefined variable 'get_worker_id' (undefined-variable)


"""