
import pytest
from flutes.iterator import scanl
import operator

def test_valid_inputs():
    # Test with a list of integers and an initial value
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test with a list of strings without an initial value
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']
    
    # Test with a list of integers and no initial value provided (should raise ValueError)
    with pytest.raises(ValueError):
        list(scanl(operator.add, [1, 2, 3, 4]))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with a list of integers and an initial value
        result = list(scanl(operator.add, [1, 2, 3, 4], 0))
        assert result == [0, 1, 3, 6, 10]
    
        # Test with a list of strings without an initial value
        result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
        assert result == ['a', 'ba', 'cba', 'dcba']
    
        # Test with a list of integers and no initial value provided (should raise ValueError)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_valid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================

"""