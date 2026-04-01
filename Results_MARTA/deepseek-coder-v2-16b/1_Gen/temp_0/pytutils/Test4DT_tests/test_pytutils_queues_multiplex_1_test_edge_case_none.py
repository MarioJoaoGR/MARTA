
import pytest
from queue import Queue
from pytutils.queues import multiplex

def test_edge_case_none():
    q = None
    try:
        q1, q2, q3 = multiplex(q, count=3)
    except TypeError as e:
        pass
