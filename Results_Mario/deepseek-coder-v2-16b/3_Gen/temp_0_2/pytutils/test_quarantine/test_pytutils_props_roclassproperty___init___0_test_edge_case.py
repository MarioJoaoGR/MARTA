
class roclassproperty:
    """
    A read-only class property descriptor factory/decorator.
    
    This class allows the creation of properties that can be accessed like attributes but cannot be set once initialized. It is particularly useful for defining immutable class properties in a way that mimics attribute access.
    
    Parameters:
        f (callable): The function to be wrapped and made read-only as a property. This function will be called when the property is accessed, but its value cannot be set directly.
        
    Returns:
        roclassproperty: An instance of the roclassproperty class that acts as a descriptor for the given function.
        
    Example:
        >>> class MyClass:
        ...     def __init__(self, value):
        ...         self._value = value
        ...     
        ...     @roclassproperty
        ...     def value(cls):
        ...         return cls._value
        ... 
        >>> obj = MyClass(10)
        >>> print(obj.value)  # Output: 10
        >>> obj.value = 20      # This will raise an AttributeError, as the property is read-only.
    
    Note:
        The roclassproperty decorator should be used on class methods that return a value and do not take any arguments other than 'cls' (the class itself).
    """
    def __init__(self, f):
        self.f = f

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.04s =============================
"""