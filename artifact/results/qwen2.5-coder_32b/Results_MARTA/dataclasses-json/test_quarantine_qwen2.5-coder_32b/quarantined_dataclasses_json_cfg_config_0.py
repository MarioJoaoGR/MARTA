
import pytest
from dataclasses_json.cfg import config, LetterCase

def test_config_custom_encoder_decoder():
    def custom_encoder(obj):
        return str(obj)

    def custom_decoder(data):
        return int(data)

    metadata = config(encoder=custom_encoder, decoder=custom_decoder)
    assert metadata['dataclasses_json']['encoder'] == custom_encoder
    assert metadata['dataclasses_json']['decoder'] == custom_decoder

def test_config_letter_case_camel():
    metadata = config(letter_case=LetterCase.CAMEL)
    assert metadata['dataclasses_json']['letter_case'] is LetterCase.CAMEL

def test_config_undefined_exclude():
    metadata = config(undefined='EXCLUDE')
    assert metadata['dataclasses_json']['undefined'].name == 'EXCLUDE'

def test_config_field_name_with_letter_case():
    from dataclasses_json import LetterCase

    def custom_encoder(obj):
        return str(obj)

    def custom_decoder(data):
        return int(data)

    metadata = config(
        encoder=custom_encoder,
        decoder=custom_decoder,
        letter_case=LetterCase.CAMEL,
        field_name='user_id'
    )
    assert metadata['dataclasses_json']['field_name'] == 'user_id'
    assert metadata['dataclasses_json']['letter_case'](metadata['dataclasses_json']['field_name']) == 'userId'

def test_config_exclude_fields():
    def exclude_fields(name, value):
        return name.startswith('temp_')

    metadata = config(exclude=exclude_fields)
    assert metadata['dataclasses_json']['exclude'] is exclude_fields

def test_config_combining_multiple_settings():
    from dataclasses_json import LetterCase

    def custom_encoder(obj):
        return str(obj)

    def custom_decoder(data):
        return int(data)

    metadata = config(
        encoder=custom_encoder,
        decoder=custom_decoder,
        letter_case=LetterCase.CAMEL,
        undefined='EXCLUDE',
        field_name='user_id',
        exclude=lambda name, value: name.startswith('temp_')
    )
    assert metadata['dataclasses_json']['encoder'] == custom_encoder
    assert metadata['dataclasses_json']['decoder'] == custom_decoder
    assert metadata['dataclasses_json']['letter_case'] is LetterCase.CAMEL
    assert metadata['dataclasses_json']['undefined'].name == 'EXCLUDE'
    assert metadata['dataclasses_json']['field_name'] == 'user_id'
    assert callable(metadata['dataclasses_json']['exclude'])

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
____________ ERROR collecting test_dataclasses_json_cfg_config_0.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_cfg_config_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_cfg_config_0.py:3: in <module>
    from dataclasses_json.cfg import config, LetterCase
E   ImportError: cannot import name 'LetterCase' from 'dataclasses_json.cfg' (/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/cfg.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_cfg_config_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""