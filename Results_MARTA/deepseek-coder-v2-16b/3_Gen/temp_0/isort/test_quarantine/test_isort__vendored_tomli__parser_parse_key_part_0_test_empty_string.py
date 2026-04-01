
import pytest
from typing import Tuple, Optional
from isort._vendored.tomli._parser import BARE_KEY_CHARS, parse_key_part, Pos, suffixed_err

def test_empty_string():
    src = ''
    pos = Pos(0)
    
    with pytest.raises(suffixed_err):
        new_pos, parsed_key = parse_key_part(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_empty_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_string _______________________________

    def test_empty_string():
        src = ''
        pos = Pos(0)
    
>       with pytest.raises(suffixed_err):
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_empty_string.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_empty_string.py::test_empty_string
============================== 1 failed in 0.11s ===============================
"""