
import unittest.mock as mock
from httpie.compat import get_dist_name

def test_get_dist_name():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        # Mocking the EntryPoint object
        entry_point = mock.Mock()
        dist = mock.Mock()
        dist.name = 'some_dist_name'
        entry_point.dist = dist
        
        result = get_dist_name(entry_point)
        assert result == 'some_dist_name'

# Example test case for edge case scenario
def test_get_dist_name_edge_case():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        # Mocking the EntryPoint object without a dist attribute
        entry_point = mock.Mock()
        entry_point.pattern = mock.Mock()
        entry_point.value = 'some_module'
        
        # Mocking pattern match to return a valid module name
        match = mock.Mock()
        match.group.return_value = {'module': 'some_module'}
        entry_point.pattern.match.return_value = match
        
        # Mocking metadata retrieval for the package
        with mock.patch('httpie.compat.importlib_metadata.metadata', return_value=mock.Mock(name='some_dist_name')):
            result = get_dist_name(entry_point)
            assert result == 'some_dist_name'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_3_test_edge_case.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_get_dist_name_edge_case _________________________

    def test_get_dist_name_edge_case():
        with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
            # Mocking the EntryPoint object without a dist attribute
            entry_point = mock.Mock()
            entry_point.pattern = mock.Mock()
            entry_point.value = 'some_module'
    
            # Mocking pattern match to return a valid module name
            match = mock.Mock()
            match.group.return_value = {'module': 'some_module'}
            entry_point.pattern.match.return_value = match
    
            # Mocking metadata retrieval for the package
            with mock.patch('httpie.compat.importlib_metadata.metadata', return_value=mock.Mock(name='some_dist_name')):
                result = get_dist_name(entry_point)
>               assert result == 'some_dist_name'
E               AssertionError: assert <Mock name='mock.dist.name' id='140561826154832'> == 'some_dist_name'

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_3_test_edge_case.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_3_test_edge_case.py::test_get_dist_name_edge_case
========================= 1 failed, 1 passed in 0.14s ==========================
"""