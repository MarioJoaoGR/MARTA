
import pytest
from unittest.mock import patch, MagicMock
import io
from flutes.io import progress_open

@pytest.mark.parametrize("path", ["non_existent_file.txt"])
def test_invalid_input(path):
    with pytest.raises(FileNotFoundError):
        with patch('flutes.io.open', side_effect=FileNotFoundError) as mock_open:
            with progress_open(path, mode="r", encoding='utf-8', verbose=True, buffer_size=io.DEFAULT_BUFFER_SIZE):
                pass
    assert mock_open.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
__________________ test_invalid_input[non_existent_file.txt] ___________________

path = 'non_existent_file.txt'

    @pytest.mark.parametrize("path", ["non_existent_file.txt"])
    def test_invalid_input(path):
        with pytest.raises(FileNotFoundError):
            with patch('flutes.io.open', side_effect=FileNotFoundError) as mock_open:
                with progress_open(path, mode="r", encoding='utf-8', verbose=True, buffer_size=io.DEFAULT_BUFFER_SIZE):
                    pass
>       assert mock_open.called
E       AssertionError: assert False
E        +  where False = <MagicMock name='open' id='140097519204304'>.called

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_invalid_input.py::test_invalid_input[non_existent_file.txt]
============================== 1 failed in 0.11s ===============================
"""