
from flutes.fs import remove_prefix

def test_valid_input_happy_path():
    # Test removing a fully matching prefix
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"
    
    # Test removing a non-fully matching prefix with fully_match=False
    assert remove_prefix("preface", "prefix", fully_match=False) == "face"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test removing a fully matching prefix
        assert remove_prefix("https://github.com/huzecong/flutes", "https://") == "github.com/huzecong/flutes"
    
        # Test removing a non-fully matching prefix with fully_match=False
>       assert remove_prefix("preface", "prefix", fully_match=False) == "face"
E       AssertionError: assert 'ace' == 'face'
E         
E         - face
E         ? -
E         + ace

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_valid_input_happy_path.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.11s ===============================
"""