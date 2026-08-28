
import pytest
from tornado.queues import Queue
from unittest.mock import patch


def test_invalid_maxsize():
    with pytest.raises(ValueError):
        q = Queue(maxsize=-1)