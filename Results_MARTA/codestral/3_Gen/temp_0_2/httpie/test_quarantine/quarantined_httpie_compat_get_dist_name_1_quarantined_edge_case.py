
import pytest
from unittest.mock import patch, MagicMock
from httpie.compat import get_dist_name
import importlib_metadata

class TestGetDistName:
    @patch('httpie.compat.importlib_metadata')
    def test_get_dist_name_edge_case(self, mock_importlib_metadata):
        # Mock an EntryPoint object with a dist attribute
        entry_point = MagicMock()
        dist = MagicMock()
        dist.name = 'test_dist'
        entry_point.dist = dist
    
        # Test the function when dist is not None
        result = get_dist_name(entry_point)
        assert result == 'test_dist'
    
        # Mock an EntryPoint object without a dist attribute
        entry_point.dist = None
    
        # Mock match to return a valid module name
        mock_match = MagicMock()
        mock_match.group.return_value = 'valid_module'
        entry_point.pattern.match.return_value = mock_match
    
        # Test the function when dist is None and pattern matches correctly
        result = get_dist_name(entry_point)
        assert result == 'valid_module'

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

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________ TestGetDistName.test_get_dist_name_edge_case _________________

self = <Test4DT_tests_codestral.test_httpie_compat_get_dist_name_1_test_edge_case.TestGetDistName object at 0x7f6f011b7510>
mock_importlib_metadata = <MagicMock name='importlib_metadata' id='140114721112912'>

    @patch('httpie.compat.importlib_metadata')
    def test_get_dist_name_edge_case(self, mock_importlib_metadata):
        # Mock an EntryPoint object with a dist attribute
        entry_point = MagicMock()
        dist = MagicMock()
        dist.name = 'test_dist'
        entry_point.dist = dist
    
        # Test the function when dist is not None
        result = get_dist_name(entry_point)
        assert result == 'test_dist'
    
        # Mock an EntryPoint object without a dist attribute
        entry_point.dist = None
    
        # Mock match to return a valid module name
        mock_match = MagicMock()
        mock_match.group.return_value = 'valid_module'
        entry_point.pattern.match.return_value = mock_match
    
        # Test the function when dist is None and pattern matches correctly
        result = get_dist_name(entry_point)
>       assert result == 'valid_module'
E       AssertionError: assert <MagicMock name='importlib_metadata.metadata().get()' id='140114721225296'> == 'valid_module'

httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_edge_case.py:30: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_1_test_edge_case.py::TestGetDistName::test_get_dist_name_edge_case
============================== 1 failed in 0.13s ===============================
"""