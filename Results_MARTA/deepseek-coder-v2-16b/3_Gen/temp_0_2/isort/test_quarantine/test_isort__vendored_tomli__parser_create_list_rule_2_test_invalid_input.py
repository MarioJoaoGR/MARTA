
import pytest
from isort._vendored.tomli._parser import create_list_rule, Output, Pos, Key, Flags, suffixed_err
from isort._vendored.tomli._parser import skip_chars, parse_key

@pytest.mark.parametrize("src, expected_error", [
    ("[[list]]\nkey=value", "Expected \"]]\" at the end of an array declaration"),
    ("[[list]", "Expected \"]]\" at the end of an array declaration")
])
def test_invalid_input(src: str, expected_error: str):
    pos = 0
    out = Output()
    with pytest.raises(suffixed_err) as exc_info:
        create_list_rule(src, pos, out)
    assert str(exc_info.value) == expected_error

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_2_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_invalid_input[[[list]]\nkey=value-Expected "]]" at the end of an array declaration] _

src = '[[list]]\nkey=value'
expected_error = 'Expected "]]" at the end of an array declaration'

    @pytest.mark.parametrize("src, expected_error", [
        ("[[list]]\nkey=value", "Expected \"]]\" at the end of an array declaration"),
        ("[[list]", "Expected \"]]\" at the end of an array declaration")
    ])
    def test_invalid_input(src: str, expected_error: str):
        pos = 0
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_2_test_invalid_input.py:12: TypeError
_ test_invalid_input[[[list]-Expected "]]" at the end of an array declaration] _

src = '[[list]'
expected_error = 'Expected "]]" at the end of an array declaration'

    @pytest.mark.parametrize("src, expected_error", [
        ("[[list]]\nkey=value", "Expected \"]]\" at the end of an array declaration"),
        ("[[list]", "Expected \"]]\" at the end of an array declaration")
    ])
    def test_invalid_input(src: str, expected_error: str):
        pos = 0
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_2_test_invalid_input.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_2_test_invalid_input.py::test_invalid_input[[[list]]\nkey=value-Expected "]]" at the end of an array declaration]
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_2_test_invalid_input.py::test_invalid_input[[[list]-Expected "]]" at the end of an array declaration]
============================== 2 failed in 0.13s ===============================
"""