
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import pytest
from dataclasses_json.mm import SchemaF  # Corrected import from module 'dataclasses_json.mm'

@dataclass
class Person:
    name: str
    age: int = 0

@pytest.fixture
def schema_f():
    return SchemaF()

def test_loads(schema_f):
    json_data = '[{"name": "John Doe", "age": 30}, {"name": "Jane Doe", "age": 25}]'
    persons = schema_f.loads(json_data, many=True)
    assert isinstance(persons, list)
    assert all(isinstance(p, Person) for p in persons)
    assert [p.name for p in persons] == ["John Doe", "Jane Doe"]
    assert [p.age for p in persons] == [30, 25]

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_2_test_edge_cases.py E [100%]

==================================== ERRORS ====================================
_________________________ ERROR at setup of test_loads _________________________

    @pytest.fixture
    def schema_f():
>       return SchemaF()

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_2_test_edge_cases.py:14: 
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
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_2_test_edge_cases.py::test_loads
=============================== 1 error in 0.04s ===============================
"""