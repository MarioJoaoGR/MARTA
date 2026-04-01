
import pytest
from dataclasses import dataclass
from typing import Optional, Callable, Dict, Union
from marshmallow import fields as MarshmallowField
from enum import Enum
from dataclasses_json import config

# Define a mock for the Undefined enum if necessary
class Undefined(Enum):
    IGNORE = "ignore"
    EXCLUDE = "exclude"

# Define a mock for the LetterCase enum if necessary
class LetterCase(Enum):
    LOWER = lambda s: s.lower()
    UPPER = lambda s: s.upper()

# Mock the dataclasses_json library and its config function
@pytest.fixture
def setup():
    class UndefinedParameterError(Exception):
        pass

    yield {
        'Undefined': Undefined,
        'LetterCase': LetterCase,
        'config': config
    }

def test_valid_inputs(setup):
    Undefined = setup['Undefined']
    LetterCase = setup['LetterCase']
    config = setup['config']

    # Test basic usage with encoder and decoder
    @dataclass
    class Example:
        a: int
        b: str = "default"
        c: Optional[int] = None

    metadata = {}
    new_metadata = config(metadata, encoder=lambda x: x, decoder=lambda y: y)
    assert 'dataclasses_json' in new_metadata
    assert 'encoder' in new_metadata['dataclasses_json']
    assert 'decoder' in new_metadata['dataclasses_json']

    # Test custom field name and letter case conversion
    @dataclass
    class Example2:
        a_camel_case: int

    metadata = {}
    new_metadata = config(metadata, letter_case=lambda s: s.upper())
    assert 'letter_case' in new_metadata['dataclasses_json']
    assert callable(new_metadata['dataclasses_json']['letter_case'])

    # Test handling undefined parameters
    @dataclass
    class Example3:
        a: int
        b: str = "default"

    metadata = {}
    new_metadata = config(metadata, undefined="ignore")
    assert 'undefined' in new_metadata['dataclasses_json']
    assert new_metadata['dataclasses_json']['undefined'] == Undefined.IGNORE

if __name__ == "__main__":
    pytest.main()

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

setup = {'LetterCase': <enum 'LetterCase'>, 'Undefined': <enum 'Undefined'>, 'config': <function config at 0x104231e10>}

    def test_valid_inputs(setup):
        Undefined = setup['Undefined']
        LetterCase = setup['LetterCase']
        config = setup['config']
    
        # Test basic usage with encoder and decoder
        @dataclass
        class Example:
            a: int
            b: str = "default"
            c: Optional[int] = None
    
        metadata = {}
        new_metadata = config(metadata, encoder=lambda x: x, decoder=lambda y: y)
        assert 'dataclasses_json' in new_metadata
        assert 'encoder' in new_metadata['dataclasses_json']
        assert 'decoder' in new_metadata['dataclasses_json']
    
        # Test custom field name and letter case conversion
        @dataclass
        class Example2:
            a_camel_case: int
    
        metadata = {}
        new_metadata = config(metadata, letter_case=lambda s: s.upper())
        assert 'letter_case' in new_metadata['dataclasses_json']
        assert callable(new_metadata['dataclasses_json']['letter_case'])
    
        # Test handling undefined parameters
        @dataclass
        class Example3:
            a: int
            b: str = "default"
    
        metadata = {}
>       new_metadata = config(metadata, undefined="ignore")

dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_2_test_valid_inputs.py:66: 
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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""