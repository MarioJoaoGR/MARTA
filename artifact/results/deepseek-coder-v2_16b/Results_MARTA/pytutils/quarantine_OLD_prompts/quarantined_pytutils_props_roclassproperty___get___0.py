
import pytest
from pytutils.props import roclassproperty

def test_roclassproperty_with_instancemethod():
    class MyClass:
        @roclassproperty
        def my_property(self):
            return 42
    
    obj = MyClass()
    with pytest.raises(AttributeError):
        obj.my_property = 100
```

```python
def test_roclassproperty_with_settable_classmethod():
    class MyClass:
        @roclassproperty
        def my_property(cls):
            return 42
    
    with pytest.raises(AttributeError):
        MyClass.my_property = 100

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 14, col 1)
```
"""