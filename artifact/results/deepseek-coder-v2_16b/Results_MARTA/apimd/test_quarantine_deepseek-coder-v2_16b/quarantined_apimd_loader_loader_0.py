
import pytest
from apimd.loader import loader




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        result = loader('', '', False, 1, False)
        assert isinstance(result, str), "Expected a string output"
>       assert len(result) == 0, "Output for edge case should be empty"
E       AssertionError: Output for edge case should be empty
E       assert 250 == 0
E        +  where 250 = len('## Module `test_file`\n\n### class MyClass\n\n*Full name:* `test_file.MyClass`\n\n#### MyClass.my_function()\n\n*Full...y_function`\n\n| self | arg1 | arg2 | return |\n|:----:|:----:|:----:|:------:|\n| `Self` | `int` | `str` | `None` |\n')

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py:8: AssertionError
----------------------------- Captured stderr call -----------------------------
[37mtest_file <= /data/results/harness/sandbox/marta/test_file.py[0m
[37mscript <= /data/results/harness/sandbox/marta/script.py[0m
[33mMissing documentation for test_file[0m
[33mMissing documentation for test_file.MyClass[0m
[33mMissing documentation for test_file.MyClass.my_function[0m
------------------------------ Captured log call -------------------------------
DEBUG    root:loader.py:89 test_file <= /data/results/harness/sandbox/marta/test_file.py
DEBUG    root:loader.py:89 script <= /data/results/harness/sandbox/marta/script.py
WARNING  root:parser.py:597 Missing documentation for test_file
WARNING  root:parser.py:597 Missing documentation for test_file.MyClass
WARNING  root:parser.py:597 Missing documentation for test_file.MyClass.my_function
_______________________ test_loader_with_default_values ________________________

    def test_loader_with_default_values():
        result = loader('/path/to/root', '/path/to/working_dir', True, 2, True)
        assert isinstance(result, str), "Expected a string output"
>       assert len(result) == 0, "Output should be empty for default values and no packages found"
E       AssertionError: Output should be empty for default values and no packages found
E       assert 25 == 0
E        +  where 25 = len('**Table of contents:**\n\n\n')

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py:13: AssertionError
__________________________ test_loader_with_no_links ___________________________

    def test_loader_with_no_links():
        result = loader('/path/to/root', '/path/to/working_dir', False, 2, True)
        assert isinstance(result, str), "Expected a string output"
>       assert len(result) == 0, "Output should be empty when links are disabled"
E       AssertionError: Output should be empty when links are disabled
E       assert 25 == 0
E        +  where 25 = len('**Table of contents:**\n\n\n')

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py:18: AssertionError
___________________________ test_loader_with_no_toc ____________________________

    def test_loader_with_no_toc():
        result = loader('/path/to/root', '/path/to/working_dir', True, 2, False)
        assert isinstance(result, str), "Expected a string output"
>       assert len(result) == 0, "Output should be empty when TOC is disabled"
E       AssertionError: Output should be empty when TOC is disabled
E       assert 1 == 0
E        +  where 1 = len('\n')

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py::test_loader_with_default_values
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py::test_loader_with_no_links
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader_loader_0.py::test_loader_with_no_toc
============================== 4 failed in 0.06s ===============================
"""