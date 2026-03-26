
import pytest
from pytutils.iters import dedupe

def test_edge_case_none():
    def my_function():
        return iter([1, 2, 3, 4, 5])
    
    @dedupe(my_function, None, (), {})
    def wrapped_function():
        yield from [1, 2, 3, 4, 5]
    
    deduped_result = list(wrapped_function())
    assert deduped_result == [1, 2, 3, 4, 5]

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

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        def my_function():
            return iter([1, 2, 3, 4, 5])
    
>       @dedupe(my_function, None, (), {})

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0_test_edge_case_none.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

f = <function test_edge_case_none.<locals>.my_function at 0x7fdeecfc0d60>
instance = None
args = (<function test_edge_case_none.<locals>.wrapped_function at 0x7fdeecfc0e00>,)
kwargs = {}

    @wrapt.decorator
    def dedupe(f, instance, args, kwargs):
        """
        Decorator to dedupe it's output iterable automatically.
    
        :param f: Wrapped meth
        :param instance: wrapt provided property for decorating hydrated class instances (unused)
        :param args: Passthrough args
        :param kwargs: Passthrough kwargs
        :return decorator: Decorator method that ingests iterables and dedupes them iteratively.
        """
>       gen = f(*args, **kwargs)
E       TypeError: test_edge_case_none.<locals>.my_function() takes 0 positional arguments but 1 was given

pytutils/pytutils/iters.py:75: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.06s ===============================
"""