
import dataclasses
from typing import Optional, Callable, Dict, Union
from dataclasses_json import dataclass_json, config
from marshmallow import fields as MarshmallowField
from enum import Enum

class Undefined(Enum):
    IGNORE = 'ignore'
    EXCLUDE = 'exclude'

def config(metadata: Optional[dict] = None, *,
           encoder: Optional[Callable] = None,
           decoder: Optional[Callable] = None,
           mm_field: Optional[MarshmallowField] = None,
           letter_case: Union[Callable[[str], str], Enum, None] = None,
           undefined: Optional[Union[str, Undefined]] = None,
           field_name: Optional[str] = None,
           exclude: Optional[Callable[[T], bool]] = None,
           ) -> Dict[str, dict]:
    if metadata is None:
        metadata = {}

    lib_metadata = metadata.setdefault('dataclasses_json', {})

    if encoder is not None:
        lib_metadata['encoder'] = encoder

    if decoder is not None:
        lib_metadata['decoder'] = decoder

    if mm_field is not None:
        lib_metadata['mm_field'] = mm_field

    if field_name is not None:
        if letter_case is not None:
            def override(_, _letter_case=letter_case, _field_name=field_name):
                return _letter_case(_field_name)
            letter_case = override

    if letter_case is not None:
        lib_metadata['letter_case'] = letter_case

    if undefined is not None:
        if isinstance(undefined, str):
            if not hasattr(Undefined, undefined.upper()):
                valid_actions = [action.name for action in Undefined]
                raise ValueError(f"Invalid undefined parameter action, must be one of {valid_actions}")
            undefined = Undefined[undefined.upper()]
        lib_metadata['undefined'] = undefined

    if exclude is not None:
        lib_metadata['exclude'] = exclude

    return metadata

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_config_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:12:0: E0102: function already defined line 4 (function-redefined)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:19:39: E0602: Undefined variable 'T' (undefined-variable)

"""