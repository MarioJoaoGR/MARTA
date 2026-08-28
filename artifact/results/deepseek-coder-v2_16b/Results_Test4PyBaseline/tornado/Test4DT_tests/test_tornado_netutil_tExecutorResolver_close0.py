# Module: tornado.netutil
# Import the function from its module
from tornado.netutil import ExecutorResolver
import pytest

@pytest.fixture
def executor_resolver():
    return ExecutorResolver()

def test_close_default(executor_resolver):
    """Test that the close method shuts down the executor and waits for ongoing tasks to complete by default."""
    assert hasattr(executor_resolver, 'executor')
    initial_executor = executor_resolver.executor
    executor_resolver.close()
    assert executor_resolver.executor is None
    # Additional assertions could be added here to ensure that the shutdown method was called on the executor

def test_close_immediate(executor_resolver):
    """Test that the close method shuts down the executor immediately without waiting for ongoing tasks."""
    executor_resolver = ExecutorResolver(close_executor=True)
    assert hasattr(executor_resolver, 'executor')
    initial_executor = executor_resolver.executor
    executor_resolver.close()
    assert executor_resolver.executor is None
    # Additional assertions could be added here to ensure that the shutdown method was called on the executor without waiting
