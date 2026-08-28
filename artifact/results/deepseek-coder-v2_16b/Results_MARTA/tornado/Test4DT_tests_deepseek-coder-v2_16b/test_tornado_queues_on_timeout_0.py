
import pytest
from tornado.queues import Future


def test_edge_case_none():
    future = None
    with pytest.raises(NameError):
        on_timeout()
