
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import _decode_dataclass

@dataclass
class Person:
    name: str
    age: int

def make_instance(cls, kvs, **kwargs):
    return _decode_dataclass(cls, {**kvs, **kwargs})




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
>       person = make_instance(Person, {'name': 'Alice', 'age': 30})

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'test_dataclasses_json_mm_make_instance_1.Person'>
kvs = {'age': 30, 'name': 'Alice'}, kwargs = {}

    def make_instance(cls, kvs, **kwargs):
>       return _decode_dataclass(cls, {**kvs, **kwargs})
E       TypeError: _decode_dataclass() missing 1 required positional argument: 'infer_missing'

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:12: TypeError
________________________ test_partial_data_with_kwargs _________________________

    def test_partial_data_with_kwargs():
>       person = make_instance(Person, {'name': 'Bob'}, age=25)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'test_dataclasses_json_mm_make_instance_1.Person'>
kvs = {'name': 'Bob'}, kwargs = {'age': 25}

    def make_instance(cls, kvs, **kwargs):
>       return _decode_dataclass(cls, {**kvs, **kwargs})
E       TypeError: _decode_dataclass() missing 1 required positional argument: 'infer_missing'

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:12: TypeError
__________________ test_missing_field_with_default_via_kwargs __________________

    def test_missing_field_with_default_via_kwargs():
>       person = make_instance(Person, {}, name='Charlie', age=30)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'test_dataclasses_json_mm_make_instance_1.Person'>, kvs = {}
kwargs = {'age': 30, 'name': 'Charlie'}

    def make_instance(cls, kvs, **kwargs):
>       return _decode_dataclass(cls, {**kvs, **kwargs})
E       TypeError: _decode_dataclass() missing 1 required positional argument: 'infer_missing'

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:12: TypeError
________________________ test_extra_key_in_kvs_ignored _________________________

    def test_extra_key_in_kvs_ignored():
>       person = make_instance(Person, {'name': 'David', 'age': 40, 'extra': 'info'})

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'test_dataclasses_json_mm_make_instance_1.Person'>
kvs = {'age': 40, 'extra': 'info', 'name': 'David'}, kwargs = {}

    def make_instance(cls, kvs, **kwargs):
>       return _decode_dataclass(cls, {**kvs, **kwargs})
E       TypeError: _decode_dataclass() missing 1 required positional argument: 'infer_missing'

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py::test_partial_data_with_kwargs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py::test_missing_field_with_default_via_kwargs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_mm_make_instance_1.py::test_extra_key_in_kvs_ignored
============================== 4 failed in 0.08s ===============================
"""