
import pytest
from dataclasses import dataclass
import typing
from dataclasses_json.mm import SchemaF

@dataclass
class A:
    attr1: str
    attr2: str

def test_invalid_inputs():
    schema = SchemaF()
    
    # Test with invalid input type (not a list)
    with pytest.raises(TypeError):
        schema.dumps("not_a_list")  # This should raise TypeError because "not_a_list" is not a list

    # Test with invalid object type in the list (not an instance of A)
    class B:
        pass
    
    obj_list = [A(attr1='value1', attr2='value2'), B()]  # List contains an instance of B which is not an instance of A
    with pytest.raises(TypeError):
        schema.dumps(obj_list)  # This should raise TypeError because the list contains an invalid object type

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       schema = SchemaF()

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_1_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <SchemaF(many=False)>, args = (), kwargs = {}

    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited.
        This class is helper only.
        """
    
        super().__init__(*args, **kwargs)
>       raise NotImplementedError()
E       NotImplementedError

dataclasses-json/dataclasses_json/mm.py:171: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""