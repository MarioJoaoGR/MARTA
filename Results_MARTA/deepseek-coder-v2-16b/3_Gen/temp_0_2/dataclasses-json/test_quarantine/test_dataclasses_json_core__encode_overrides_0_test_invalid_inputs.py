
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, Callable, Optional

@dataclass
class OverrideInfo:
    letter_case: Optional[Callable[[str], str]] = None
    encoder: Optional[Callable[[Any], Any]] = None
    exclude: Optional[Callable[[Any], bool]] = None

def _encode_overrides(kvs, overrides, encode_json=False):
    override_kvs = {}
    for k, v in kvs.items():
        if k in overrides:
            exclude = overrides[k].exclude
            # If the exclude predicate returns true, the key should be
            #  excluded from encoding, so skip the rest of the loop
            if exclude and exclude(v):
                continue
            letter_case = overrides[k].letter_case
            original_key = k
            k = letter_case(k) if letter_case is not None else k
            if k in override_kvs:
                raise ValueError(
                    f"Multiple fields map to the same JSON "
                    f"key after letter case encoding: {k}"
                )

            encoder = overrides[original_key].encoder
            v = encoder(v) if encoder is not None else v

        if encode_json:
            v = _encode_json_type(v)
        override_kvs[k] = v
    return override_kvs

# Assuming _encode_json_type is defined somewhere in the module
def _encode_json_type(value):
    if isinstance(value, dict):
        return {_encode_json_type(k): _encode_json_type(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [_encode_json_type(i) for i in value]
    else:
        return value

# Test case to check invalid inputs
def test_invalid_inputs():
    with pytest.raises(ValueError):
        kvs = {'name': 'John', 'age': 30}
        overrides = {
            'name': OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
            'age': OverrideInfo(letter_case=None, encoder=str)
        }
        _encode_overrides(kvs, overrides)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_invalid_inputs.py:49: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""