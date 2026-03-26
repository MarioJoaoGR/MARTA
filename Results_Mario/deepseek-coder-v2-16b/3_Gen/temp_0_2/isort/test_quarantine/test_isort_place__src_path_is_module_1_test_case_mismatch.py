
import pytest
from pathlib import Path
from unittest.mock import patch, Mock
from isort.place import exists_case_sensitive

def _src_path_is_module(src_path: Path, module_name: str) -> bool:
    return (
        module_name == src_path.name and src_path.is_dir() and exists_case_sensitive(str(src_path))
    )

@pytest.fixture
def valid_module():
    return Path("valid_module")

@patch('isort.place.exists_case_sensitive')
def test_valid_module(_mock_exists):
    _mock_exists.return_value = True
    assert _src_path_is_module(Path("valid_module"), "valid_module") == True

@patch('isort.place.exists_case_sensitive')
def test_invalid_module(_mock_exists):
    _mock_exists.return_value = False
    assert _src_path_is_module(Path("valid_module"), "invalid_module") == False

@patch('isort.place.exists_case_sensitive')
def test_not_a_directory(_mock_exists):
    _mock_exists.return_value = True
    assert _src_path_is_module(Path("valid_module.py"), "valid_module") == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_place__src_path_is_module_1_test_case_mismatch.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_module _______________________________

_mock_exists = <MagicMock name='exists_case_sensitive' id='140404605802640'>

    @patch('isort.place.exists_case_sensitive')
    def test_valid_module(_mock_exists):
        _mock_exists.return_value = True
>       assert _src_path_is_module(Path("valid_module"), "valid_module") == True
E       AssertionError: assert False == True
E        +  where False = _src_path_is_module(PosixPath('valid_module'), 'valid_module')
E        +    where PosixPath('valid_module') = Path('valid_module')

isort/Test4DT_tests/test_isort_place__src_path_is_module_1_test_case_mismatch.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__src_path_is_module_1_test_case_mismatch.py::test_valid_module
========================= 1 failed, 2 passed in 0.13s ==========================
"""