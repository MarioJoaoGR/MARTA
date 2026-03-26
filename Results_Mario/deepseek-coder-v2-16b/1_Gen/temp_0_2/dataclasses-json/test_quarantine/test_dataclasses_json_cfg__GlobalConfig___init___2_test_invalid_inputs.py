
from dataclasses_json.cfg import _GlobalConfig
import pytest
from typing import Dict, Union, Optional, Callable

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        config = _GlobalConfig()
        assert isinstance(config.encoders, Dict)
        assert isinstance(config.decoders, Dict)
        assert isinstance(config.mm_fields, Dict)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___2_test_invalid_inputs.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""