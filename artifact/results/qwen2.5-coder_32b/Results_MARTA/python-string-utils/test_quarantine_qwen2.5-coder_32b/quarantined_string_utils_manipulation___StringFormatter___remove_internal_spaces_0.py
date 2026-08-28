
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
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
____________ test___StringFormatter___remove_internal_spaces_basic _____________

    def test___StringFormatter___remove_internal_spaces_basic():
        formatter = __StringFormatter('hello   world')
>       result = re.sub(r'(\S+)\s+(\S+)', formatter.__remove_internal_spaces, "hello   world")
E       AttributeError: '__StringFormatter' object has no attribute '__remove_internal_spaces'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:7: AttributeError
_______ test___StringFormatter___remove_internal_spaces_multiple_groups ________

    def test___StringFormatter___remove_internal_spaces_multiple_groups():
        formatter = __StringFormatter('this  is  a  test')
>       result = re.sub(r'(\S+)\s+(\S+)', formatter.__remove_internal_spaces, "this  is  a  test")
E       AttributeError: '__StringFormatter' object has no attribute '__remove_internal_spaces'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:12: AttributeError
________________ test___StringFormatter___invalid_input_string _________________

    def test___StringFormatter___invalid_input_string():
>       with pytest.raises(InvalidInputError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:16: NameError
________________ test___StringFormatter___single_word_no_change ________________

    def test___StringFormatter___single_word_no_change():
        formatter = __StringFormatter('hello')
>       result = re.sub(r'(\S+)\s+(\S+)', formatter.__remove_internal_spaces, "hello")
E       AttributeError: '__StringFormatter' object has no attribute '__remove_internal_spaces'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:21: AttributeError
_________________ test___StringFormatter___no_internal_spaces __________________

    def test___StringFormatter___no_internal_spaces():
        formatter = __StringFormatter('helloworld')
>       result = re.sub(r'(\S+)\s+(\S+)', formatter.__remove_internal_spaces, "helloworld")
E       AttributeError: '__StringFormatter' object has no attribute '__remove_internal_spaces'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py:26: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py::test___StringFormatter___remove_internal_spaces_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py::test___StringFormatter___remove_internal_spaces_multiple_groups
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py::test___StringFormatter___invalid_input_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py::test___StringFormatter___single_word_no_change
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0.py::test___StringFormatter___no_internal_spaces
============================== 5 failed in 0.07s ===============================
"""