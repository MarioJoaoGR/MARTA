
import pytest
import multiprocessing as mp
from typing import List, Optional, Iterable, Dict, Any, Iterator, Union, Literal
import time
import random
import functools
import flutes

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
    
        @pytest.mark.parametrize("iterable", [None, []])
        @pytest.mark.parametrize("update_frequency", [1, 0.01, 0.5])
        def test_invalid_input(self, iterable, update_frequency):
            with pytest.raises(TypeError):
                self.new(iterable=iterable, update_frequency=update_frequency)
    
    class _DummyProxy(Proxy):
    
        def __init__(self):
            pass
    
        def new(self, iterable=None, **kwargs):
            if iterable is not None:
                return iterable
            return self
    
        def update(self, n: int=0, *, postfix: Optional[Dict[str, Any]]=None) ->None:
            pass
    
        def write(self, message: str) ->None:
            pass
    
        def close(self) ->None:
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
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:64:16: E1101: Instance of 'Proxy' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:94:55: E0602: Undefined variable 'defaultdict' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:96:22: E0602: Undefined variable 'threading' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:96:46: E1101: Instance of 'ProgressBarManager' has no '_run' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:101:8: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:103:37: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_invalid_input.py:106:8: E1101: Instance of 'ProgressBarManager' has no 'close' member (no-member)


"""