
import pytest
from dataclasses_json.core import _resolve_collection_type_to_decode_to

def test_none_input():
    with pytest.raises(TypeError):
        result = _resolve_collection_type_to_decode_to(None)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_none_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_none_input.py::test_none_input
============================== 1 failed in 0.05s ===============================
"""