
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open

@pytest.mark.parametrize("path, encoding, allow_empty_lines, buffer_size", [
    ('example.txt', 'utf-8', True, io.DEFAULT_BUFFER_SIZE),
    ('example.txt', 'utf-8', False, 1024)
])
def test_valid_input(path, encoding, allow_empty_lines, buffer_size):
    # Arrange
    expected_lines = ["Line 3", "Line 2", "Line 1"]
    
    with open('example.txt', 'w') as f:
        f.writelines("\n".join(expected_lines) + "\n")
    
    # Act
    lines = list(reverse_open(Path(path), encoding=encoding, allow_empty_lines=allow_empty_lines, buffer_size=buffer_size))
    
    # Assert
    if allow_empty_lines:
        assert lines == expected_lines[::-1]
    else:
        assert lines == [line for line in expected_lines if line.strip()]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_io_reverse_open_4_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ test_valid_input[example.txt-utf-8-True-8192] _________________

path = 'example.txt', encoding = 'utf-8', allow_empty_lines = True
buffer_size = 8192

    @pytest.mark.parametrize("path, encoding, allow_empty_lines, buffer_size", [
        ('example.txt', 'utf-8', True, io.DEFAULT_BUFFER_SIZE),
        ('example.txt', 'utf-8', False, 1024)
    ])
    def test_valid_input(path, encoding, allow_empty_lines, buffer_size):
        # Arrange
        expected_lines = ["Line 3", "Line 2", "Line 1"]
    
        with open('example.txt', 'w') as f:
            f.writelines("\n".join(expected_lines) + "\n")
    
        # Act
        lines = list(reverse_open(Path(path), encoding=encoding, allow_empty_lines=allow_empty_lines, buffer_size=buffer_size))
    
        # Assert
        if allow_empty_lines:
>           assert lines == expected_lines[::-1]
E           AssertionError: assert ['\n', 'Line ...', 'Line 3\n'] == ['Line 1', 'Line 2', 'Line 3']
E             
E             At index 0 diff: '\n' != 'Line 1'
E             Left contains one more item: 'Line 3\n'
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_4_test_valid_input.py:23: AssertionError
________________ test_valid_input[example.txt-utf-8-False-1024] ________________

path = 'example.txt', encoding = 'utf-8', allow_empty_lines = False
buffer_size = 1024

    @pytest.mark.parametrize("path, encoding, allow_empty_lines, buffer_size", [
        ('example.txt', 'utf-8', True, io.DEFAULT_BUFFER_SIZE),
        ('example.txt', 'utf-8', False, 1024)
    ])
    def test_valid_input(path, encoding, allow_empty_lines, buffer_size):
        # Arrange
        expected_lines = ["Line 3", "Line 2", "Line 1"]
    
        with open('example.txt', 'w') as f:
            f.writelines("\n".join(expected_lines) + "\n")
    
        # Act
        lines = list(reverse_open(Path(path), encoding=encoding, allow_empty_lines=allow_empty_lines, buffer_size=buffer_size))
    
        # Assert
        if allow_empty_lines:
            assert lines == expected_lines[::-1]
        else:
>           assert lines == [line for line in expected_lines if line.strip()]
E           AssertionError: assert ['Line 1\n', ...', 'Line 3\n'] == ['Line 3', 'Line 2', 'Line 1']
E             
E             At index 0 diff: 'Line 1\n' != 'Line 3'
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_io_reverse_open_4_test_valid_input.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_4_test_valid_input.py::test_valid_input[example.txt-utf-8-True-8192]
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_4_test_valid_input.py::test_valid_input[example.txt-utf-8-False-1024]
============================== 2 failed in 0.12s ===============================
"""