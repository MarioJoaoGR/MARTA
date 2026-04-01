
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union, cast

def _get_type_arg_param(tp: Type, index: int) -> Union[Type, _NoArgs]:
    _args = _get_type_args(tp)
    if _args is not _NO_ARGS:
        try:
            return cast(Tuple[Type, ...], _args)[index]
        except (TypeError, IndexError, NotImplementedError):
            pass

    return _NO_ARGS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_arg_param_0_test_no_arguments_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_no_arguments_case.py:5:61: E0602: Undefined variable '_NoArgs' (undefined-variable)


"""