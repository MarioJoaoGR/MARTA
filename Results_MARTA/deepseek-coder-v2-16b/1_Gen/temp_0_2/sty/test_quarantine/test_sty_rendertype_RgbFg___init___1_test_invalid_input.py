
from sty import RgbFg

def test_invalid_input():
    # Test initialization with invalid input types
    try:
        rgb = RgbFg("not an integer", 255, 0)
    except TypeError as e:
        assert str(e) == "R value must be an integer"
    else:
        raise AssertionError("Expected a TypeError")
    
    try:
        rgb = RgbFg(256, 255, 0)
    except ValueError as e:
        assert str(e) == "Red component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")
    
    try:
        rgb = RgbFg(-1, 255, 0)
    except ValueError as e:
        assert str(e) == "Red component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")
    
    try:
        rgb = RgbFg(255, "not an integer", 0)
    except TypeError as e:
        assert str(e) == "G value must be an integer"
    else:
        raise AssertionError("Expected a TypeError")
    
    try:
        rgb = RgbFg(255, 256, 0)
    except ValueError as e:
        assert str(e) == "Green component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")
    
    try:
        rgb = RgbFg(255, -1, 0)
    except ValueError as e:
        assert str(e) == "Green component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")
    
    try:
        rgb = RgbFg(255, 255, "not an integer")
    except TypeError as e:
        assert str(e) == "B value must be an integer"
    else:
        raise AssertionError("Expected a TypeError")
    
    try:
        rgb = RgbFg(255, 255, 256)
    except ValueError as e:
        assert str(e) == "Blue component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")
    
    try:
        rgb = RgbFg(255, 255, -1)
    except ValueError as e:
        assert str(e) == "Blue component out of range (0-255)"
    else:
        raise AssertionError("Expected a ValueError")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test initialization with invalid input types
        try:
            rgb = RgbFg("not an integer", 255, 0)
        except TypeError as e:
            assert str(e) == "R value must be an integer"
        else:
>           raise AssertionError("Expected a TypeError")
E           AssertionError: Expected a TypeError

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_invalid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""