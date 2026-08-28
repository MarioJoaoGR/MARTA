
import pytest
from docstring_parser.numpydoc import Section






"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_____________________ test_title_pattern_matches_correctly _____________________

    def test_title_pattern_matches_correctly():
        section = Section("Parameters", "param_key")
>       pattern = section.title_pattern()
E       TypeError: 'str' object is not callable

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:7: TypeError
____________________ test_invalid_inputs_raises_type_error _____________________

    def test_invalid_inputs_raises_type_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:11: Failed
____________ test_invalid_inputs_with_none_title_raises_type_error _____________

    def test_invalid_inputs_with_none_title_raises_type_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:15: Failed
_____________ test_invalid_inputs_with_none_key_raises_type_error ______________

    def test_invalid_inputs_with_none_key_raises_type_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:19: Failed
_________ test_invalid_inputs_with_non_string_title_raises_type_error __________

    def test_invalid_inputs_with_non_string_title_raises_type_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:23: Failed
__________ test_invalid_inputs_with_non_string_key_raises_type_error ___________

    def test_invalid_inputs_with_non_string_key_raises_type_error():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py:27: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_title_pattern_matches_correctly
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_invalid_inputs_raises_type_error
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_invalid_inputs_with_none_title_raises_type_error
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_invalid_inputs_with_none_key_raises_type_error
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_invalid_inputs_with_non_string_title_raises_type_error
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_Section_title_pattern_0.py::test_invalid_inputs_with_non_string_key_raises_type_error
============================== 6 failed in 0.06s ===============================
"""