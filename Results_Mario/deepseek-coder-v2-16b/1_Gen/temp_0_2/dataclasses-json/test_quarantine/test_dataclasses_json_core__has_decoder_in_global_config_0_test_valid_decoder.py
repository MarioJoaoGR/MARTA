
import pytest
from dataclasses_json.core import _has_decoder_in_global_config

# Mocking the cfg object and its structure
class Config:
    def __init__(self):
        self.global_config = GlobalConfig()

class GlobalConfig:
    def __init__(self):
        self.decoders = {'example_decoder'}

@pytest.fixture(autouse=True)
def mock_cfg():
    cfg = Config()
    yield cfg

# Test case to check if the decoder is in the global configuration
def test_valid_decoder():
    assert _has_decoder_in_global_config('example_decoder') == True

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_decoder ______________________________

    def test_valid_decoder():
>       assert _has_decoder_in_global_config('example_decoder') == True
E       AssertionError: assert False == True
E        +  where False = _has_decoder_in_global_config('example_decoder')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_valid_decoder.py::test_valid_decoder
============================== 1 failed in 0.04s ===============================
"""