
import subprocess
from pathlib import Path
import pytest
from flutes.fs import get_folder_size

@pytest.mark.parametrize("path", [Path("."), Path("/tmp")])
def test_valid_input(path):
    # Mocking the subprocess output for a known folder size
    expected_output = 123456  # Example size in bytes
    with pytest.MonkeyPatch.context() as mp_mock:
        mp_mock.setattr(subprocess, 'check_output', lambda args, **kwargs: f"{expected_output}\t{path}".encode('utf-8'))
        assert get_folder_size(path) == expected_output * 512

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input[path0] ____________________________

path = PosixPath('.')

    @pytest.mark.parametrize("path", [Path("."), Path("/tmp")])
    def test_valid_input(path):
        # Mocking the subprocess output for a known folder size
        expected_output = 123456  # Example size in bytes
        with pytest.MonkeyPatch.context() as mp_mock:
            mp_mock.setattr(subprocess, 'check_output', lambda args, **kwargs: f"{expected_output}\t{path}".encode('utf-8'))
>           assert get_folder_size(path) == expected_output * 512
E           AssertionError: assert 123456 == (123456 * 512)
E            +  where 123456 = get_folder_size(PosixPath('.'))

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_valid_input.py:13: AssertionError
___________________________ test_valid_input[path1] ____________________________

path = PosixPath('/tmp')

    @pytest.mark.parametrize("path", [Path("."), Path("/tmp")])
    def test_valid_input(path):
        # Mocking the subprocess output for a known folder size
        expected_output = 123456  # Example size in bytes
        with pytest.MonkeyPatch.context() as mp_mock:
            mp_mock.setattr(subprocess, 'check_output', lambda args, **kwargs: f"{expected_output}\t{path}".encode('utf-8'))
>           assert get_folder_size(path) == expected_output * 512
E           AssertionError: assert 123456 == (123456 * 512)
E            +  where 123456 = get_folder_size(PosixPath('/tmp'))

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_valid_input.py::test_valid_input[path0]
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_0_test_valid_input.py::test_valid_input[path1]
============================== 2 failed in 0.11s ===============================
"""