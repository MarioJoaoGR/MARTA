
import pytest
from dataclasses_json.core import cfg

def _has_decoder_in_global_config(type_):
    return type_ in cfg.global_config.decoders

@pytest.mark.parametrize("test_input, expected", [
    ("nonexistent_decoder_type", False),
    ("some_decoder_type", True)  # Assuming 'some_decoder_type' exists in the global configuration for testing purposes
])
def test_invalid_decoder_missing(test_input, expected):
    assert _has_decoder_in_global_config(test_input) == expected

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_decoder_missing.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ test_invalid_decoder_missing[some_decoder_type-True] _____________

test_input = 'some_decoder_type', expected = True

    @pytest.mark.parametrize("test_input, expected", [
        ("nonexistent_decoder_type", False),
        ("some_decoder_type", True)  # Assuming 'some_decoder_type' exists in the global configuration for testing purposes
    ])
    def test_invalid_decoder_missing(test_input, expected):
>       assert _has_decoder_in_global_config(test_input) == expected
E       AssertionError: assert False == True
E        +  where False = _has_decoder_in_global_config('some_decoder_type')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_decoder_missing.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_decoder_missing.py::test_invalid_decoder_missing[some_decoder_type-True]
========================= 1 failed, 1 passed in 0.03s ==========================
"""