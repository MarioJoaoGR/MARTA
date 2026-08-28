
import pytest
from concurrent.futures import Future
from tornado.concurrent import future_set_exc_info
import unittest.mock as mock


def test_future_set_exc_info_without_exception():
    with pytest.raises(Exception):
        my_future = Future()
        future_set_exc_info(my_future, (None, None, None))