
import pytest
from blib2to3.pgen2.tokenize import tokenize
from io import BytesIO

def find_cookie(line: bytes) -> Optional[str]:
    try:
        line_string = line.decode("ascii")
    except UnicodeDecodeError:
        return None
    match = cookie_re.match(line_string)
    if not match:
        return None
    encoding = _get_normal_name(match.group(1))
    try:
        codec = lookup(encoding)
    except LookupError:
        raise SyntaxError("unknown encoding: " + encoding)

    if bom_found:
        if codec.name != "utf-8":
            raise SyntaxError("encoding problem: utf-8")
        encoding += "-sig"
    return encoding

# Test cases for find_cookie function
def test_find_cookie_valid_utf8():
    assert find_cookie(b"Cookie: utf-8") == 'utf-8'

def test_find_cookie_valid_utf8_bom():
    assert find_cookie(b"\xef\xbb\xbfThis is UTF-8 with BOM") == 'utf-8-sig'

def test_find_cookie_invalid_encoding():
    assert find_cookie(b"Invalid encoding") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
______ ERROR collecting test_src_blib2to3_pgen2_tokenize_find_cookie_0.py ______
/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_find_cookie_0.py:6: in <module>
    def find_cookie(line: bytes) -> Optional[str]:
E   NameError: name 'Optional' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_find_cookie_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""