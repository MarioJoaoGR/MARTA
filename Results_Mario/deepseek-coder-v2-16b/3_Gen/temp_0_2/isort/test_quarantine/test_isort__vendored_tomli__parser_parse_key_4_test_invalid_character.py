
from typing import Tuple
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, Key

def test_invalid_character():
    src = "invalid#key"
    pos = 0
    with pytest.raises(ValueError) as excinfo:
        new_pos, key = parse_key(src, pos)
    assert str(excinfo.value) == "Invalid initial character for a key part (at line 1, column 1)"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_4_test_invalid_character.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_character ____________________________

    def test_invalid_character():
        src = "invalid#key"
        pos = 0
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_4_test_invalid_character.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_4_test_invalid_character.py::test_invalid_character
============================== 1 failed in 0.11s ===============================
"""