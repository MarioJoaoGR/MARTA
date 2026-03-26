
import pytest
from flutes.iterator import LazyList

# Test initialization with a list
def test_lazy_list_with_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0.py F       [100%]

=================================== FAILURES ===================================
___________________________ test_lazy_list_with_list ___________________________

    def test_lazy_list_with_list():
        my_list = [1, 2, 3, 4, 5]
        lazy_list = LazyList(my_list)
>       assert isinstance(lazy_list.iter, type([].__iter__)), "Expected iter to be an iterator"
E       AssertionError: Expected iter to be an iterator
E       assert False
E        +  where False = isinstance(<list_iterator object at 0x7f6228c66e60>, <class 'method-wrapper'>)
E        +    where <list_iterator object at 0x7f6228c66e60> = <flutes.iterator.LazyList object at 0x7f6228f24e10>.iter
E        +    and   <class 'method-wrapper'> = type(<method-wrapper '__iter__' of list object at 0x7f6229c41340>)
E        +      where <method-wrapper '__iter__' of list object at 0x7f6229c41340> = [].__iter__

flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___init___0.py::test_lazy_list_with_list
============================== 1 failed in 0.09s ===============================
"""