
from dataclasses_json.utils import _issubclass_safe
import pytest

def test_invalid_input():
    cls = None
    classinfo = object()  # Creating an instance of object, not a type
    
    # Test when cls is None
    assert not _issubclass_safe(cls, classinfo), "Expected False when cls is None"
    
    # Test when classinfo is an instance (not a type)
    with pytest.raises(TypeError):  # Because isinstance(cls, classinfo) would raise TypeError
        assert not _issubclass_safe(int, classinfo), "Expected False when classinfo is an instance"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        cls = None
        classinfo = object()  # Creating an instance of object, not a type
    
        # Test when cls is None
        assert not _issubclass_safe(cls, classinfo), "Expected False when cls is None"
    
        # Test when classinfo is an instance (not a type)
>       with pytest.raises(TypeError):  # Because isinstance(cls, classinfo) would raise TypeError
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_2_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__issubclass_safe_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""