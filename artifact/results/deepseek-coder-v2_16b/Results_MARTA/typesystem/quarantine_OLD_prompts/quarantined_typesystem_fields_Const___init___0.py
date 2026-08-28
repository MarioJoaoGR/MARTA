
import pytest
from typesystem.fields import Const


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Const___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_const_invalid_allow_null _________________________

    def test_const_invalid_allow_null():
        with pytest.raises(AssertionError) as e:
            Const(const=42, allow_null=True)
>       assert str(e.value) == "Must be the value '42'."
E       assert '' == "Must be the value '42'."
E         
E         - Must be the value '42'.

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Const___init___0.py:8: AssertionError
______________________ test_const_validate_invalid_value _______________________

    def test_const_validate_invalid_value():
        const_instance = Const(const=42)
        with pytest.raises(AssertionError) as e:
>           const_instance.validate(value="not 42")

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Const___init___0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <typesystem.fields.Const object at 0x7f0cd1d317e0>, value = 'not 42'
strict = False

    def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
        if value != self.const:
            if self.const is None:
                raise self.validation_error("only_null")
>           raise self.validation_error("const")
E           typesystem.base.ValidationError: Must be the value '42'.

/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/fields.py:761: ValidationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Const___init___0.py::test_const_invalid_allow_null
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Const___init___0.py::test_const_validate_invalid_value
============================== 2 failed in 0.15s ===============================
"""