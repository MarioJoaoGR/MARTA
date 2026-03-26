
# Module: pytutils.memo
import pytest
from cachetools import cachedmethod
from functools import lru_cache
from warnings import simplefilter

# Import the function definition from the module
from pytutils.memo import cachedmethod as cm

# Define a custom exception for testing
class CachedException(Exception):
    pass

# Mock the cachetools and functools modules to simulate their behavior
class MockCache:
    def __init__(self):
        self.cache = {}
    
    def __call__(self, instance):
        return self.cache

class MockLock:
    def __init__(self):
        self.lock = threading.Lock()
    
    def __call__(self, instance):
        return self.lock

# Define a mock for the cachetools.typedkey and hashkey functions
def typedkey(method, *args, **kwargs):
    return f"key_{method.__name__}_{args}_{kwargs}"

def hashkey(method, *args, **kwargs):
    return f"key_{method.__name__}_{args}_{kwargs}"

# Mock the warnings module to simulate deprecation warning
simplefilter("always")

@pytest.fixture(autouse=True)
def reset_warnings():
    yield
    simplefilter("default", category=DeprecationWarning)

# Test cases for cachedmethod decorator
def test_basic_usage():
    class MyClass:
        @cachedmethod(lru_cache(maxsize=None))
        def expensive_calculation(self, a, b):
            return a + b
    
    obj = MyClass()
    assert obj.expensive_calculation(2, 3) == 5
    assert obj.expensive_calculation(2, 3) == 5  # Second call should be cached

def test_custom_key_function():
    class MyClass:
        @cachedmethod(lru_cache(maxsize=None), key=lambda self, a, b: f"key_{a}_{b}")
        def expensive_calculation(self, a, b):
            return a + b
    
    obj = MyClass()
    assert obj.expensive_calculation(2, 3) == 5
    assert obj.expensive_calculation(2, 3) == 5  # Custom key function should be used for caching

def test_using_lock():
    class MyClass:
        lock = threading.Lock()
        
        @cachedmethod(lru_cache(maxsize=None), lock=lambda self: MyClass.lock)
        def expensive_calculation(self, a, b):
            return a + b
    
    obj = MyClass()
    assert obj.expensive_calculation(2, 3) == 5
    assert obj.expensive_calculation(2, 3) == 5  # Lock should be used for synchronization

def test_caching_exception():
    class MyClass:
        @cachedmethod(lru_cache(maxsize=None), cached_exception=ValueError)
        def risky_calculation(self, value):
            if value < 0:
                raise ValueError("Value must be non-negative")
            return value * 2
    
    obj = MyClass()
    with pytest.raises(ValueError) as excinfo:
        obj.risky_calculation(-1)
    assert str(excinfo.value) == "Value must be non-negative"
    # Second call should cache the exception and rethrow it
    with pytest.raises(CachedException):
        obj.risky_calculation(-1)

def test_deprecated_typed_parameter():
    class MyClass:
        @cachedmethod(lru_cache(maxsize=None), typed=True)  # This will trigger a deprecation warning
        def expensive_calculation(self, a, b):
            return a + b
    
    with pytest.warns(DeprecationWarning):
        MyClass()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_cachedmethod_0
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py:25:20: E0602: Undefined variable 'threading' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py:68:15: E0602: Undefined variable 'threading' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py:80:9: E1123: Unexpected keyword argument 'cached_exception' in function call (unexpected-keyword-arg)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py:96:9: E1123: Unexpected keyword argument 'typed' in function call (unexpected-keyword-arg)


"""