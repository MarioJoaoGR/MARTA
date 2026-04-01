
import pytest
from pathlib import Path
from unittest.mock import MagicMock
from isort.place import _is_namespace_package

@pytest.mark.parametrize("src_extensions", [frozenset({"py"})])
def test_valid_case(src_extensions):
    mock_path = MagicMock()
    mock_path.__str__.return_value = 'mocked_dir'
    mock_path.exists.return_value = True
    mock_path.is_dir.return_value = True
    mock_path.iterdir.return_value = [
        MagicMock(name='file1', suffix='.py'),
        MagicMock(name='__init__.py')
    ]
    
    assert _is_namespace_package(mock_path, src_extensions) is True

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

isort/Test4DT_tests/test_isort_place__is_namespace_package_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_case[src_extensions0] _______________________

src_extensions = frozenset({'py'})

    @pytest.mark.parametrize("src_extensions", [frozenset({"py"})])
    def test_valid_case(src_extensions):
        mock_path = MagicMock()
        mock_path.__str__.return_value = 'mocked_dir'
        mock_path.exists.return_value = True
        mock_path.is_dir.return_value = True
        mock_path.iterdir.return_value = [
            MagicMock(name='file1', suffix='.py'),
            MagicMock(name='__init__.py')
        ]
    
>       assert _is_namespace_package(mock_path, src_extensions) is True
E       AssertionError: assert False is True
E        +  where False = _is_namespace_package(<MagicMock id='139891863941904'>, frozenset({'py'}))

isort/Test4DT_tests/test_isort_place__is_namespace_package_0_test_valid_case.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_0_test_valid_case.py::test_valid_case[src_extensions0]
============================== 1 failed in 0.10s ===============================
"""