
import pytest
from pytutils.queues import Queue
from threading import Thread
from queue import Empty

def merge(*in_qs, **kwargs):
    """ Merge multiple queues together

    >>> q1, q2, q3 = [Queue() for _ in range(3)]
    >>> out_q = merge(q1, q2, q3)
    """
    out_q = Queue(**kwargs)
    threads = [Thread(target=out_q.put, args=(q.get(),)) for q in in_qs]
    for t in threads:
        t.daemon = True
        t.start()
    return out_q

def test_none_input():
    with pytest.raises(TypeError):
        merge()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""