
from isort._vendored.tomli._parser import parse_key_part, Pos
import pytest

def test_invalid_key_initial_char():
    src = '1name = 123'
    pos = Pos(0)
    
    with pytest.raises(Exception):
        parse_key_part(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_2_test_invalid_key_initial_char.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_key_initial_char _________________________

    def test_invalid_key_initial_char():
        src = '1name = 123'
        pos = Pos(0)
    
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_2_test_invalid_key_initial_char.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_2_test_invalid_key_initial_char.py::test_invalid_key_initial_char
============================== 1 failed in 0.11s ===============================
"""