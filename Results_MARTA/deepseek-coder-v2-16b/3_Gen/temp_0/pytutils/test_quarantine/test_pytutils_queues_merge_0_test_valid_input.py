
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import merge

def test_valid_input():
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    
    # Push some items into the queues
    q1.put(1)
    q2.put(2)
    q3.put(3)
    
    out_q = merge(q1, q2, q3)
    
    assert not out_q.empty()
    assert out_q.get() == 1
    assert out_q.get() == 2
    assert out_q.get() == 3
    assert out_q.empty()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""