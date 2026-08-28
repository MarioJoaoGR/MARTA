
import pytest
from dataclasses import dataclass
from marshmallow_dataclass import dataclass_json
from typing import Callable, Optional, Union, Dict, Any
from dataclasses_json.cfg import config
from marshmallow import fields as MarshmallowField
from dataclasses_json import Undefined
import functools

# Example 1: Basic Usage
@dataclass_json
@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None

def test_basic_usage():
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    metadata = {}
    new_metadata = config(metadata)
    assert 'dataclasses_json' in new_metadata

# Example 2: Custom Encoder and Decoder
def encode_int(value):
    return str(value)

def decode_str(value):
    return int(value)

@pytest.mark.parametrize("encoder, decoder", [
    (encode_int, decode_str),
])
def test_custom_encoder_decoder(encoder, decoder):
    config.register_encoder(int, encoder)
    config.register_decoder(int, decoder)
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    metadata = {}
    new_metadata = config(metadata, encoder=encoder, decoder=decoder)
    assert 'encoder' in new_metadata['dataclasses_json']
    assert 'decoder' in new_metadata['dataclasses_json']

# Example 3: Custom Letter Case
def camel_case(field_name):
    return ''.join([word.capitalize() for word in field_name.split('_')])

@pytest.mark.parametrize("letter_case", [camel_case])
def test_custom_letter_case(letter_case):
    config.register_encoder(int, lambda value: str(value))  # Example encoder for int type
    config.register_decoder(int, lambda value: int(value))  # Example decoder for int type
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    metadata = {}
    new_metadata = config(metadata, letter_case=letter_case)
    assert 'letter_case' in new_metadata['dataclasses_json']

# Example 4: Handling Undefined Parameters
@pytest.mark.parametrize("undefined", [Undefined.EXCLUDE])
def test_handling_undefined_parameters(undefined):
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    metadata = {}
    new_metadata = config(metadata, undefined=undefined)
    assert 'undefined' in new_metadata['dataclasses_json']

# Example 5: Custom Field Name and Exclusion
def camel_case(field_name):
    return ''.join([word.capitalize() for word in field_name.split('_')])

@pytest.mark.parametrize("exclude", [lambda f, t: f == 'email'])
def test_custom_field_name_and_exclusion(exclude):
    config.register_encoder(int, lambda value: str(value))  # Example encoder for int type
    config.register_decoder(int, lambda value: int(value))  # Example decoder for int type
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    metadata = {}
    new_metadata = config(metadata, letter_case=camel_case, exclude=exclude)
    assert 'letter_case' in new_metadata['dataclasses_json']
    assert 'exclude' in new_metadata['dataclasses_json']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting test_dataclasses_json_cfg_config_0.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_0.py:4: in <module>
    from marshmallow_dataclass import dataclass_json
E   ModuleNotFoundError: No module named 'marshmallow_dataclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""