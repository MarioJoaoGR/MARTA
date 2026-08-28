
import pytest
from unittest.mock import patch
from ast import parse as ast_parse
from ast import FunctionDef, ClassDef, Assign, Name
from apimd.parser import Parser





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('apimd.parser.Parser.new', return_value=Parser()):
            p = Parser.new(link=True, level=1)
            mock_class = ClassDef(name='MockClass', bases=[], body=[
>               FunctionDef(name='mock_function', args=ast_parse('arg1: int, arg2: str -> None').body[0].args)
            ])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = 'arg1: int, arg2: str -> None', filename = '<unknown>', mode = 'exec'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 1
E           arg1: int, arg2: str -> None
E                    ^
E       SyntaxError: invalid syntax

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: SyntaxError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('apimd.parser.Parser.new', return_value=Parser()):
            p = Parser.new(link=True, level=1)
            mock_class = ClassDef(name='MockClass', bases=[], body=[
>               FunctionDef(name='mock_function', args=ast_parse('arg1: int, arg2: str -> None').body[0].args),
                Assign(targets=[Name(id='invalid_attr')], value=ast_parse('42'))  # Invalid attribute assignment
            ])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = 'arg1: int, arg2: str -> None', filename = '<unknown>', mode = 'exec'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 1
E           arg1: int, arg2: str -> None
E                    ^
E       SyntaxError: invalid syntax

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: SyntaxError
___________________ test_default_initialization_and_parsing ____________________

    def test_default_initialization_and_parsing():
        with patch('apimd.parser.Parser.new', return_value=Parser()):
            p = Parser.new(link=True, level=1)
            with open("pkg_path", 'r') as f:
                pkg_content = f.read()
            p.parse('pkg_name', pkg_content)
>           assert 'Members' in p.doc['pkg_name']
E           assert 'Members' in '## Module `{}`\n<a id="{}"></a>\n\n'

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py:33: AssertionError
________________ test_parameterized_initialization_and_parsing _________________

    def test_parameterized_initialization_and_parsing():
        with patch('apimd.parser.Parser.new', return_value=Parser()):
            p = Parser.new(link=True, level=2, toc=False)
            with open("pkg_path", 'r') as f:
                pkg_content = f.read()
            p.parse('pkg_name', pkg_content)
>           assert 'Members' in p.doc['pkg_name']
E           assert 'Members' in '## Module `{}`\n<a id="{}"></a>\n\n'

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py:41: AssertionError
___________________________ test_parsing_from_string ___________________________

    def test_parsing_from_string():
        with patch('apimd.parser.Parser.new', return_value=Parser()):
            p = Parser.new(link=True, level=1)
            script_content = """
    class MyClass:
        def my_function(self, arg1: int, arg2: str) -> None:
            pass
    """
            p.parse('MyModule', script_content)
>           assert 'Members' in p.doc['MyClass']
E           KeyError: 'MyClass'

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py:52: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py::test_invalid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py::test_default_initialization_and_parsing
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py::test_parameterized_initialization_and_parsing
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser_class_api_0.py::test_parsing_from_string
============================== 5 failed in 0.11s ===============================
"""