
import pytest
from flutes.log import _remove_handlers
import logging

def test_none_input():
    with pytest.raises(TypeError):
        _remove_handlers(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
>           _remove_handlers(None)

flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

logger = None

    def _remove_handlers(logger):
>       while len(logger.handlers) > 0:
E       AttributeError: 'NoneType' object has no attribute 'handlers'

flutes/flutes/log.py:97: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""