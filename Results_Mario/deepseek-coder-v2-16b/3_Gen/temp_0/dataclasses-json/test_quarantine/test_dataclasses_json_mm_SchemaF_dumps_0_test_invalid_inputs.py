
import pytest
from dataclasses_json.mm import SchemaF

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()  # This should raise NotImplementedError
    
    with pytest.raises(NotImplementedError):
        schema = SchemaF(123)  # This should also raise NotImplementedError, as the constructor does not accept parameters

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(NotImplementedError):
            schema = SchemaF()  # This should raise NotImplementedError
    
        with pytest.raises(NotImplementedError):
>           schema = SchemaF(123)  # This should also raise NotImplementedError, as the constructor does not accept parameters

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'SchemaF' object has no attribute 'many'") raised in repr()] SchemaF object at 0x102a56d70>
args = (123,), kwargs = {}

    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited.
        This class is helper only.
        """
    
>       super().__init__(*args, **kwargs)
E       TypeError: Schema.__init__() takes 1 positional argument but 2 were given

dataclasses-json/dataclasses_json/mm.py:170: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""