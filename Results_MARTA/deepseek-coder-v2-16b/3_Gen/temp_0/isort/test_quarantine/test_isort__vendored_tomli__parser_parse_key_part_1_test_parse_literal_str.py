
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS, Pos, suffixed_err

def test_parse_literal_str():
    src = "key'value"
    pos = Pos(0)
    new_pos, parsed_key = parse_key_part(src, pos)
    assert parsed_key == "key'value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_parse_literal_str.py F [100%]

=================================== FAILURES ===================================
____________________________ test_parse_literal_str ____________________________

    def test_parse_literal_str():
        src = "key'value"
        pos = Pos(0)
        new_pos, parsed_key = parse_key_part(src, pos)
>       assert parsed_key == "key'value"
E       assert 'key' == "key'value"
E         
E         - key'value
E         + key

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_parse_literal_str.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_parse_literal_str.py::test_parse_literal_str
============================== 1 failed in 0.13s ===============================
"""