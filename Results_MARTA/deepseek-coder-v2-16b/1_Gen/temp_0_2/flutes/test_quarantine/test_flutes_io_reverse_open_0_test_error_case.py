
import pytest
from pathlib import Path
from flutes.io import reverse_open

@pytest.fixture(scope="module")
def sample_file():
    file_path = Path("temp_test_file.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    yield file_path
    file_path.unlink()

def test_reverse_open(sample_file):
    with reverse_open(sample_file, encoding="utf-8", allow_empty_lines=True) as reader:
        lines = list(reader)
    assert lines == ["Line 3\n", "Line 2\n", "Line 1\n"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_error_case.py F  [100%]

=================================== FAILURES ===================================
______________________________ test_reverse_open _______________________________

sample_file = PosixPath('temp_test_file.txt')

    def test_reverse_open(sample_file):
        with reverse_open(sample_file, encoding="utf-8", allow_empty_lines=True) as reader:
            lines = list(reader)
>       assert lines == ["Line 3\n", "Line 2\n", "Line 1\n"]
E       AssertionError: assert ['\n', 'Line ...', 'Line 1\n'] == ['Line 3\n', ...', 'Line 1\n']
E         
E         At index 0 diff: '\n' != 'Line 3\n'
E         Left contains one more item: 'Line 1\n'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_error_case.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_error_case.py::test_reverse_open
============================== 1 failed in 0.12s ===============================
"""