
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_valid_saxon_genitive ___________________________

    def test_valid_saxon_genitive():
        formatter = __StringFormatter('John s house')
        pattern = re.compile(r"(\b\w+)' s\b")
        match = pattern.search(formatter.input_string)
>       assert formatter._StringFormatter__fix_saxon_genitive(match) == "John's "

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x7f56c9335660>
regex_match = None

    def __fix_saxon_genitive(self, regex_match):
>       return regex_match.group(1).replace(' ', '') + ' '
E       AttributeError: 'NoneType' object has no attribute 'group'

/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/manipulation.py:242: AttributeError
___________________________ test_invalid_input_type ____________________________

    def test_invalid_input_type():
>       with pytest.raises(InvalidInputError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py:12: NameError
_________________________ test_no_match_saxon_genitive _________________________

    def test_no_match_saxon_genitive():
        formatter = __StringFormatter('Johns house')
        pattern = re.compile(r"(\b\w+)' s\b")
        match = pattern.search(formatter.input_string)
>       assert formatter._StringFormatter__fix_saxon_genitive(match) is None

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x7f56c9334100>
regex_match = None

    def __fix_saxon_genitive(self, regex_match):
>       return regex_match.group(1).replace(' ', '') + ' '
E       AttributeError: 'NoneType' object has no attribute 'group'

/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/manipulation.py:242: AttributeError
______________________ test_valid_saxon_genitive_no_space ______________________

    def test_valid_saxon_genitive_no_space():
        formatter = __StringFormatter("John's house")
        pattern = re.compile(r"(\b\w+)' s\b")
        match = pattern.search(formatter.input_string)
>       assert formatter._StringFormatter__fix_saxon_genitive(match) is None

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x7f56c9477e50>
regex_match = None

    def __fix_saxon_genitive(self, regex_match):
>       return regex_match.group(1).replace(' ', '') + ' '
E       AttributeError: 'NoneType' object has no attribute 'group'

/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/manipulation.py:242: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py::test_valid_saxon_genitive
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py::test_invalid_input_type
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py::test_no_match_saxon_genitive
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_2.py::test_valid_saxon_genitive_no_space
============================== 4 failed in 0.09s ===============================
"""