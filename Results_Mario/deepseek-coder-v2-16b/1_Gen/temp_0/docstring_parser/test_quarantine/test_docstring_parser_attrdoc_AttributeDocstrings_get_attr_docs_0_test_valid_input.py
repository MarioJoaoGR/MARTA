
import ast
from unittest import mock
from docstring_parser.attrdoc import AttributeDocstrings

def test_valid_input():
    class MyClass:
        attr1: str = "default1"
        attr2: int = 2
    
    visitor = AttributeDocstrings()
    
    # Mocking inspect.getsource to return the source code of MyClass
    with mock.patch('inspect.getsource', return_value=ast.unparse(ast.parse("class MyClass:\n    attr1: str = 'default1'\n    attr2: int = 2"))):
        result = visitor.get_attr_docs(MyClass)
    
    assert isinstance(result, dict)
    assert len(result) == 2
    assert "attr1" in result and "attr2" in result
    assert result["attr1"] == ("", "str", "'default1'")
    assert result["attr2"] == ("", "int", "2")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        class MyClass:
            attr1: str = "default1"
            attr2: int = 2
    
        visitor = AttributeDocstrings()
    
        # Mocking inspect.getsource to return the source code of MyClass
        with mock.patch('inspect.getsource', return_value=ast.unparse(ast.parse("class MyClass:\n    attr1: str = 'default1'\n    attr2: int = 2"))):
            result = visitor.get_attr_docs(MyClass)
    
        assert isinstance(result, dict)
>       assert len(result) == 2
E       assert 0 == 2
E        +  where 0 = len({})

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================

"""