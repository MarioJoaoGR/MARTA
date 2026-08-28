
import pytest
from docstring_parser.rest import _build_meta, ParseError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with pytest.raises(ParseError):
            _build_meta(['param'], 'Name of the entity')
    
        with pytest.raises(ParseError):
>           _build_meta([], 'Empty list should raise an error')

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_1.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = [], desc = 'Empty list should raise an error'

    def _build_meta(args: T.List[str], desc: str) -> DocstringMeta:
>       key = args[0]
E       IndexError: list index out of range

/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/rest.py:22: IndexError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_1.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_rest__build_meta_1.py::test_invalid_inputs
============================== 2 failed in 0.05s ===============================
"""