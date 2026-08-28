
import pytest
from dataclasses import dataclass, field
from typing import Dict
from dataclasses_json.core import DataClassJsonMixin, FieldOverride, fields

# Assuming cfg is a module-level configuration object
# For the purpose of this test, we will mock its behavior using a simple class
class MockConfig:
    def __init__(self):
        self.encoders = {}
        self.decoders = {}
        self.mm_fields = {}

cfg = MockConfig()

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int
    details: Dict[str, str] = field(default_factory=dict)

def _user_overrides_or_exts(cls):
    global_metadata = {}
    encoders = cfg.encoders
    decoders = cfg.decoders
    mm_fields = cfg.mm_fields
    for field in fields(cls):
        if field.type in encoders:
            global_metadata[field.name] = {'encoder': encoders[field.type]}
        if field.type in decoders:
            global_metadata[field.name] = {'decoder': decoders[field.type]}
        if field.type in mm_fields:
            global_metadata[field.name] = {'mm_field': mm_fields[field.type]}
    try:
        cls_config = (cls.dataclass_json_config
                      if cls.dataclass_json_config is not None else {})
    except AttributeError:
        cls_config = {}

    overrides = {}
    for field in fields(cls):
        field_config = {}
        # first apply global overrides or extensions
        field_metadata = global_metadata.get(field.name, {})
        field_config.update(field_metadata)
        # then apply class-level overrides or extensions
        field_config.update(cls_config)
        # last apply field-level overrides or extensions
        field_config.update(field.metadata.get('dataclasses_json', {}))
        overrides[field.name] = FieldOverride(*map(field_config.get, ['encoder', 'decoder', 'mm_field']))
    return overrides

def test_user_overrides_or_exts_no_global_config():
    """Test that _user_overrides_or_exts returns empty configurations when no global config is set."""
    cfg.encoders = {}
    cfg.decoders = {}
    cfg.mm_fields = {}

    result = _user_overrides_or_exts(MyDataClass)
    
    assert all(isinstance(override, FieldOverride) for override in result.values())
    assert all(not any(getattr(override, attr) for attr in ['encoder', 'decoder', 'mm_field']) for override in result.values())

def test_user_overrides_or_exts_with_global_encoders():
    """Test that _user_overrides_or_exts applies global encoders correctly."""
    cfg.encoders = {str: lambda x: x.upper(), int: lambda x: str(x)}
    cfg.decoders = {}
    cfg.mm_fields = {}

    result = _user_overrides_or_exts(MyDataClass)
    
    assert result['name'].encoder('test') == 'TEST'
    assert result['age'].encoder(123) == '123'

def test_user_overrides_or_exts_with_global_decoders():
    """Test that _user_overrides_or_exts applies global decoders correctly."""
    cfg.encoders = {}
    cfg.decoders = {str: lambda x: x.lower(), int: lambda x: int(x)}
    cfg.mm_fields = {}

    result = _user_overrides_or_exts(MyDataClass)
    
    assert result['name'].decoder('TEST') == 'test'
    assert result['age'].decoder('123') == 123

def test_user_overrides_or_exts_with_global_mm_fields():
    """Test that _user_overrides_or_exts applies global mm_fields correctly."""
    cfg.encoders = {}
    cfg.decoders = {}
    cfg.mm_fields = {str: 'custom_str', int: 'custom_int'}

    result = _user_overrides_or_exts(MyDataClass)
    
    assert result['name'].mm_field == 'custom_str'
    assert result['age'].mm_field == 'custom_int'

def test_user_overrides_or_exts_with_class_level_config():
    """Test that _user_overrides_or_exts applies class-level configurations correctly."""
    cfg.encoders = {}
    cfg.decoders = {}
    cfg.mm_fields = {}

    MyDataClass.dataclass_json_config = {'name': FieldOverride(encoder=lambda x: x.title())}

    result = _user_overrides_or_exts(MyDataClass)
    
    assert result['name'].encoder('test') == 'Test'
    assert not hasattr(result['age'], 'encoder')

def test_user_overrides_or_exts_with_field_level_config():
    """Test that _user_overrides_or_exts applies field-level configurations correctly."""
    cfg.encoders = {}
    cfg.decoders = {}
    cfg.mm_fields = {}

    @dataclass
    class MyDataClass(DataClassJsonMixin):
        name: str = field(metadata={'dataclasses_json': {'encoder': lambda x: x.upper()}})
        age: int
        details: Dict[str, str] = field(default_factory=dict)

    result = _user_overrides_or_exts(MyDataClass)
    
    assert result['name'].encoder('test') == 'TEST'
    assert not hasattr(result['age'], 'encoder')

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
___ ERROR collecting test_dataclasses_json_core__user_overrides_or_exts_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__user_overrides_or_exts_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__user_overrides_or_exts_0.py:5: in <module>
    from dataclasses_json.core import DataClassJsonMixin, FieldOverride, fields
E   ImportError: cannot import name 'DataClassJsonMixin' from 'dataclasses_json.core' (/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/core.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__user_overrides_or_exts_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""