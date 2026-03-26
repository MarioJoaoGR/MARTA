
from flutes.log import set_log_file
from pathlib import Path
from unittest.mock import patch
import logging

def test_valid_input():
    with patch('flutes.log.set_log_file') as mock_set_log_file:
        valid_path = Path("logs/app.log")
        set_log_file(valid_path, fmt="%Y-%m-%d %H:%M:%S")
        assert mock_set_log_file.called

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

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('flutes.log.set_log_file') as mock_set_log_file:
            valid_path = Path("logs/app.log")
>           set_log_file(valid_path, fmt="%Y-%m-%d %H:%M:%S")

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/log.py:147: in set_log_file
    handler.setFormatter(logging.Formatter(fmt))
/usr/local/lib/python3.11/logging/__init__.py:598: in __init__
    self._style.validate()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.PercentStyle object at 0x7fbc4b273550>

    def validate(self):
        """Validate the input format, ensure it matches the correct style"""
        if not self.validation_pattern.search(self._fmt):
>           raise ValueError("Invalid format '%s' for '%s' style" % (self._fmt, self.default_format[0]))
E           ValueError: Invalid format '%Y-%m-%d %H:%M:%S' for '%' style

/usr/local/lib/python3.11/logging/__init__.py:438: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.13s ===============================
"""