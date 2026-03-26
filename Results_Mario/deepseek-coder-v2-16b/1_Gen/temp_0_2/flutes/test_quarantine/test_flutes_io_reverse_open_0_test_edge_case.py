
import io
from pathlib import Path
import pytest
from flutes.io import reverse_open

def test_reverse_open_basic(tmp_path):
    # Create a sample file with some content
    file_content = "Line 1\nLine 2\nLine 3\n"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(file_content, encoding='utf-8')

    # Test the reverse_open function
    with open(file_path, 'rb') as f:
        expected_lines = list(reversed([line.decode('utf-8').strip() for line in f]))

    lines = []
    with reverse_open(file_path, encoding='utf-8', allow_empty_lines=True) as f:
        for line in f:
            lines.append(line.strip())

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

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_edge_case.py F   [100%]

=================================== FAILURES ===================================
___________________________ test_reverse_open_basic ____________________________

tmp_path = PosixPath('/tmp/pytest-of-joaovitorino/pytest-1/test_reverse_open_basic0')

    def test_reverse_open_basic(tmp_path):
        # Create a sample file with some content
        file_content = "Line 1\nLine 2\nLine 3\n"
        file_path = tmp_path / "sample.txt"
        file_path.write_text(file_content, encoding='utf-8')
    
        # Test the reverse_open function
        with open(file_path, 'rb') as f:
            expected_lines = list(reversed([line.decode('utf-8').strip() for line in f]))
    
        lines = []
        with reverse_open(file_path, encoding='utf-8', allow_empty_lines=True) as f:
            for line in f:
                lines.append(line.strip())
    
>       assert lines == expected_lines
E       AssertionError: assert ['', 'Line 3'... 2', 'Line 1'] == ['Line 3', 'Line 2', 'Line 1']
E         
E         At index 0 diff: '' != 'Line 3'
E         Left contains one more item: 'Line 1'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_edge_case.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_edge_case.py::test_reverse_open_basic
============================== 1 failed in 0.09s ===============================
"""