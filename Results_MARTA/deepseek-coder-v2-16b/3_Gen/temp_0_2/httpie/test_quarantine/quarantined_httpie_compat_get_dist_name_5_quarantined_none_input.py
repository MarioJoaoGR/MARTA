
import unittest
from unittest.mock import patch, MagicMock
from httpie.compat import get_dist_name
import importlib_metadata

class TestGetDistName(unittest.TestCase):
    @patch('httpie.compat.importlib_metadata')
    def test_none_input(self, mock_importlib_metadata):
        # Mock an EntryPoint with a dist attribute set to a MagicMock object
        entry_point = MagicMock()
        entry_point.dist = MagicMock()
        entry_point.dist.name = 'some_name'
        
        result = get_dist_name(entry_point)
        self.assertEqual(result, 'some_name')

    @patch('httpie.compat.importlib_metadata')
    def test_none_input_no_dist(self, mock_importlib_metadata):
        # Mock an EntryPoint without a dist attribute
        entry_point = MagicMock()
        entry_point.pattern = MagicMock()
        entry_point.value = 'some_module'
        
        # Mock the pattern match to return a group with 'module'
        mock_match = MagicMock()
        mock_match.group.return_value = 'some_module'
        entry_point.pattern.match.return_value = mock_match
        
        result = get_dist_name(entry_point)
        self.assertEqual(result, 'some_name')  # Assuming the metadata retrieval works correctly and returns 'some_name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_5_test_none_input.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________ TestGetDistName.test_none_input_no_dist ____________________

self = <test_httpie_compat_get_dist_name_5_test_none_input.TestGetDistName testMethod=test_none_input_no_dist>
mock_importlib_metadata = <MagicMock name='importlib_metadata' id='139693963546576'>

    @patch('httpie.compat.importlib_metadata')
    def test_none_input_no_dist(self, mock_importlib_metadata):
        # Mock an EntryPoint without a dist attribute
        entry_point = MagicMock()
        entry_point.pattern = MagicMock()
        entry_point.value = 'some_module'
    
        # Mock the pattern match to return a group with 'module'
        mock_match = MagicMock()
        mock_match.group.return_value = 'some_module'
        entry_point.pattern.match.return_value = mock_match
    
        result = get_dist_name(entry_point)
>       self.assertEqual(result, 'some_name')  # Assuming the metadata retrieval works correctly and returns 'some_name'
E       AssertionError: <MagicMock name='mock.dist.name' id='139693968893520'> != 'some_name'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_5_test_none_input.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_compat_get_dist_name_5_test_none_input.py::TestGetDistName::test_none_input_no_dist
========================= 1 failed, 1 passed in 0.16s ==========================
"""