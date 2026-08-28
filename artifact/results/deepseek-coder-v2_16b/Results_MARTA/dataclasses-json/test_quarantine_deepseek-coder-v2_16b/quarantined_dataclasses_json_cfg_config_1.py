
import pytest
from dataclasses_json import config, Undefined
from marshmallow_dataclass import MarshmallowField
from typing import Callable, Dict, Optional, Union

# Define a simple dataclass for demonstration
@pytest.fixture
def example_dataclass():
    from dataclasses import dataclass
    @dataclass
    class ExampleDataclass:
        id: int
        name: str
    return ExampleDataclass(id=1, name="TestName")

# Test the config function with basic usage
def test_config_basic_usage(example_dataclass):
    metadata = {}
    new_metadata = config(metadata)
    assert 'dataclasses_json' in new_metadata
    assert new_metadata['dataclasses_json'] == {}

# Test the config function with custom encoder and decoder
def test_config_custom_encoder_decoder():
    from dataclasses import dataclass
    @dataclass
    class Person:
        name: str
        age: int
        email: Optional[str] = None
    
    def encode_int(value):
        return str(value)

    def decode_str(value):
        return int(value)

    config.register_encoder(int, encode_int)
    config.register_decoder(int, decode_str)

    metadata = {}
    new_metadata = config(metadata, encoder=encode_int, decoder=decode_str)
    assert 'dataclasses_json' in new_metadata
    assert new_metadata['dataclasses_json'] == {'encoder': encode_int, 'decoder': decode_str}

# Test the config function with custom letter case
def test_config_custom_letter_case():
    from dataclasses import dataclass
    @dataclass
    class Person:
        name: str
        age: int
        email: Optional[str] = None
    
    def camel_case(field_name):
        return ''.join([word.capitalize() for word in field_name.split('_')])

    metadata = {}
    new_metadata = config(metadata, letter_case=camel_case)
    assert 'dataclasses_json' in new_metadata
    assert new_metadata['dataclasses_json'] == {'letter_case': camel_case}

# Test the config function with handling of undefined parameters
def test_config_handling_undefined():
    from dataclasses import dataclass
    @dataclass
    class Person:
        name: str
        age: int
        email: Optional[str] = None
    
    metadata = {}
    new_metadata = config(metadata, undefined=Undefined.EXCLUDE)
    assert 'dataclasses_json' in new_metadata
    assert new_metadata['dataclasses_json'] == {'undefined': Undefined.EXCLUDE}

# Test the config function with custom field name and exclusion
def test_config_custom_field_name_and_exclusion():
    from dataclasses import dataclass
    @dataclass
    class Person:
        name: str
        age: int
        email: Optional[str] = None
    
    def camel_case(field_name):
        return ''.join([word.capitalize() for word in field_name.split('_')])

    metadata = {}
    new_metadata = config(metadata, letter_case=camel_case, exclude=lambda f, t: f == 'email')
    assert 'dataclasses_json' in new_metadata
    assert new_metadata['dataclasses_json'] == {'letter_case': camel_case, 'exclude': lambda f, t: f == 'email'}

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
____________ ERROR collecting test_dataclasses_json_cfg_config_1.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_1.py:4: in <module>
    from marshmallow_dataclass import MarshmallowField
E   ModuleNotFoundError: No module named 'marshmallow_dataclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_cfg_config_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""