
import pytest
from isort._vendored.tomli._parser import parse_array, skip_comments_and_array_ws

@pytest.mark.parametrize("src, pos, expected", [
    ("[1, 2.5, 'string', [3, 4], {'key': 'value'}]", 0, "[1, 2.5, 'string', [3, 4], {'key': 'value'}]"),
    ("[1, 2.5, 'string', [3, 4], {'key': 'value'", 0, "Unclosed array")
])
def test_invalid_input(src, pos, expected):
    with pytest.raises(Exception) as excinfo:
        parse_array(src, pos, float)
    assert str(excinfo.value) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_1_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_invalid_input[[1, 2.5, 'string', [3, 4], {'key': 'value'}]-0-[1, 2.5, 'string', [3, 4], {'key': 'value'}]] _

src = "[1, 2.5, 'string', [3, 4], {'key': 'value'}]", pos = 0
expected = "[1, 2.5, 'string', [3, 4], {'key': 'value'}]"

    @pytest.mark.parametrize("src, pos, expected", [
        ("[1, 2.5, 'string', [3, 4], {'key': 'value'}]", 0, "[1, 2.5, 'string', [3, 4], {'key': 'value'}]"),
        ("[1, 2.5, 'string', [3, 4], {'key': 'value'", 0, "Unclosed array")
    ])
    def test_invalid_input(src, pos, expected):
        with pytest.raises(Exception) as excinfo:
            parse_array(src, pos, float)
>       assert str(excinfo.value) == expected
E       assert 'Expected "="...1, column 34)' == "[1, 2.5, 'st...y': 'value'}]"
E         
E         - [1, 2.5, 'string', [3, 4], {'key': 'value'}]
E         + Expected "=" after a key in a key/value pair (at line 1, column 34)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_1_test_invalid_input.py:12: AssertionError
_ test_invalid_input[[1, 2.5, 'string', [3, 4], {'key': 'value'-0-Unclosed array] _

src = "[1, 2.5, 'string', [3, 4], {'key': 'value'", pos = 0
expected = 'Unclosed array'

    @pytest.mark.parametrize("src, pos, expected", [
        ("[1, 2.5, 'string', [3, 4], {'key': 'value'}]", 0, "[1, 2.5, 'string', [3, 4], {'key': 'value'}]"),
        ("[1, 2.5, 'string', [3, 4], {'key': 'value'", 0, "Unclosed array")
    ])
    def test_invalid_input(src, pos, expected):
        with pytest.raises(Exception) as excinfo:
            parse_array(src, pos, float)
>       assert str(excinfo.value) == expected
E       assert 'Expected "="...1, column 34)' == 'Unclosed array'
E         
E         - Unclosed array
E         + Expected "=" after a key in a key/value pair (at line 1, column 34)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_1_test_invalid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_1_test_invalid_input.py::test_invalid_input[[1, 2.5, 'string', [3, 4], {'key': 'value'}]-0-[1, 2.5, 'string', [3, 4], {'key': 'value'}]]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_array_1_test_invalid_input.py::test_invalid_input[[1, 2.5, 'string', [3, 4], {'key': 'value'-0-Unclosed array]
============================== 2 failed in 0.11s ===============================
"""