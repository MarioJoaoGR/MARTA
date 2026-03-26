
import pytest
from flutes.iterator import scanl

def test_valid_input_with_initial():
    # Test with a list of numbers and an initial value
    result = list(scanl(lambda s, x: s + x, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]

    # Test with a list of characters and no initial value
    result = list(scanl(lambda s, x: s + x, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']

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

flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_input_with_initial.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_with_initial _________________________

    def test_valid_input_with_initial():
        # Test with a list of numbers and an initial value
        result = list(scanl(lambda s, x: s + x, [1, 2, 3, 4], 0))
        assert result == [0, 1, 3, 6, 10]
    
        # Test with a list of characters and no initial value
        result = list(scanl(lambda s, x: s + x, ['a', 'b', 'c', 'd']))
>       assert result == ['a', 'ba', 'cba', 'dcba']
E       AssertionError: assert ['a', 'ab', 'abc', 'abcd'] == ['a', 'ba', 'cba', 'dcba']
E         
E         At index 1 diff: 'ab' != 'ba'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_input_with_initial.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_0_test_valid_input_with_initial.py::test_valid_input_with_initial
============================== 1 failed in 0.08s ===============================
"""