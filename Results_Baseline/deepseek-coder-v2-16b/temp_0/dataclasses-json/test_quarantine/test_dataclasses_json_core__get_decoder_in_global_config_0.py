
import pytest
from dataclasses_json.core import _get_decoder_in_global_config
try:
    import cfg  # Assuming cfg is a module with global_config containing decoders
except ImportError:
    class MockConfig:
        def __init__(self):
            self.decoders = {
                'some_type': "Decoder for some_type",
                'another_type': "Decoder for another_type"
            }

    cfg = MockConfig()

def test_get_decoder_in_global_config_valid():
    # Test with a valid type
    decoder = _get_decoder_in_global_config('some_type')
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py F [100%]

=================================== FAILURES ===================================
___________________ test_get_decoder_in_global_config_valid ____________________

    def test_get_decoder_in_global_config_valid():
        # Test with a valid type
>       decoder = _get_decoder_in_global_config('some_type')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = 'some_type'

    def _get_decoder_in_global_config(type_):
>       return cfg.global_config.decoders[type_]
E       KeyError: 'some_type'

dataclasses-json/dataclasses_json/core.py:467: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py::test_get_decoder_in_global_config_valid
============================== 1 failed in 0.03s ===============================

"""