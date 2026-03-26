
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Assuming this is the correct module path

@pytest.fixture(scope="module")
def source():
    return """
    def func(arg1=5): pass
    """
```

This fixture will provide a sample `source` code for the test case to use. Now, you can proceed with your test:

```python
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Assuming this is the correct module path

@pytest.fixture(scope="module")
def source():
    return """
    def func(arg1=5): pass
    """

def test_default_args(source, expected_is_optional, expected_type_name, expected_default):
    docstring = parse(source)
    assert docstring is not None
    assert len(docstring.params) == 1

    arg1 = docstring.params[0]
    assert arg1.is_optional == expected_is_optional
    assert arg1.type_name == expected_type_name
    assert arg1.default == expected_default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_edge_case_2
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_edge_case_2.py:10:1: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_edge_case_2, line 10)' (syntax-error)


"""