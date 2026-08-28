
import pytest
from apimd.parser import Parser

# Test for valid input and default parser initialization

# Test for error handling when parsing an empty file
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_default_parser ________________________

    def test_valid_input_default_parser():
        p = Parser()
        with open("test_file.py", 'r') as f:
            content = f.read()
        p.parse('TestModule', content)
>       assert "def test_function():" in p.compile()
E       assert 'def test_function():' in '## Module `TestModule`\n<a id="testmodule"></a>\n\n### class MyClass\n\n*Full name:* `TestModule.MyClass`\n<a id="tes...ction"></a>\n\n| self | arg1 | arg2 | return |\n|:----:|:----:|:----:|:------:|\n| `Self` | `int` | `str` | `None` |\n'
E        +  where '## Module `TestModule`\n<a id="testmodule"></a>\n\n### class MyClass\n\n*Full name:* `TestModule.MyClass`\n<a id="tes...ction"></a>\n\n| self | arg1 | arg2 | return |\n|:----:|:----:|:----:|:------:|\n| `Self` | `int` | `str` | `None` |\n' = compile()
E        +    where compile = Parser(link=True, b_level=1, toc=False, level={'TestModule': 0, 'TestModule.MyClass': 0, 'TestModule.MyClass.my_functi... 'TestModule', 'TestModule.MyClass': 'TestModule', 'TestModule.MyClass.my_function': 'TestModule'}, alias={}, const={}).compile

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_1.py:11: AssertionError
----------------------------- Captured stderr call -----------------------------
[33mMissing documentation for TestModule[0m
[33mMissing documentation for TestModule.MyClass[0m
[33mMissing documentation for TestModule.MyClass.my_function[0m
------------------------------ Captured log call -------------------------------
WARNING  root:parser.py:597 Missing documentation for TestModule
WARNING  root:parser.py:597 Missing documentation for TestModule.MyClass
WARNING  root:parser.py:597 Missing documentation for TestModule.MyClass.my_function
________________________ test_error_handling_empty_file ________________________

    def test_error_handling_empty_file():
        p = Parser()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_1.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_1.py::test_valid_input_default_parser
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_1.py::test_error_handling_empty_file
============================== 2 failed in 0.06s ===============================
"""