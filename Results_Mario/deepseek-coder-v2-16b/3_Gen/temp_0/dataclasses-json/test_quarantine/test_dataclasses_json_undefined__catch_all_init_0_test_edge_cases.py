
from dataclasses import is_dataclass, fields
from inspect import signature
from typing import Any, Dict, List, Union

class _CatchAllUndefinedParameters:
    @staticmethod
    def _separate_defined_undefined_kvs(obj, kwargs):
        known_kwargs = {}
        unknown_kwargs = {}
        for key, value in kwargs.items():
            if hasattr(obj, key):
                known_kwargs[key] = value
            else:
                unknown_kwargs[key] = value
        return known_kwargs, unknown_kwargs

    @staticmethod
    def _get_catch_all_field(obj):
        for field in fields(obj):
            if field.name == "_UNKNOWN":
                return field
        raise AttributeError("No catch-all field found")

    @staticmethod
    def handle_from_dict(obj, kwargs: Dict[str, Any]):
        result = {}
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
            else:
                result[key] = value
        return result

def _catch_all_init(self, *args, **kwargs):
    init_signature = signature(self.__init__)
    known_kwargs, unknown_kwargs = _CatchAllUndefinedParameters._separate_defined_undefined_kvs(self, kwargs)
    
    num_params_takeable = len(init_signature.parameters) - 1  # don't count self
    if "_UNKNOWN" not in known_kwargs:
        num_params_takeable -= 1
    num_args_takeable = num_params_takeable - len(known_kwargs)

    args, unknown_args = args[:num_args_takeable], args[num_args_takeable:]
    
    bound_parameters = init_signature.bind_partial(self, *args, **known_kwargs)
    unknown_args = {f"_UNKNOWN{i}": v for i, v in enumerate(unknown_args)}
    arguments = bound_parameters.arguments
    arguments.update(unknown_args)
    arguments.update(unknown_kwargs)
    arguments.pop("self", None)
    
    final_parameters = _CatchAllUndefinedParameters.handle_from_dict(self, arguments)
    self.__init__(**final_parameters)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.03s =============================
"""