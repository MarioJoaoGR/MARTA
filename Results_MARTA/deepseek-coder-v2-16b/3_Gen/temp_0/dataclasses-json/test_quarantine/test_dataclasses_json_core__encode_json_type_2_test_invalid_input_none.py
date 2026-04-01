
import pytest
from dataclasses_json.core import _encode_json_type
from dataclasses_json._extended_encoder import _ExtendedEncoder
from typing import List, Dict, Union

def test_invalid_input_none():
    with pytest.raises(TypeError):
        _encode_json_type(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_json_type_2_test_invalid_input_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_2_test_invalid_input_none.py:4:0: E0401: Unable to import 'dataclasses_json._extended_encoder' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_2_test_invalid_input_none.py:4:0: E0611: No name '_extended_encoder' in module 'dataclasses_json' (no-name-in-module)


"""