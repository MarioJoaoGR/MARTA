
import pytest
from tornado import concurrent
from unittest.mock import patch

class TestRunOnExecutorDecorator:
    @pytest.mark.asyncio
    async def test_run_on_executor_decorator(self):
        from concurrent.futures import Future
        
        class MyClass:
            def __init__(self):
                self.executor = DummyExecutor()
            
            @concurrent.run_on_executor_decorator
            async def my_async_function(self, arg1, arg2):
                return arg1 + arg2
        
        obj = MyClass()
        future_result = obj.my_async_function("example_arg1", "example_arg2")
        assert isinstance(future_result, Future)
        assert future_result.done()
        assert future_result.result() == "example_arg1example_arg2"

    @pytest.mark.asyncio
    async def test_run_on_executor_decorator_with_default_executor(self):
        from concurrent.futures import Future
        
        class MyClass:
            def __init__(self):
                self.executor = DummyExecutor()
            
            @concurrent.run_on_executor_decorator
            async def my_async_function(self, arg1, arg2):
                return arg1 + arg2
        
        obj = MyClass()
        with patch('concurrent.futures.Future', new=MockFuture):
            future_result = obj.my_async_function("example_arg1", "example_arg2")
            assert isinstance(future_result, MockFuture)
            assert future_result.done()
            assert future_result.result() == "example_arg1example_arg2"

class DummyExecutor:
    def submit(self, fn, *args):
        return fn(*args)

class MockFuture(concurrent.futures.Future):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._result = None
    
    def set_result(self, result):
        self._result = result
    
    def result(self):
        return self._result
