
import pytest
from unittest.mock import patch, MagicMock
from httpie.compat import get_dist_name

def test_get_dist_name():
    with patch('httpie.compat.importlib_metadata') as mock_metadata:
        # Create a mock EntryPoint object
        entry_point = MagicMock()
        entry_point.value = 'some_module'
    
        # Mock the metadata method to return a metadata object with name attribute
        metadata = MagicMock()
        metadata.get.return_value = 'some_name'
        mock_metadata.metadata.return_value = metadata

        # Call the function under test
        result = get_dist_name(entry_point)
    
        # Assert that the expected name was returned
        assert result == 'some_name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_get_dist_name ______________________________

    def test_get_dist_name():
        with patch('httpie.compat.importlib_metadata') as mock_metadata:
            # Create a mock EntryPoint object
            entry_point = MagicMock()
            entry_point.value = 'some_module'
    
            # Mock the metadata method to return a metadata object with name attribute
            metadata = MagicMock()
            metadata.get.return_value = 'some_name'
            mock_metadata.metadata.return_value = metadata
    
            # Call the function under test
            result = get_dist_name(entry_point)
    
            # Assert that the expected name was returned
>           assert result == 'some_name'
E           AssertionError: assert <MagicMock name='mock.dist.name' id='140678403754064'> == 'some_name'

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_2_test_edge_case.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_2_test_edge_case.py::test_get_dist_name
============================== 1 failed in 0.11s ===============================
"""