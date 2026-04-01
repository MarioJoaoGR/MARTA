
import functools
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator, overload
import multiprocessing as mp
import threading
from collections import defaultdict
from tqdm import tqdm
from flutes.multiproc import Event, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent

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
                import traceback
                traceback.print_exc()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:55:54: E1101: Instance of 'ProgressBarManager' has no '_DummyProxy' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:66:22: E1101: Instance of 'ProgressBarManager' has no 'Proxy' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:68:8: E0401: Unable to import 'Test4DT_tests.log' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:70:37: E1101: Instance of 'ProgressBarManager' has no 'proxy' member; maybe '_proxy'? (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:79:20: E1101: Instance of 'ProgressBarManager' has no '_close_bar' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_edge_case.py:92:20: E1101: Instance of 'ProgressBarManager' has no '_close_bar' member (no-member)


"""