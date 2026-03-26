
import pytest
from flutes.iterator import scanl

def test_edge_cases():
    # Test with None input
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, None, 0))
    
    # Test with empty iterable
    assert list(scanl(lambda acc, x: acc + x, [], 0)) == [0]
    
    # Test with boundary value initial
    assert list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], float('-inf'))) == [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')]
    
    # Test with None in iterable
    assert list(scanl(lambda acc, x: acc + x if x is not None else acc, [1, None, 3, 4], 0)) == [0, 1, 1, 4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_scanl_7_test_edge_cases.py F   [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None input
        with pytest.raises(TypeError):
            list(scanl(lambda acc, x: acc + x, None, 0))
    
        # Test with empty iterable
        assert list(scanl(lambda acc, x: acc + x, [], 0)) == [0]
    
        # Test with boundary value initial
        assert list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], float('-inf'))) == [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')]
    
        # Test with None in iterable
>       assert list(scanl(lambda acc, x: acc + x if x is not None else acc, [1, None, 3, 4], 0)) == [0, 1, 1, 4]
E       assert [0, 1, 1, 4, 8] == [0, 1, 1, 4]
E         
E         Left contains one more item: 8
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_7_test_edge_cases.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_7_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================

"""