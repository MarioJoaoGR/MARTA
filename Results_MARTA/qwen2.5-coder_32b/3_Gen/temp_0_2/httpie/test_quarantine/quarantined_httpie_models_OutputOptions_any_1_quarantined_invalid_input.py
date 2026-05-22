
import pytest
from unittest.mock import patch
from httpie.models import RequestsMessageKind
from your_module_name import OutputOptions  # Replace 'your_module_name' with the actual module name where OutputOptions is defined

def test_invalid_input():
    with pytest.raises(TypeError) as e:
        options = OutputOptions(kind='INVALID', headers=True, body=True, meta=True)
    assert str(e.value) == "Invalid kind value: 'INVALID'. Expected one of RequestsMessageKind."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_OutputOptions_any_1_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_OutputOptions_any_1_test_invalid_input.py:5:0: E0401: Unable to import 'your_module_name' (import-error)


"""