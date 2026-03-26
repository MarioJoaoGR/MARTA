
import pytest
from pytutils.meth import bind

def test_bind_edge_case():
    # Test with None instance
    func = lambda self: None  # A dummy function that does nothing
    as_name = 'method'
    
    with pytest.raises(TypeError):
        bind(None, func, as_name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_meth_bind_0_test_edge_case.py F     [100%]

=================================== FAILURES ===================================
_____________________________ test_bind_edge_case ______________________________

    def test_bind_edge_case():
        # Test with None instance
        func = lambda self: None  # A dummy function that does nothing
        as_name = 'method'
    
        with pytest.raises(TypeError):
>           bind(None, func, as_name)

pytutils/Test4DT_tests/test_pytutils_meth_bind_0_test_edge_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

instance = None
func = <function test_bind_edge_case.<locals>.<lambda> at 0x7ff2c14d8900>
as_name = 'method'

    def bind(instance, func, as_name):
        """
        Turn a function to a bound method on an instance
    
        >>> class Foo(object):
        ...     def __init__(self, x, y):
        ...         self.x = x
        ...         self.y = y
        >>> foo = Foo(2, 3)
        >>> my_unbound_method = lambda self: self.x * self.y
        >>> bind(foo, my_unbound_method, 'multiply')
        >>> foo.multiply()  # noinspection PyUnresolvedReferences
        6
    
        :param object instance: some object
        :param callable func: unbound method (i.e. a function that takes `self` argument, that you now
            want to be bound to this class as a method)
        :param str as_name: name of the method to create on the object
        """
>       setattr(instance, as_name, func.__get__(instance, instance.__class__))
E       AttributeError: 'NoneType' object has no attribute 'method'

pytutils/pytutils/meth.py:20: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_meth_bind_0_test_edge_case.py::test_bind_edge_case
============================== 1 failed in 0.06s ===============================
"""