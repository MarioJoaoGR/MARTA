
import pytest
from isort.sorting import naturally, _natural_keys
from typing import Iterable, Callable, Any

def test_invalid_inputs():
    with pytest.raises(TypeError):
        naturally(['item12', 'item2', 'item1'], key=lambda x: None, reverse=True)
    
    with pytest.raises(ValueError):
        naturally(['item12', 'item2', 'item1'], key=lambda x: x, reverse='true')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            naturally(['item12', 'item2', 'item1'], key=lambda x: None, reverse=True)
    
        with pytest.raises(ValueError):
>           naturally(['item12', 'item2', 'item1'], key=lambda x: x, reverse='true')

isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

to_sort = ['item12', 'item2', 'item1']
key = <function test_invalid_inputs.<locals>.<lambda> at 0x7fddf31a1bc0>
reverse = 'true'

    def naturally(
        to_sort: Iterable[str], key: Callable[[str], Any] | None = None, reverse: bool = False
    ) -> list[str]:
        """Returns a naturally sorted list"""
        if key is None:
            key_callback = _natural_keys
        else:
    
            def key_callback(text: str) -> list[Any]:
                return _natural_keys(key(text))
    
>       return sorted(to_sort, key=key_callback, reverse=reverse)
E       TypeError: 'str' object cannot be interpreted as an integer

isort/isort/sorting.py:123: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting_naturally_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""