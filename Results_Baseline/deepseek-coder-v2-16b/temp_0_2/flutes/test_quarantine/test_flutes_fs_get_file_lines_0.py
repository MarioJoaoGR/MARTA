
import subprocess
from pathlib import Path
from flutes.fs import get_file_lines
import pytest

# Test case 1: Count lines in a local text file
def test_get_file_lines_local():
    path = Path('test_file.txt')
    with open(path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    assert get_file_lines(path) == 3
    path.unlink()  # Clean up the test file

# Test case 2: Count lines in a remote text file (URL)
def test_get_file_lines_remote():
    url = 'https://example.com/test_file.txt'
    subprocess.run(['curl', '-o', 'test_file.txt', url])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_fs_get_file_lines_0.py F.               [100%]

=================================== FAILURES ===================================
__________________________ test_get_file_lines_local ___________________________

    def test_get_file_lines_local():
        path = Path('test_file.txt')
        with open(path, 'w') as f:
            f.write("Line 1\nLine 2\nLine 3")
>       assert get_file_lines(path) == 3
E       AssertionError: assert 2 == 3
E        +  where 2 = get_file_lines(PosixPath('test_file.txt'))

flutes/Test4DT_tests/test_flutes_fs_get_file_lines_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_get_file_lines_0.py::test_get_file_lines_local
========================= 1 failed, 1 passed in 0.20s ==========================
"""