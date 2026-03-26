
import inspect
import functools
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _IgnoreUndefinedParameters

class MyClass:
    def __init__(self, a, b=None, c=0):
        self.a = a
        self.b = b
        self.c = c

def create_init(obj) -> Callable:
    original_init = obj.__init__
    init_signature = inspect.signature(original_init)

    @functools.wraps(obj.__init__)
    def _ignore_init(self, *args, **kwargs):
        known_kwargs, _ = \
            _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                obj, kwargs)
        num_params_takeable = len(
            init_signature.parameters) - 1  # don't count self
        num_args_takeable = num_params_takeable - len(known_kwargs)

        args = args[:num_args_takeable]
        bound_parameters = init_signature.bind_partial(self, *args, **known_kwargs)
        bound_parameters.apply_defaults()

        arguments = bound_parameters.arguments
        arguments.pop("self", None)
        final_parameters = \
            _IgnoreUndefinedParameters.handle_from_dict(obj, arguments)
        original_init(self, **final_parameters)

    return _ignore_init

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_input.py:12:24: E0602: Undefined variable 'Callable' (undefined-variable)


"""