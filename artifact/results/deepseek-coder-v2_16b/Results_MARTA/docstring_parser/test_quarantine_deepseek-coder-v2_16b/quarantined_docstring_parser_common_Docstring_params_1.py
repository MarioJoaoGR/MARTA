
import pytest
from docstring_parser.common import Docstring, DocstringParam

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_common_Docstring_params_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_params _______________________________

    def test_valid_params():
        class DocstringParam:
            def __init__(self, arg_name, type_name, is_optional, default):
                self.arg_name = arg_name
                self.type_name = type_name
                self.is_optional = is_optional
                self.default = default
    
        doc = Docstring()
        param1 = DocstringParam('param1', 'int', False, 0)
        doc.meta.append(param1)
    
>       assert len(doc.params()) == 1
E       TypeError: 'list' object is not callable

/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_common_Docstring_params_1.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_common_Docstring_params_1.py::test_valid_params
============================== 1 failed in 0.05s ===============================
"""