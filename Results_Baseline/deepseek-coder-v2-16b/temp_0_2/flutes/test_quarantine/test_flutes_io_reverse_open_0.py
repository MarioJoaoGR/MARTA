
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open

# Assuming _ReverseReadlineFile is a class defined in the same module or imported correctly
# If not, you might need to define it or adjust the imports accordingly.

def test_reverse_open_with_and_without_empty_lines():
    # Create a temporary file with different line structures
    content = "Line1\n\nLine2\nLine3"  # Includes empty lines
    temp_file_path = Path('temp.txt')
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Test allowing empty lines
    with reverse_open(temp_file_path, encoding='utf-8', allow_empty_lines=True) as f:
        lines = [line for line in f]
        assert lines == ['Line1\n', '', 'Line2\n', 'Line3']
    
    # Test not allowing empty lines
    with reverse_open(temp_file_path, encoding='utf-8', allow_empty_lines=False) as f:
        lines = [line for line in f]
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

flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py F                  [100%]

=================================== FAILURES ===================================
________________ test_reverse_open_with_and_without_empty_lines ________________

    def test_reverse_open_with_and_without_empty_lines():
        # Create a temporary file with different line structures
        content = "Line1\n\nLine2\nLine3"  # Includes empty lines
        temp_file_path = Path('temp.txt')
        with open(temp_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
        # Test allowing empty lines
        with reverse_open(temp_file_path, encoding='utf-8', allow_empty_lines=True) as f:
            lines = [line for line in f]
>           assert lines == ['Line1\n', '', 'Line2\n', 'Line3']
E           AssertionError: assert ['Line3\n', '...n', 'Line1\n'] == ['Line1\n', '...2\n', 'Line3']
E             
E             At index 0 diff: 'Line3\n' != 'Line1\n'
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py::test_reverse_open_with_and_without_empty_lines
============================== 1 failed in 0.10s ===============================
"""