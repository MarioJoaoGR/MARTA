
import pytest
from dataclasses_json.core import _has_decoder_in_global_config

# Mocking the cfg module and its global_config with decoders for testing purposes
class MockCfg:
    class GlobalConfig:
        def __init__(self, decoders):
            self.decoders = decoders

cfg = MockCfg()

def test_has_decoder_in_global_config_found():
    # Setup the mock global config with a decoder
    cfg.global_config = MockCfg.GlobalConfig(['json', 'xml'])
    
    # Test when the decoder is present in the global configuration
    assert _has_decoder_in_global_config('json') == True

def test_has_decoder_in_global_config_not_found():
    # Setup the mock global config without any decoders
    cfg.global_config = MockCfg.GlobalConfig([])
    
    # Test when the decoder is not present in the global configuration
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
___________________ test_has_decoder_in_global_config_found ____________________

    def test_has_decoder_in_global_config_found():
        # Setup the mock global config with a decoder
        cfg.global_config = MockCfg.GlobalConfig(['json', 'xml'])
    
        # Test when the decoder is present in the global configuration
>       assert _has_decoder_in_global_config('json') == True
E       AssertionError: assert False == True
E        +  where False = _has_decoder_in_global_config('json')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0.py::test_has_decoder_in_global_config_found
========================= 1 failed, 1 passed in 0.02s ==========================

"""