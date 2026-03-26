
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF
import typing

# Assuming TOneOrMulti is a placeholder for a type hint that represents either a single object or a list of objects.
TOneOrMulti = typing.Union[dict, list]  # Example type hint

@pytest.fixture
def schema_f():
    return SchemaF()

def test_invalid_inputs(schema_f):
    with pytest.raises(NotImplementedError):
        # Attempting to instantiate the class should raise NotImplementedError
        schema_f.__init__()

    # Test invalid inputs for dumps method
    obj = {"key": "value"}
    with pytest.raises(NotImplementedError):
        schema_f.dumps(obj)
    
    objs = [{"key1": "value1"}, {"key2": "value2"}]
    with pytest.raises(NotImplementedError):
        schema_f.dumps(objs, many=True)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_invalid_inputs _____________________

    @pytest.fixture
    def schema_f():
>       return SchemaF()

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py:12: 
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
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_invalid_inputs.py::test_invalid_inputs
=============================== 1 error in 0.04s ===============================

"""