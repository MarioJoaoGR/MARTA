
import pytest
from unittest.mock import MagicMock, patch
from flutes.multiproc import PoolType

@pytest.fixture
def setup_pool():
    return PoolType()

def test_map_async(setup_pool):
    # Mock the function to be applied
    mock_fn = MagicMock(side_effect=[1, 4, 9, 16])
    
    # Define the iterable
    iterable = [1, 2, 3, 4]
    
    # Call map_async method
    with patch('flutes.multiproc.mp', autospec=True) as mock_mp:
        result = setup_pool.map_async(mock_fn, iterable, chunksize=2)
        
        # Assert that the mock function was called correctly
        assert mock_fn.call_count == 4
        
        # Optionally, you can add more assertions to check the behavior of the ApplyResult or callbacks if needed
        # For example:
        # assert result.get() == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_async_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
________________________________ test_map_async ________________________________

setup_pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_map_async(setup_pool):
        # Mock the function to be applied
        mock_fn = MagicMock(side_effect=[1, 4, 9, 16])
    
        # Define the iterable
        iterable = [1, 2, 3, 4]
    
        # Call map_async method
        with patch('flutes.multiproc.mp', autospec=True) as mock_mp:
            result = setup_pool.map_async(mock_fn, iterable, chunksize=2)
    
            # Assert that the mock function was called correctly
>           assert mock_fn.call_count == 4
E           AssertionError: assert 0 == 4
E            +  where 0 = <MagicMock id='140371880551184'>.call_count

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_async_0_test_edge_cases.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_async_0_test_edge_cases.py::test_map_async
============================== 1 failed in 0.21s ===============================
"""