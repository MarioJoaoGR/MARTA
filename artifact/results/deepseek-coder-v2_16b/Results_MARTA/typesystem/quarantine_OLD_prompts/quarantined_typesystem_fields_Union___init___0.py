
import pytest
from typesystem.fields import Field, Union



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_validate_non_null ____________________________

    def test_validate_non_null():
        class Field:
            def __init__(self, allow_null=False):
                self.allow_null = allow_null
    
            def validate_or_error(self, value, strict=False):
                if value is None and self.allow_null:
                    return None, None
                elif value is None:
                    return None, ValueError("May not be null.")
                else:
                    return value, None
    
        field1 = Field(allow_null=False)
        field2 = Field(allow_null=True)
        union = Union(any_of=[field1, field2])
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py:22: Failed
__________________________ test_validate_valid_value ___________________________

    def test_validate_valid_value():
        class Field:
            def __init__(self, allow_null=False):
                self.allow_null = allow_null
    
            def validate_or_error(self, value, strict=False):
                if value is None and self.allow_null:
                    return None, None
                elif value is None:
                    return None, ValueError("May not be null.")
                else:
                    return value, None
    
        field1 = Field(allow_null=True)
        field2 = Field(allow_null=False)
        union = Union(any_of=[field1, field2])
    
>       result, error = union.validate("valid_value")
E       ValueError: too many values to unpack (expected 2)

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py:42: ValueError
_________________________ test_validate_invalid_value __________________________

    def test_validate_invalid_value():
        class Field:
            def __init__(self, allow_null=False):
                self.allow_null = allow_null
    
            def validate_or_error(self, value, strict=False):
                if value is None and self.allow_null:
                    return None, None
                elif value is None:
                    return None, ValueError("May not be null.")
                else:
                    return value, None
    
        field1 = Field(allow_null=True)
        field2 = Field(allow_null=False)
        union = Union(any_of=[field1, field2])
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py:63: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py::test_validate_non_null
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py::test_validate_valid_value
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Union___init___0.py::test_validate_invalid_value
============================== 3 failed in 0.15s ===============================
"""