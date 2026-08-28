
import pytest
from dataclasses_json.core import _decode_letter_case_overrides


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__decode_letter_case_overrides_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_basic _____________________________

    def test_valid_case_basic():
        field_names = ['FirstName', 'LastName']
        overrides = {
            'FirstName': {'letter_case': lambda x: x.lower()},
            'LastName': {'letter_case': lambda x: x.upper()}
        }
>       result = _decode_letter_case_overrides(field_names, overrides)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__decode_letter_case_overrides_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['FirstName', 'LastName']
overrides = {'FirstName': {'letter_case': <function test_valid_case_basic.<locals>.<lambda> at 0x7f508ce7a170>}, 'LastName': {'letter_case': <function test_valid_case_basic.<locals>.<lambda> at 0x7f508cb96050>}}

    def _decode_letter_case_overrides(field_names, overrides):
        """Override letter case of field names for encode/decode"""
        names = {}
        for field_name in field_names:
            field_override = overrides.get(field_name)
            if field_override is not None:
>               letter_case = field_override.letter_case
E               AttributeError: 'dict' object has no attribute 'letter_case'

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/core.py:124: AttributeError
________________________ test_valid_case_title_override ________________________

    def test_valid_case_title_override():
        field_names = ['FullName']
        overrides = {
            'FullName': {'letter_case': lambda x: x.title()}
        }
>       result = _decode_letter_case_overrides(field_names, overrides)

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__decode_letter_case_overrides_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['FullName']
overrides = {'FullName': {'letter_case': <function test_valid_case_title_override.<locals>.<lambda> at 0x7f508cb95f30>}}

    def _decode_letter_case_overrides(field_names, overrides):
        """Override letter case of field names for encode/decode"""
        names = {}
        for field_name in field_names:
            field_override = overrides.get(field_name)
            if field_override is not None:
>               letter_case = field_override.letter_case
E               AttributeError: 'dict' object has no attribute 'letter_case'

/opt/marta/baselines/codamosa/replication/test-apps/dataclasses-json/dataclasses_json/core.py:124: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__decode_letter_case_overrides_0.py::test_valid_case_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__decode_letter_case_overrides_0.py::test_valid_case_title_override
============================== 2 failed in 0.08s ===============================
"""