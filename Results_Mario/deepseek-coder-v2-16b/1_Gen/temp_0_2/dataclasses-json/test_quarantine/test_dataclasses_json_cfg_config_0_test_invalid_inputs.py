
import pytest
from dataclasses_json import config, Undefined
from typing import Callable, Dict, Optional, Union
from marshmallow import fields as MarshmallowField
from dataclasses import dataclass

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test invalid undefined parameter action
        config({}, undefined='invalid_action')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # Test invalid undefined parameter action
>           config({}, undefined='invalid_action')

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

metadata = {'dataclasses_json': {}}

    def config(metadata: Optional[dict] = None, *,
               # TODO: these can be typed more precisely
               # Specifically, a Callable[A, B], where `B` is bound as a JSON type
               encoder: Optional[Callable] = None,
               decoder: Optional[Callable] = None,
               mm_field: Optional[MarshmallowField] = None,
               letter_case: Union[Callable[[str], str], LetterCase, None] = None,
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
                    valid_actions = list(action.name for action in Undefined)
>                   raise UndefinedParameterError(
                        f"Invalid undefined parameter action, "
                        f"must be one of {valid_actions}")
E                   dataclasses_json.undefined.UndefinedParameterError: Invalid undefined parameter action, must be one of ['INCLUDE', 'RAISE', 'EXCLUDE']

dataclasses-json/dataclasses_json/cfg.py:100: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""