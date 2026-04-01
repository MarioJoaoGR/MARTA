
import pytest
from flutes.iterator import split_by

def test_invalid_separator():
    iterable = 'banana'
    separator = 'a'
    
    with pytest.raises(ValueError):
        list(split_by(iterable, empty_segments=False, separator=separator))

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

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_invalid_separator.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_separator ____________________________

    def test_invalid_separator():
        iterable = 'banana'
        separator = 'a'
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_invalid_separator.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_invalid_separator.py::test_invalid_separator
============================== 1 failed in 0.09s ===============================
"""