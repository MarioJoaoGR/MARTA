
import pytest
from flutes.fs import remove_suffix

def test_valid_input_happy_path():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=True) == "https://github.com/huzecong"
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=False) == "https://github.com/huzecong/flutes"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_2_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
        assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
        assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=True) == "https://github.com/huzecong"
>       assert remove_suffix("https://github.com/huzecong/flutes", "/flutes", fully_match=False) == "https://github.com/huzecong/flutes"
E       AssertionError: assert 'https://github.com/huzecong' == 'https://gith...zecong/flutes'
E         
E         - https://github.com/huzecong/flutes
E         ?                            -------
E         + https://github.com/huzecong

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_2_test_valid_input_happy_path.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_2_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.10s ===============================

"""