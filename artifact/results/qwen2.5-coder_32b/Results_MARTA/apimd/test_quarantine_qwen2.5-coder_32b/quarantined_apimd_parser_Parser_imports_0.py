
import pytest
from apimd.parser import Parser




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________________ test_valid_imports ______________________________

    def test_valid_imports():
        parser = Parser()
        source_code = """
    import os
    from sys import path as p
    """
        parser.parse('test_package', source_code)
        assert 'os' in parser.alias.values()
>       assert 'p' in parser.alias.values()
E       assert 'p' in dict_values(['os', 'sys.path'])
E        +  where dict_values(['os', 'sys.path']) = <built-in method values of dict object at 0x7f9fc9012ec0>()
E        +    where <built-in method values of dict object at 0x7f9fc9012ec0> = {'test_package.os': 'os', 'test_package.p': 'sys.path'}.values
E        +      where {'test_package.os': 'os', 'test_package.p': 'sys.path'} = Parser(link=True, b_level=1, toc=False, level={'test_package': 0}, doc={'test_package': '## Module `{}`\n<a id="{}"></...set()}, root={'test_package': 'test_package'}, alias={'test_package.os': 'os', 'test_package.p': 'sys.path'}, const={}).alias

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py:13: AssertionError
_____________________________ test_invalid_imports _____________________________

    def test_invalid_imports():
        parser = Parser()
    
        # Test unknown module
        source_code_unknown_module = "import unknown_module"
>       with pytest.raises(ModuleNotFoundError):
E       Failed: DID NOT RAISE <class 'ModuleNotFoundError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py:20: Failed
_________________________ test_from_import_with_alias __________________________

    def test_from_import_with_alias():
        parser = Parser()
        source_code = """
    from math import sqrt as square_root
    """
        parser.parse('test_package', source_code)
>       assert 'square_root' in parser.alias.values()
E       assert 'square_root' in dict_values(['math.sqrt'])
E        +  where dict_values(['math.sqrt']) = <built-in method values of dict object at 0x7f9fc8657d80>()
E        +    where <built-in method values of dict object at 0x7f9fc8657d80> = {'test_package.square_root': 'math.sqrt'}.values
E        +      where {'test_package.square_root': 'math.sqrt'} = Parser(link=True, b_level=1, toc=False, level={'test_package': 0}, doc={'test_package': '## Module `{}`\n<a id="{}"></...est_package': set()}, root={'test_package': 'test_package'}, alias={'test_package.square_root': 'math.sqrt'}, const={}).alias

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py:29: AssertionError
____________________________ test_relative_imports _____________________________

    def test_relative_imports():
        parser = Parser()
        source_code = """
    from ..module import function
    """
        parser.parse('test_package.subpackage', source_code)
>       assert 'function' in parser.alias.values()
E       AssertionError: assert 'function' in dict_values(['test_package.module.function'])
E        +  where dict_values(['test_package.module.function']) = <built-in method values of dict object at 0x7f9fc8657140>()
E        +    where <built-in method values of dict object at 0x7f9fc8657140> = {'test_package.subpackage.function': 'test_package.module.function'}.values
E        +      where {'test_package.subpackage.function': 'test_package.module.function'} = Parser(link=True, b_level=1, toc=False, level={'test_package.subpackage': 1}, doc={'test_package.subpackage': '## Modu...age': 'test_package.subpackage'}, alias={'test_package.subpackage.function': 'test_package.module.function'}, const={}).alias

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py:37: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py::test_valid_imports
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py::test_invalid_imports
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py::test_from_import_with_alias
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_imports_0.py::test_relative_imports
============================== 4 failed in 0.07s ===============================
"""