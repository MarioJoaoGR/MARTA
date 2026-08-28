
import pytest
from tornado.locks import BoundedSemaphore
import threading


def test_edge_case():
    with pytest.raises(NameError):
        manager = _ReleasingContextManager(None)