
import pytest
from dataclasses import dataclass, fields, is_dataclass
from inspect import signature
import functools
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@pytest.fixture
def create_test_class():
    @dataclass
    class TestClass:
        a: int
        b: str = None
        c: float = 0.0

    return TestClass

def test_ignore_undefined_parameters(create_test_class):
    TestClass = create_test_class
    original_init = TestClass.__init__
    
    @functools.wraps(original_init)
    def _ignore_init(self, *args, **kwargs):
        known_kwargs, _ = _CatchAllUndefinedParameters._separate_defined_undefined_kvs(TestClass, kwargs)
        init_signature = signature(original_init)
        num_params_takeable = len(init_signature.parameters) - 1  # don't count self
        num_args_takeable = num_params_takeable - len(known_kwargs)

        args = args[:num_args_takeable]
        bound_parameters = init_signature.bind_partial(self, *args, **known_kwargs)
        bound_parameters.apply_defaults()

        arguments = bound_parameters.arguments
        arguments.pop("self", None)
        final_parameters = _IgnoreUndefinedParameters.handle_from_dict(TestClass, arguments)
        original_init(self, **final_parameters)

    new_init = _IgnoreUndefinedParameters.create_init(TestClass)
    
    # Test creating an instance without providing all parameters
    instance = new_init()
    assert isinstance(instance, TestClass)
    assert hasattr(instance, 'a') and getattr(instance, 'a') is None  # Assuming a should be set to default or provided value
    assert not hasattr(instance, 'b')  # b should be ignored as undefined
    assert hasattr(instance, 'c') and getattr(instance, 'c') == 0.0  # c should be set to default or provided value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_case.py:24:26: E0602: Undefined variable '_CatchAllUndefinedParameters' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_edge_case.py:41:15: E1120: No value for argument 'self' in function call (no-value-for-parameter)


"""