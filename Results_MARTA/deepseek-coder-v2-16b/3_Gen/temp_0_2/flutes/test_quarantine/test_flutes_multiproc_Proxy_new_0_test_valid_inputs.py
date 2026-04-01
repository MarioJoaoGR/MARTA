
import multiprocessing as mp
from flutes.multiproc import Event, get_worker_id

class Proxy:
    """Proxy class for the progress bar manager. Subprocesses should communicate with the progress bar manager through this class.
    
    This class provides a method to create and manage a progress bar. The progress bar can be updated based on either the percentage of completion or a fixed number of iterations, depending on the provided parameters. It also allows for additional keyword arguments that customize the behavior of the progress bar as per the `tqdm <https://tqdm.github.io/>`_ library.
    
    Parameters:
        queue (mp.Queue[Event]): A multiprocessing queue used to communicate with the progress bar manager.
        
    Methods:
        new(iterable=None, update_frequency=1, **kwargs): Constructs a new progress bar.
            - iterable (optional): The iterable object to be wrapped by the progress bar. If provided, it should have a valid length attribute or specify a total count for updates.
            - update_frequency (int or float, optional): Determines how often the progress bar is updated. If an integer, it specifies the number of iterations per update. If a float, it represents the percentage of completion per update. Must be within the range (0, 1] if provided as a float.
            - kwargs: Additional keyword arguments to configure the tqdm progress bar. These can override default settings in `ProgressBarManager`.
        
        Returns:
            The wrapped iterable or the proxy class itself, depending on whether an iterable was provided.
    
    Example:
        To create a progress bar for an iterable with automatic updates based on percentage completion:
        ```python
        pb = Proxy(queue)
        result = pb.new([1, 2, 3, 4, 5], update_frequency=0.1)
        # The progress bar will update every time the iterable progresses by 10%.
        ```
        
        To manually manage updates for an iterable:
        ```python
        pb = Proxy(queue)
        result = pb.new()
        for i in range(100):
            # Manually update the progress bar
            result.update()
        ```
    """
    def __init__(self, queue: 'mp.Queue[Event]'):
        self.queue = queue

    def new(self, iterable=None, update_frequency=1, **kwargs):
        r"""Construct a new progress bar.
        
        :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually managed with calls to :meth:`update`.
        :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable` is not ``None``:

            - If :attr:`update_frequency` is a float, then the progress bar is updated whenever the iterable progresses over that percentage of elements. For instance, a value of 0.1 results in an update per 10% of progress. Requires a sized iterable (having a valid ``__len__``).
            - If :attr:`update_frequency` is an int, then the progress bar is updated whenever the iterable progresses over that many elements. For instance, a value of 10 results in an update per 10 elements.
        :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer. These can override the default arguments set in the constructor of `ProgressBarManager`.
        :return: The wrapped iterable, or the proxy class itself.
        """
        length = kwargs.get("total", None)
        ret_val = self
        if iterable is not None:
            try:
                iter_len = len(iterable)
                if length is None:
                    length = iter_len
                    kwargs.update(total=iter_len)
                elif length != iter_len:
                    import warnings
                    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")
            except TypeError:
                pass
            if isinstance(update_frequency, float):
                if length is None:
                    raise ValueError("`iterable` must have valid length, or `total` must be specified "
                                     "if `update_frequency` is float")
                if not (0.0 < update_frequency <= 1.0):
                    raise ValueError("`update_frequency` must be within the range (0, 1]")
                ret_val = self._iter_per_percentage(iterable, length, update_frequency)
            else:
                if not (0 < update_frequency):
                    raise ValueError("`update_frequency` must be positive")
                ret_val = self._iter_per_elems(iterable, update_frequency)
        self.queue.put_nowait(NewEvent(get_worker_id(), kwargs))
        return ret_val

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_new_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_valid_inputs.py:72:26: E1101: Instance of 'Proxy' has no '_iter_per_percentage' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_valid_inputs.py:76:26: E1101: Instance of 'Proxy' has no '_iter_per_elems' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_valid_inputs.py:77:30: E0602: Undefined variable 'NewEvent' (undefined-variable)


"""