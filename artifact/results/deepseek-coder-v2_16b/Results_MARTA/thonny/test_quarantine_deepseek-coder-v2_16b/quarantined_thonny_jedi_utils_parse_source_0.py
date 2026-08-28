
import pytest
from thonny.jedi_utils import parse_source
import parso



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_parse_simple_function __________________________

    def test_parse_simple_function():
        source = "def example(): return 42"
        ast = parse_source(source)
>       assert isinstance(ast, parso.parse_string.Module), f"Expected a Module object, but got {type(ast)}"
E       AttributeError: module 'parso' has no attribute 'parse_string'

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py:9: AttributeError
___________________________ test_parse_complex_code ____________________________

    def test_parse_complex_code():
        source = """
        def main():
            x = 10
            y = 20
            return x + y
        """
        ast = parse_source(source)
>       assert isinstance(ast, parso.parse_string.Module), f"Expected a Module object, but got {type(ast)}"
E       AttributeError: module 'parso' has no attribute 'parse_string'

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py:19: AttributeError
_________________________ test_parse_with_syntax_error _________________________

    def test_parse_with_syntax_error():
        source = "def invalid_code(): return"  # Syntax error in the function definition
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py::test_parse_simple_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py::test_parse_complex_code
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_parse_source_0.py::test_parse_with_syntax_error
============================== 3 failed in 0.11s ===============================
"""