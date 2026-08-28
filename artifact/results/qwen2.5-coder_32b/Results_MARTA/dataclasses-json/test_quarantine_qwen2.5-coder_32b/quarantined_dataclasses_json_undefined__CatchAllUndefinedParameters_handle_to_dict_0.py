
import pytest
from dataclasses import dataclass, field
from typing import Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@dataclass
class MyDataClass(_CatchAllUndefinedParameters):
    defined_field: int
    catch_all: Optional[Dict] = field(default_factory=dict)




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________ test_handle_to_dict_with_undefined_parameters _________________

    def test_handle_to_dict_with_undefined_parameters():
        obj = MyDataClass(defined_field=10, catch_all={'undefined_param': 'value'})
        kvs = {'defined_field': 30, 'catch_all': {'yet_another_field': 'more_values'}}
>       result_dict = MyDataClass.handle_to_dict(obj, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:196: in handle_to_dict
    _CatchAllUndefinedParameters._get_catch_all_field(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = MyDataClass(defined_field=10, catch_all={'undefined_param': 'value'})

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        catch_all_fields = list(
            filter(lambda f: f.type == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:249: UndefinedParameterError
_________________ test_handle_to_dict_no_undefined_parameters __________________

    def test_handle_to_dict_no_undefined_parameters():
        obj = MyDataClass(defined_field=10, catch_all={})
        kvs = {'defined_field': 40, 'catch_all': {}}
>       result_dict = MyDataClass.handle_to_dict(obj, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:196: in handle_to_dict
    _CatchAllUndefinedParameters._get_catch_all_field(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = MyDataClass(defined_field=10, catch_all={})

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        catch_all_fields = list(
            filter(lambda f: f.type == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:249: UndefinedParameterError
______________ test_handle_to_dict_multiple_undefined_parameters _______________

    def test_handle_to_dict_multiple_undefined_parameters():
        obj = MyDataClass(defined_field=10, catch_all={'field1': 'value1', 'field2': 'value2'})
        kvs = {'defined_field': 50, 'catch_all': {'field1': 'value1', 'field2': 'value2'}}
>       result_dict = MyDataClass.handle_to_dict(obj, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:196: in handle_to_dict
    _CatchAllUndefinedParameters._get_catch_all_field(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = MyDataClass(defined_field=10, catch_all={'field1': 'value1', 'field2': 'value2'})

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        catch_all_fields = list(
            filter(lambda f: f.type == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:249: UndefinedParameterError
__________________ test_handle_to_dict_empty_catch_all_field ___________________

    def test_handle_to_dict_empty_catch_all_field():
        obj = MyDataClass(defined_field=10, catch_all=None)
        kvs = {'defined_field': 60, 'catch_all': None}
>       result_dict = MyDataClass.handle_to_dict(obj, kvs)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:196: in handle_to_dict
    _CatchAllUndefinedParameters._get_catch_all_field(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = MyDataClass(defined_field=10, catch_all=None)

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        catch_all_fields = list(
            filter(lambda f: f.type == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/undefined.py:249: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py::test_handle_to_dict_with_undefined_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py::test_handle_to_dict_no_undefined_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py::test_handle_to_dict_multiple_undefined_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_to_dict_0.py::test_handle_to_dict_empty_catch_all_field
============================== 4 failed in 0.10s ===============================
"""