
import pytest
from pytutils.queues import Queue
from threading import Thread

def merge(*in_qs, **kwargs):
    """ Merge multiple queues together.

    This function takes any number of queue objects (`in_qs`) and merges them into a single output queue (`out_q`). Additional keyword arguments can be passed to customize the behavior of the merged queue. The merging is performed concurrently using threads. Each thread pushes elements from its respective input queue to the output queue.

    Parameters:
        *in_qs (Queue): One or more queue objects that need to be merged. These should all be instances of `Queue`.
        **kwargs: Keyword arguments to customize the behavior of the merged queue. The only supported keyword argument is 'maxsize', which sets the maximum number of items allowed in the output queue. If not provided, the default maxsize will be used (if applicable).

    Returns:
        Queue: A new queue object that contains elements from all input queues.

    Example:
        >>> q1, q2, q3 = [Queue() for _ in range(3)]
        >>> out_q = merge(q1, q2, q3)
        
    This example creates three empty queues (`q1`, `q2`, and `q3`), merges them into a single output queue (`out_q`), and returns the merged queue.
    """
    if not in_qs:
        raise TypeError("At least one queue must be provided")
    
    out_q = Queue(**kwargs)
    threads = [Thread(target=out_q.put, args=(in_q.get,)) for in_q in in_qs]
    for t in threads:
        t.daemon = True
        t.start()
    return out_q

def test_none_input():
    with pytest.raises(TypeError):
        merge()
