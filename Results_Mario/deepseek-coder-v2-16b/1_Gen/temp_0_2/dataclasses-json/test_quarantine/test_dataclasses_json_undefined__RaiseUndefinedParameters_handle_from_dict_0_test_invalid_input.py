
import pytest
from dataclasses_json.undefined import UndefinedParameterError
from unittest.mock import MagicMock

# Mocking the class and its method for testing
class _RaiseUndefinedParameters:
    def __init__(self, param1=None, param2=None):
        pass

def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
    known, unknown = \
        _UndefinedParameterAction._separate_defined_undefined_kvs(
            cls=cls, kvs=kvs)
    if len(unknown) > 0:
        raise UndefinedParameterError(
            f"Received undefined initialization arguments {unknown}")
    return known

def test_invalid_input():
    # Create a mock class with fields 'param1' and 'param2'
    MockClass = MagicMock()
    MockClass.__dataclass_fields__ = {'param1': None, 'param2': None}
    
    # Define an invalid dictionary with an undefined parameter
    kvs = {'param1': 1, 'extra_param': 2}
    
    # Test that it raises UndefinedParameterError for the unknown parameter
    with pytest.raises(UndefinedParameterError) as excinfo:
        handle_from_dict(MockClass, kvs)
    assert str(excinfo.value) == "Received undefined initialization arguments {'extra_param'}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input.py:11:31: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input.py:11:40: E0602: Undefined variable 'Dict' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input.py:11:50: E0602: Undefined variable 'Any' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input.py:13:8: E0602: Undefined variable '_UndefinedParameterAction' (undefined-variable)


"""