
from dataclasses import is_dataclass, make_dataclass
import pytest
from dataclasses_json.core import _decode_type

@pytest.fixture
def setup_test():
    pass

def test_edge_case_none(setup_test):
    # Test when value is None and infer_missing is True
    assert _decode_type(int, None, True) is None
    
    # Test when value is None and infer_missing is False
    with pytest.raises(TypeError):
        _decode_type(int, None, False)
    
    # Test when type_ is a dataclass and value is None
    DataClass = make_dataclass("DataClass", [("field1", int)])
    assert _decode_type(DataClass, None, True) == DataClass(field1=None)
    
    # Test when type_ is not a dataclass but value is None
    with pytest.raises(TypeError):
        _decode_type(int, None, True)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

setup_test = None

    def test_edge_case_none(setup_test):
        # Test when value is None and infer_missing is True
>       assert _decode_type(int, None, True) is None

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'int'>, field_value = None

    def _support_extended_types(field_type, field_value):
        if _issubclass_safe(field_type, datetime):
            # FIXME this is a hack to deal with mm already decoding
            # the issue is we want to leverage mm fields' missing argument
            # but need this for the object creation hook
            if isinstance(field_value, datetime):
                res = field_value
            else:
                tz = datetime.now(timezone.utc).astimezone().tzinfo
                res = datetime.fromtimestamp(field_value, tz=tz)
        elif _issubclass_safe(field_type, Decimal):
            res = (field_value
                   if isinstance(field_value, Decimal)
                   else Decimal(field_value))
        elif _issubclass_safe(field_type, UUID):
            res = (field_value
                   if isinstance(field_value, UUID)
                   else UUID(field_value))
        elif _issubclass_safe(field_type, (int, float, str, bool)):
            res = (field_value
                   if isinstance(field_value, field_type)
>                  else field_type(field_value))
E           TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

dataclasses-json/dataclasses_json/core.py:274: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.04s ===============================
"""