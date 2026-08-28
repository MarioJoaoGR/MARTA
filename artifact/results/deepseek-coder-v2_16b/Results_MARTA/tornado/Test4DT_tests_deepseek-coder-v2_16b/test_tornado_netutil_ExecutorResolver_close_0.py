
import pytest
from tornado.netutil import ExecutorResolver
import concurrent.futures as futures


def test_valid_input():
    resolver = ExecutorResolver()
    resolver.close_executor = True
    assert isinstance(resolver.executor, futures.Executor)
    resolver.close()
    assert resolver.executor is None