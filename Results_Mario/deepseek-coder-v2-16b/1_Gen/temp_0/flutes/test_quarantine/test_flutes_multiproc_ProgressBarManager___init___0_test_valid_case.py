
import functools
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Iterator, Optional, Dict, Any, Union, Literal
from flutes.multiproc import get_worker_id, NewEvent, UpdateEvent, WriteEvent, CloseEvent

class ProgressBarManager:
    """A manager for `tqdm <https://tqdm.github.io/>`_ progress bars that allows maintaining multiple bars from
        multiple worker processes.
    
        .. code:: python
    
            def run(xs: List[int], *, bar) -> int:
                # Create a new progress bar for the current worker.
                bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
                # Compute-intensive stuff!
                result = 0
                for idx, x in enumerate(xs):
                    result += x
                    time.sleep(random.uniform(0.01, 0.2))
                    bar.update(1, postfix={"sum": result})  # update progress
                    if (idx + 1) % 100 == 0:
                        # Logging works without messing up terminal output.
                        flutes.log(f"Processed {idx + 1} samples")
                return result
    
            def run2(xs: List[int], *, bar) -> int:
                # An alternative way to achieve the same functionalities (though slightly slower):
                result = 0
                for idx, x in enumerate(bar.iter(xs)):
                    result += x
                    time.sleep(random.uniform(0.01, 0.2))
                    bar.update(1, postfix={"sum": result})  # update progress
                    if (idx + 1) % 100 == 0:
                        # Logging works without messing up terminal output.
                        flutes.log(f"Processed {idx + 1} samples")
                return result
    
            manager = flutes.ProgressBarManager()
            # Worker processes interact with the manager through proxies.
            run_fn = functools.partial(run, bar=manager.proxy)
            with flutes.safe_pool(4) as pool:
                for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
                    flutes.log(f"Processed {idx + 1} arrays")
    
        :param verbose: If ``False``, all progress bars are disabled. Defaults to ``True``.
        :param kwargs: Default arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
        """
    class Proxy:
        """Proxy class for the progress bar manager. Subprocesses should communicate with the progress bar manager
            through this class.
            """
    
        def __init__(self, queue: 'mp.Queue[Event]'):
            self.queue = queue
    
        @overload
        def new(self, iterable: Iterable[T], update_frequency: Union[int, float]=1, **kwargs) -> Iterator[T]:
            ...
    
        @overload
        def new(self, iterable: Literal[None] = None, update_frequency: Union[int, float] = 1, **kwargs) -> 'tqdm':
            ...
    
        def new(self, iterable=None, update_frequency=1, **kwargs):
            """Construct a new progress bar.
                
                :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually
                    managed with calls to :meth:`update`.
                :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable`
                    is not ``None``:
    
                    - If :attr:`update_frequency` is a ``float``, then the progress bar is updated whenever the iterable
                      progresses over that percentage of elements. For instance, a value of ``0.01`` results in an update
                      per 1% of progress. Requires a sized iterable (having a valid ``__len__``).
                    - If :attr:`update_frequency` is an ``int``, then the progress bar is updated whenever the iterable
                      progresses over that many elements. For instance, a value of ``10`` results in an update per 10
                      elements.
                :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
                    These can override the default arguments set in the constructor of :class:`ProgressBarManager`.
                :return: The wrapped iterable, or the proxy class itself.
                """
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
                        warnings.warn(
                            f'Iterable has length {iter_len} but total={length} is specified'
                            )
                except TypeError:
                    pass
                if isinstance(update_frequency, float):
                    if length is None:
                        raise ValueError(
                            '`iterable` must have valid length, or `total` must be specified if `update_frequency` is float'
                            )
                    if not 0.0 < update_frequency <= 1.0:
                        raise ValueError(
                            '`update_frequency` must be within the range (0, 1]')
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
            """Update progress for the current progress bar.
    
                :param n: Increment to add to the counter.
                :param postfix: An optional dictionary containing additional stats displayed at the end of the progress bar.
                    See `tqdm.set_postfix <https://tqdm.github.io/docs/tqdm/#set_postfix>`_ for more details.
                """
            self.queue.put_nowait(UpdateEvent(get_worker_id(), n, postfix))
    
        def write(self, message: str) -> None:
            """Write a message to console without disrupting the progress bars.
    
                :param message: The message to write.
                """
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:59:9: E0602: Undefined variable 'overload' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:60:41: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:60:106: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:64:8: E0102: method already defined line 60 (function-redefined)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:63:9: E0602: Undefined variable 'overload' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:67:8: E0102: method already defined line 60 (function-redefined)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:116:53: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:116:92: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:129:58: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:129:112: E0602: Undefined variable 'T' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:197:55: E0602: Undefined variable 'defaultdict' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:199:22: E0602: Undefined variable 'threading' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:199:46: E1101: Instance of 'ProgressBarManager' has no '_run' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:204:8: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_case.py:206:37: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)


"""