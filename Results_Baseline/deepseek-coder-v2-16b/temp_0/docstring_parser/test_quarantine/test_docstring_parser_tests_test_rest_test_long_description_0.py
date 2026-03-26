
def test_long_description():
    docstring = parse("This is a brief description.\n\nAnd this is more detailed documentation.")
    assert docstring.short_description == 'This is a brief description.'
    assert docstring.long_description == 'And this is more detailed documentation.'

def test_long_description():
    docstring = parse("Short description.")
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == ''

def test_long_description():
    docstring = parse("Another brief description.\n\n.. meta::\n   :property: value")
    assert docstring.short_description == 'Another brief description.'
    assert docstring.long_description == ''

def test_long_description():
    docstring = parse("")
    assert docstring.short_description == ''
    assert docstring.long_description == ''

def test_long_description():
    docstring = parse("And this is more detailed documentation.")
    assert docstring.short_description == ''
    assert docstring.long_description == 'And this is more detailed documentation.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_rest_test_long_description_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:3:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:7:0: E0102: function already defined line 2 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:8:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:12:0: E0102: function already defined line 2 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:13:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:17:0: E0102: function already defined line 2 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:18:16: E0602: Undefined variable 'parse' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:22:0: E0102: function already defined line 2 (function-redefined)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_long_description_0.py:23:16: E0602: Undefined variable 'parse' (undefined-variable)

"""