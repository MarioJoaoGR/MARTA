
import pytest
import asyncio
from flutils.decorators import cached_property

class MyClass:
    def __init__(self):
        self.x = 5
        
    @cached_property
    def y(self):
        return self.x + 1

# Creating an instance of the class and accessing the property
@pytest.fixture
def obj():
    return MyClass()

def test_cached_property_instance_method(obj):
    # First access should compute the value
    assert obj.y == 6
    
    # Second access should use the cached value
    assert obj.y == 6

# Test for asynchronous function caching
@pytest.mark.asyncio
async def test_cached_property_asynchronous():
    class AsyncClass:
        def __init__(self):
            self.x = 5
            
        @cached_property
        def y(self):
            return asyncio.ensure_future(self._compute_y())
        
        async def _compute_y(self):
            await asyncio.sleep(0)  # Simulating an expensive operation
            return self.x + 1

    obj = AsyncClass()
    
    # First access should compute the value
    result = await obj.y
    assert result == 6
    
    # Second access should use the cached value
    result = await obj.y
    assert result == 6
