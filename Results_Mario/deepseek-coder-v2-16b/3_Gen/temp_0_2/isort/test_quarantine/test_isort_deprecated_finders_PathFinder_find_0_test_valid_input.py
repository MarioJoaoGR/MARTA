
from isort.deprecated.finders import PathFinder
import pytest
from unittest.mock import patch, MagicMock

@patch('isort.deprecated.finders.sys')
@patch('isort.deprecated.finders.os.path')
@patch('isort.deprecated.finders.glob')
@patch('isort.deprecated.finders.sysconfig')
@patch('isort.deprecated.finders.Path')
@patch('isort.deprecated.finders.exists_case_sensitive', return_value=True)
def test_valid_input(mock_exists, mock_path, mock_glob, mock_sysconfig, mock_pathfinder, mock_config):
    from isort.deprecated.finders import PathFinder
    
    # Initialize the PathFinder with a valid configuration and default path
    finder = PathFinder(config=mock_config)
    
    # Test that paths are correctly set up based on virtual environment or conda environment if present
    assert "src" in finder.paths, f"Expected 'src' to be included in paths but got {finder.paths}"

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

isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mock_exists = <MagicMock name='exists_case_sensitive' id='140313665839120'>
mock_path = <MagicMock name='Path' id='140313665828624'>
mock_glob = <MagicMock name='sysconfig' id='140313681615696'>
mock_sysconfig = <MagicMock name='glob' id='140313665985296'>
mock_pathfinder = <MagicMock name='path' id='140313665990800'>
mock_config = <MagicMock name='sys' id='140313667896720'>

    @patch('isort.deprecated.finders.sys')
    @patch('isort.deprecated.finders.os.path')
    @patch('isort.deprecated.finders.glob')
    @patch('isort.deprecated.finders.sysconfig')
    @patch('isort.deprecated.finders.Path')
    @patch('isort.deprecated.finders.exists_case_sensitive', return_value=True)
    def test_valid_input(mock_exists, mock_path, mock_glob, mock_sysconfig, mock_pathfinder, mock_config):
        from isort.deprecated.finders import PathFinder
    
        # Initialize the PathFinder with a valid configuration and default path
        finder = PathFinder(config=mock_config)
    
        # Test that paths are correctly set up based on virtual environment or conda environment if present
>       assert "src" in finder.paths, f"Expected 'src' to be included in paths but got {finder.paths}"
E       AssertionError: Expected 'src' to be included in paths but got [<MagicMock name='path.abspath()' id='140313667901968'>, "<MagicMock name='path.abspath()' id='140313667901968'>/src", <MagicMock name='path.normcase()' id='140313667790416'>]
E       assert 'src' in [<MagicMock name='path.abspath()' id='140313667901968'>, "<MagicMock name='path.abspath()' id='140313667901968'>/src", <MagicMock name='path.normcase()' id='140313667790416'>]
E        +  where [<MagicMock name='path.abspath()' id='140313667901968'>, "<MagicMock name='path.abspath()' id='140313667901968'>/src", <MagicMock name='path.normcase()' id='140313667790416'>] = <isort.deprecated.finders.PathFinder object at 0x7f9d5235a610>.paths

isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_PathFinder_find_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""