
import pytest
from docstring_parser.rest import _build_meta, DocstringMeta, ParseError

# Define constants for keywords as per the function implementation
PARAM_KEYWORDS = ['param']
RETURNS_KEYWORDS = ['return']
YIELDS_KEYWORDS = ['yield', 'yieldeffect']  # Assuming these are defined in your module
RAISES_KEYWORDS = ['raises']



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
____________________________ test_valid_param_input ____________________________

    def test_valid_param_input():
        meta = _build_meta(['param', 'name', 'str'], 'Name of the entity')
        assert isinstance(meta, DocstringMeta)
        assert meta.args == ['param', 'name', 'str']
        assert meta.description == 'Name of the entity'
>       assert meta.arg_name == 'name'
E       AssertionError: assert 'str' == 'name'
E         
E         - name
E         + str

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:16: AssertionError
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
>       meta = _build_meta(None, 'No description provided')

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = None, desc = 'No description provided'

    def _build_meta(args: T.List[str], desc: str) -> DocstringMeta:
>       key = args[0]
E       TypeError: 'NoneType' object is not subscriptable

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/rest.py:22: TypeError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py:30: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_valid_param_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_edge_case_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_0.py::test_invalid_input_error_handling
============================== 3 failed in 0.06s ===============================
"""