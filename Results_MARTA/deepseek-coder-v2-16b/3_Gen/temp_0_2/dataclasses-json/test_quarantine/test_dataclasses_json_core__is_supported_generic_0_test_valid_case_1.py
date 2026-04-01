
import pytest
from dataclasses_json.core import _is_supported_generic, Enum

@pytest.mark.parametrize("type_, expected", [
    (List[int], True),
    (Optional[str], True),
    (Union[int, str], True),
    (Enum, False)  # Assuming Enum is not a dataclass or optional type
])
def test_valid_case_1(type_, expected):
    assert _is_supported_generic(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_case_1.py:6:5: E0602: Undefined variable 'List' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_case_1.py:7:5: E0602: Undefined variable 'Optional' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_valid_case_1.py:8:5: E0602: Undefined variable 'Union' (undefined-variable)


"""