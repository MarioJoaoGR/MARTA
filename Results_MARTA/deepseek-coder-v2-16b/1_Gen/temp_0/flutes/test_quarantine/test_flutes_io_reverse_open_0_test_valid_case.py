
import io
from flutes.io import reverse_open as ro

def test_valid_case():
    # Test valid case with a sample file
    path = "sample.txt"
    with open(path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    expected_lines = ["Line 3", "Line 2", "Line 1"]
    lines = list(ro(path))
    
    assert lines == expected_lines

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

    def test_valid_case():
        # Test valid case with a sample file
        path = "sample.txt"
        with open(path, 'w') as f:
            f.write("Line 1\nLine 2\nLine 3\n")
    
        expected_lines = ["Line 3", "Line 2", "Line 1"]
        lines = list(ro(path))
    
>       assert lines == expected_lines
E       AssertionError: assert ['Line 3\n', ...', 'Line 1\n'] == ['Line 3', 'Line 2', 'Line 1']
E         
E         At index 0 diff: 'Line 3\n' != 'Line 3'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_valid_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.09s ===============================
"""