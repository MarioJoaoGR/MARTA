
import dataclasses
from typing import Optional, Callable, Dict, Union
from dataclasses_json import dataclass_json, config
from marshmallow import fields as MarshmallowField
from enum import Enum

class Undefined(Enum):
    IGNORE = "ignore"
    EXCLUDE = "exclude"

class Example2:
    def __init__(self, a_camel_case: int):
        self.a_camel_case = a_camel_case

@dataclass_json
@dataclasses.dataclass
class Example2Config(Example2):
    pass

def config(metadata: Optional[dict] = None, *,
           encoder: Optional[Callable] = None,
           decoder: Optional[Callable] = None,
           mm_field: Optional[MarshmallowField] = None,
           letter_case: Union[Callable[[str], str], LetterCase, None] = None,
           undefined: Optional[Union[str, Undefined]] = None,
           field_name: Optional[str] = None,
           exclude: Optional[Callable[[Example2Config], bool]] = None,
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
            @functools.wraps(letter_case)  # type:ignore
            def override(_, _letter_case=letter_case, _field_name=field_name):
                return _letter_case(_field_name)
        else:
            def override(_, _field_name=field_name):  # type:ignore
                return _field_name
        letter_case = override

    if letter_case is not None:
        lib_metadata['letter_case'] = letter_case

    if undefined is not None:
        # Get the corresponding action for undefined parameters
        if isinstance(undefined, str):
            if not hasattr(Undefined, undefined.upper()):
                valid_actions = [action.name for action in Undefined]
                raise ValueError(
                    f"Invalid undefined parameter action, "
                    f"must be one of {valid_actions}")
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
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:21:0: E0102: function already defined line 4 (function-redefined)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:25:52: E0602: Undefined variable 'LetterCase' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:46:13: E0602: Undefined variable 'functools' (undefined-variable)


"""