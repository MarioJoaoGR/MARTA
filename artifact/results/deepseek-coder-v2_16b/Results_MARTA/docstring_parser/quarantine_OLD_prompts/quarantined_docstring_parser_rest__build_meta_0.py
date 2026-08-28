
import pytest
from unittest.mock import patch, call
from docstring_parser.rest import _build_meta, DocstringMeta, ParseError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_param _______________________________

    def test_valid_param():
        with patch('docstring_parser.rest._build_meta', autospec=True) as mock_build_meta:
            args = ['param', 'name', 'str']
            desc = 'Name of the entity'
            _build_meta(args, desc)
>           assert mock_build_meta.called
E           assert False
E            +  where False = <function _build_meta at 0x7f779e6ed750>.called

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:11: AssertionError
______________________________ test_valid_return _______________________________

    def test_valid_return():
        with patch('docstring_parser.rest._build_meta', autospec=True) as mock_build_meta:
            args = ['return', 'int']
            desc = 'The result is an integer.'
            _build_meta(args, desc)
>           assert mock_build_meta.called
E           assert False
E            +  where False = <function _build_meta at 0x7f779e734d30>.called

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:18: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('docstring_parser.rest._build_meta', autospec=True) as mock_build_meta:
            args = ['raises', 'ValueError']
            desc = 'If something happens, ValueError will be raised.'
>           with pytest.raises(ParseError):
E           Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:24: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_valid_param
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_valid_return
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_invalid_input
============================== 3 failed in 0.05s ===============================
"""