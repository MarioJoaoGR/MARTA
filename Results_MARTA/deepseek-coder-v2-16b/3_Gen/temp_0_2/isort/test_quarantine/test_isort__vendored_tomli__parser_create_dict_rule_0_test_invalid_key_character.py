
from isort._vendored.tomli._parser import create_dict_rule, Output, Pos, Key
import pytest

def test_invalid_key_character():
    src = "invalid#key"
    pos = 0
    out = Output()
    
    with pytest.raises(ValueError) as excinfo:
        new_pos, key = create_dict_rule(src, pos, out)
        
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_dict_rule_0_test_invalid_key_character.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_key_character __________________________

    def test_invalid_key_character():
        src = "invalid#key"
        pos = 0
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_dict_rule_0_test_invalid_key_character.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_dict_rule_0_test_invalid_key_character.py::test_invalid_key_character
============================== 1 failed in 0.11s ===============================
"""