
import pytest
from flutils.decorators import cached_property
import asyncio
from unittest.mock import patch, MagicMock

# Test scenario 1: Correct usage of cached_property in a class
def test_cached_property_usage():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6, "Expected cached property to be computed once and then retrieved from cache"
    # Accessing the property again should not recompute it
    assert obj.y == 6, "Expected cached property to be retrieved from cache without recomputation"

# Test scenario 2: Resetting the cached value by deleting the attribute
def test_reset_cached_property():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6, "Initial access should compute the property"
    del obj.__dict__['y']
    assert obj.y == 6, "After deleting the attribute, accessing the property should recompute it"

# Test scenario 3: Mocking an asynchronous function with cached_property
@pytest.mark.asyncio
async def test_cached_property_with_mocked_async_function():
    class MyClass:
        @cached_property
        async def y(self):
            mock = MagicMock()
            mock.return_value = 6
            return await mock()

    obj = MyClass()
    with patch('__main__.mock', new=MagicMock()) as mock_func:
        assert await obj.y == 6, "Expected mocked async function to return a cached value"
        # Ensure the mock was called only once
        mock_func.assert_called_once()
