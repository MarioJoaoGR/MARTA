
import pytest
from typesystem.json_schema import get_valid_types




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_multiple_types ________________________

    def test_valid_input_multiple_types():
        result = get_valid_types({"type": ["null", "string"]})
>       assert result == ({'null', 'string'}, True)
E       AssertionError: assert ({'string'}, True) == ({'null', 'string'}, True)
E         
E         At index 0 diff: {'string'} != {'string', 'null'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py:7: AssertionError
________________________ test_invalid_input_empty_list _________________________

    def test_invalid_input_empty_list():
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py:10: Failed
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        with pytest.raises(TypeError):
>           get_valid_types(None)

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

data = None

    def get_valid_types(data: dict) -> typing.Tuple[typing.Set[str], bool]:
        """
        Returns a two-tuple of `(type_strings, allow_null)`.
        """
    
>       type_strings = data.get("type", [])
E       AttributeError: 'NoneType' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/json_schema.py:179: AttributeError
_____________________ test_invalid_input_missing_type_key ______________________

    def test_invalid_input_missing_type_key():
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py::test_valid_input_multiple_types
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py::test_invalid_input_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py::test_invalid_input_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_json_schema_get_valid_types_0.py::test_invalid_input_missing_type_key
============================== 4 failed in 0.15s ===============================
"""