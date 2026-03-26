
import pytest
from flutes.fs import remove_suffix

def test_error_case_invalid_suffix():
    # Test case for invalid suffix
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "suffix", fully_match=False) == "bug"
    with pytest.raises(ValueError):
        remove_suffix("https://github.com/huzecong/flutes", "invalid_suffix")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_case_invalid_suffix.py F [100%]

=================================== FAILURES ===================================
________________________ test_error_case_invalid_suffix ________________________

    def test_error_case_invalid_suffix():
        # Test case for invalid suffix
        assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
        assert remove_suffix("bugfix", "suffix", fully_match=False) == "bug"
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_case_invalid_suffix.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_error_case_invalid_suffix.py::test_error_case_invalid_suffix
============================== 1 failed in 0.13s ===============================
"""