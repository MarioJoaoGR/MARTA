
from dataclasses_json.undefined import UndefinedParameterAction
from typing import Dict, Any

class _UndefinedParameterAction:
    def handle_dump(self, obj) -> Dict[Any, Any]:
        """
        Return the parameters that will be added to the schema dump.
        """
        return {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_handle_dump_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_dump_0_test_invalid_input.py:2:0: E0611: No name 'UndefinedParameterAction' in module 'dataclasses_json.undefined' (no-name-in-module)

"""