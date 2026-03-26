
import pytest
from dataclasses_json.utils import Undefined

def _handle_undefined_parameters_safe(cls, kvs, usage: str):
    """
    Checks if an undefined parameters action is defined and performs the
    according action.
    """
    undefined_parameter_action = _undefined_parameter_action_safe(cls)
    usage = usage.lower()
    if undefined_parameter_action is None:
        return kvs if usage != "init" else cls.__init__
    if usage == "from":
        return undefined_parameter_action.value.handle_from_dict(cls=cls,
                                                                 kvs=kvs)
    elif usage == "to":
        return undefined_parameter_action.value.handle_to_dict(obj=cls,
                                                               kvs=kvs)
    elif usage == "dump":
        return undefined_parameter_action.value.handle_dump(obj=cls)
    elif usage == "init":
        return undefined_parameter_action.value.create_init(obj=cls)
    else:
        raise ValueError(
            f"usage must be one of ['to', 'from', 'dump', 'init'], "
            f"but is '{usage}'")

# Example test case for _handle_undefined_parameters_safe function
def test_handle_undefined_parameters_safe():
    from dataclasses import dataclass
    from dataclasses_json import dataclass_json, Undefined
    
    @dataclass_json
    @dataclass
    class MyDataClass:
        a: int = None
        b: str = None

    kvs = {'a': 1, 'c': 2}  # Example undefined parameter dictionary

    # Test with usage='to'
    result_to = _handle_undefined_parameters_safe(MyDataClass, kvs, usage='to')
    assert result_to == {'a': 1, 'b': Undefined.MISSING, 'c': 2}

    # Test with usage='from'
    result_from = _handle_undefined_parameters_safe(MyDataClass, kvs, usage='from')
    assert result_from == {'a': 1, 'b': Undefined.MISSING, 'c': 2}

    # Test with usage='dump'
    result_dump = _handle_undefined_parameters_safe(MyDataClass, kvs, usage='dump')
    assert result_dump == {'a': 1, 'b': Undefined.MISSING}

    # Test with usage='init'
    result_init = _handle_undefined_parameters_safe(MyDataClass, kvs, usage='init')
    assert callable(result_init)

    # Test with invalid usage
    with pytest.raises(ValueError):
        _handle_undefined_parameters_safe(MyDataClass, kvs, usage='invalid')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs.py:3:0: E0611: No name 'Undefined' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs.py:10:33: E0602: Undefined variable '_undefined_parameter_action_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs.py:44:38: E1101: Class 'Undefined' has no 'MISSING' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs.py:48:40: E1101: Class 'Undefined' has no 'MISSING' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_valid_inputs.py:52:40: E1101: Class 'Undefined' has no 'MISSING' member (no-member)


"""