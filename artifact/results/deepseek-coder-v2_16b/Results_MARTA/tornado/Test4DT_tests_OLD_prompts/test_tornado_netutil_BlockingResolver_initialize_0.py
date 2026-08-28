
import pytest
from tornado.netutil import BlockingResolver
import socket
import unittest.mock as mock



def test_initialize_method():
    resolver = BlockingResolver()
    with mock.patch('tornado.netutil.BlockingResolver.initialize', return_value=None):
        assert resolver.initialize() is None