
import pytest
from typesystem.fields import Field, NO_DEFAULT


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Field_validation_error_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________ test_field_creation_with_required_parameters _________________

    def test_field_creation_with_required_parameters():
        field = Field(title="Age", description="The age of the person")
        assert field.title == "Age"
        assert field.description == "The age of the person"
>       assert field.default is NO_DEFAULT
E       AttributeError: 'Field' object has no attribute 'default'

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Field_validation_error_0.py:9: AttributeError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(AssertionError) as e:
            field = Field(title=123, description='Invalid input')
>       assert str(e.value) == "assert isinstance(title, str)"
E       AssertionError: assert '' == 'assert isins...e(title, str)'
E         
E         - assert isinstance(title, str)

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Field_validation_error_0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Field_validation_error_0.py::test_field_creation_with_required_parameters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_fields_Field_validation_error_0.py::test_invalid_inputs
============================== 2 failed in 0.13s ===============================
"""