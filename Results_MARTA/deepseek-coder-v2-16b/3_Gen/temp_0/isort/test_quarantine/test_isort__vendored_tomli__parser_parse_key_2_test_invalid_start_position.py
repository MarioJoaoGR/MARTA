
import pytest
from isort._vendored.tomli._parser import parse_key, Pos

def test_invalid_start_position():
    src = 'a.b.c'
    pos = Pos(-1)  # Negative position indicates an invalid start
    
    with pytest.raises(IndexError):
        parse_key(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_2_test_invalid_start_position.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_start_position __________________________

    def test_invalid_start_position():
        src = 'a.b.c'
        pos = Pos(-1)  # Negative position indicates an invalid start
    
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_2_test_invalid_start_position.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_2_test_invalid_start_position.py::test_invalid_start_position
============================== 1 failed in 0.13s ===============================
"""