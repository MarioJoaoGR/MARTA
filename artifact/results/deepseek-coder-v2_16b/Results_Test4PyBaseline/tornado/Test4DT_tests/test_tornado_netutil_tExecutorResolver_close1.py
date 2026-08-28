
# Module: tornado.netutil
from tornado.netutil import ExecutorResolver
import pytest

@pytest.fixture
def executor_resolver():
    return ExecutorResolver()

@pytest.fixture
def close_executor_resolver():
    return ExecutorResolver(close_executor=True)

# Test cases for the default behavior of closing the executor
def test_close_default(executor_resolver):
    """Test that the close method shuts down the executor and waits for ongoing tasks to complete by default."""
    assert hasattr(executor_resolver, 'executor')
    initial_executor = executor_resolver.executor
    executor_resolver.close()
    assert executor_resolver.executor is None
    # Additional assertions could be added here to ensure that the shutdown method was called on the executor

def test_close_immediate(close_executor_resolver):
    """Test that the close method shuts down the executor immediately without waiting for ongoing tasks."""
    assert hasattr(close_executor_resolver, 'executor')
    initial_executor = close_executor_resolver.executor
    close_executor_resolver.close()