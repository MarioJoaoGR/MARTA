
import pytest
from dataclasses import dataclass, field
from typing import Optional, Dict
import inspect
import functools
from dataclasses_json.undefined import _CatchAllUndefinedParameters

def create_init(obj) -> Callable:
    original_init = obj.__init__
    init_signature = inspect.signature(original_init)

    @functools.wraps(obj.__init__)
    def _catch_all_init(self, *args, **kwargs):
        known_kwargs, unknown_kwargs = \
            _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                obj, kwargs)
        num_params_takeable = len(
            init_signature.parameters) - 1  # don't count self
        if _CatchAllUndefinedParameters._get_catch_all_field(
                obj).name not in known_kwargs:
            num_params_takeable -= 1
        num_args_takeable = num_params_takeable - len(known_kwargs)

        args, unknown_args = args[:num_args_takeable], args[
                                                       num_args_takeable:]
        bound_parameters = init_signature.bind_partial(self, *args,
                                                       **known_kwargs)

        unknown_args = {f"_UNKNOWN{i}": v for i, v in
                        enumerate(unknown_args)}
        arguments = bound_parameters.arguments
        arguments.update(unknown_args)
        arguments.update(unknown_kwargs)
        arguments.pop("self", None)
        final_parameters = _CatchAllUndefinedParameters.handle_from_dict(
            obj, arguments)
        original_init(self, **final_parameters)

    return _catch_all_init

@dataclass
class MyClass(_CatchAllUndefinedParameters):
    defined_param: int
    catch_all_field: Optional[Dict] = field(default_factory=dict)

MyClass.__init__ = create_init(MyClass)

def test_my_class_with_undefined_parameter():
    instance = MyClass(defined_param=10, undefined_param=20)
    assert instance.catch_all_field == {'undefined_param': 20}

@dataclass
class AnotherClass(_CatchAllUndefinedParameters):
    defined_param: int

AnotherClass.__init__ = create_init(AnotherClass)

def test_another_class_with_undefined_parameter():
    instance = AnotherClass(defined_param=10, another_undefined_param=30)
    assert instance.catch_all_field == {'another_undefined_param': 30}

@dataclass
class MultiParamClass(_CatchAllUndefinedParameters):
    param1: int
    param2: str
    catch_all_field: Optional[Dict] = field(default_factory=dict)

MultiParamClass.__init__ = create_init(MultiParamClass)

def test_multi_param_class_with_undefined_parameter():
    instance = MultiParamClass(param1=5, param2="hello", extra_param=40)
    assert instance.catch_all_field == {'extra_param': 40}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0.py _
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0.py:9: in <module>
    def create_init(obj) -> Callable:
E   NameError: name 'Callable' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""