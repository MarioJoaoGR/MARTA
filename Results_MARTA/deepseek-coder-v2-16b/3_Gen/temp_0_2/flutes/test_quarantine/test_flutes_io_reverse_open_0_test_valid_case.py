
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open, _ReverseReadlineFile

@pytest.fixture(scope="module")
def sample_file():
    # Create a temporary file for testing
    temp_file = "temp_reverse_file.txt"
    with open(temp_file, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    yield temp_file
    # Clean up the temporary file after the test
    Path(temp_file).unlink()

def test_valid_case(sample_file):
    with reverse_open(Path(sample_file), allow_empty_lines=True) as f:
        lines = list(f)
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

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_valid_case.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

sample_file = 'temp_reverse_file.txt'

    def test_valid_case(sample_file):
        with reverse_open(Path(sample_file), allow_empty_lines=True) as f:
            lines = list(f)
>           assert lines == ["Line 3\n", "Line 2\n", "Line 1\n"]
E           AssertionError: assert ['\n', 'Line ...', 'Line 1\n'] == ['Line 3\n', ...', 'Line 1\n']
E             
E             At index 0 diff: '\n' != 'Line 3\n'
E             Left contains one more item: 'Line 1\n'
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_valid_case.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.08s ===============================
"""