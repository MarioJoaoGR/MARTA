
import pytest
from tornado.netutil import ThreadedResolver
import concurrent.futures
import asyncio

# Fixture to create a ThreadedResolver instance for testing
@pytest.fixture
def resolver():
    return ThreadedResolver(num_threads=10)

# Test case for initializing the ThreadedResolver with default number of threads (10)
def test_initialize_default_threads(resolver):
    assert isinstance(resolver.executor, concurrent.futures.ThreadPoolExecutor)
    assert resolver.executor._max_workers == 10

# Test case for initializing the ThreadedResolver with a specified number of threads
def test_initialize_specified_threads():
    resolver = ThreadedResolver(num_threads=5)
    assert isinstance(resolver.executor, concurrent.futures.ThreadPoolExecutor)