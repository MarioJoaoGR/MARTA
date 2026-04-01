
from dataclasses_json.cfg import letter_case, field_name

def override(_, _letter_case=letter_case, _field_name=field_name):
    return _letter_case(_field_name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_override_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_override_0_test_invalid_input.py:2:0: E0611: No name 'letter_case' in module 'dataclasses_json.cfg' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_override_0_test_invalid_input.py:2:0: E0611: No name 'field_name' in module 'dataclasses_json.cfg' (no-name-in-module)


"""