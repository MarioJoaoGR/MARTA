
import pytest
from flutes.fs import remove_suffix

def test_remove_suffix():
    # Test removing a fully matching suffix
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    
    # Test removing a non-fully matching suffix with fully_match=False
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
    
    # Test removing a suffix that is not present
    assert remove_suffix("https://github.com/huzecong", "/flutes") == "https://github.com/huzecong"
    
    # Test removing an empty suffix
    assert remove_suffix("test", "") == "test"
    
    # Test removing a suffix from an empty string
    assert remove_suffix("", "empty") == ""
    
    # Test removing a suffix with fully_match=True and it is not fully matching
    with pytest.raises(ValueError):
        remove_suffix("https://github.com/huzecong", "/flutes")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________________ test_remove_suffix ______________________________

    def test_remove_suffix():
        # Test removing a fully matching suffix
        assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    
        # Test removing a non-fully matching suffix with fully_match=False
        assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
    
        # Test removing a suffix that is not present
        assert remove_suffix("https://github.com/huzecong", "/flutes") == "https://github.com/huzecong"
    
        # Test removing an empty suffix
        assert remove_suffix("test", "") == "test"
    
        # Test removing a suffix from an empty string
        assert remove_suffix("", "empty") == ""
    
        # Test removing a suffix with fully_match=True and it is not fully matching
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_handling.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_handling.py::test_remove_suffix
============================== 1 failed in 0.08s ===============================

"""