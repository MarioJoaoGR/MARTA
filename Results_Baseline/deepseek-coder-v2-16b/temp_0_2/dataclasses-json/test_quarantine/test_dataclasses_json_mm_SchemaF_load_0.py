
import pytest
from dataclasses_json import Undefined, dataclass_json
from dataclasses import dataclass

# Define a sample dataclass with some undefined parameters
@dataclass_json
@dataclass
class SampleDataClass:
    name: str
    age: int
    city: str = None  # This parameter is optional and can be undefined

def test_sample_data_class_include():
    try:
        data_include = SampleDataClass(name="Jane Doe", age=30, city=Undefined.INCLUDE)
        assert data_include.city is None, f"Expected city to be None but got {data_include.city}"
    except Exception as e:
        pytest.fail("Unexpected error using INCLUDE strategy: " + str(e))

def test_sample_data_class_raise():
    with pytest.raises(Exception):
        SampleDataClass(name="Alice Smith", age=25, city=Undefined.RAISE)

def test_sample_data_class_exclude():
    data_exclude = SampleDataClass(name="Bob Johnson", age=35, city=Undefined.EXCLUDE)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_sample_data_class_include ________________________

    def test_sample_data_class_include():
        try:
            data_include = SampleDataClass(name="Jane Doe", age=30, city=Undefined.INCLUDE)
>           assert data_include.city is None, f"Expected city to be None but got {data_include.city}"
E           AssertionError: Expected city to be None but got Undefined.INCLUDE
E           assert <Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>> is None
E            +  where <Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>> = SampleDataClass(name='Jane Doe', age=30, city=<Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>>).city

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py:17: AssertionError

During handling of the above exception, another exception occurred:

    def test_sample_data_class_include():
        try:
            data_include = SampleDataClass(name="Jane Doe", age=30, city=Undefined.INCLUDE)
            assert data_include.city is None, f"Expected city to be None but got {data_include.city}"
        except Exception as e:
>           pytest.fail("Unexpected error using INCLUDE strategy: " + str(e))
E           Failed: Unexpected error using INCLUDE strategy: Expected city to be None but got Undefined.INCLUDE
E           assert <Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>> is None
E            +  where <Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>> = SampleDataClass(name='Jane Doe', age=30, city=<Undefined.INCLUDE: <class 'dataclasses_json.undefined._CatchAllUndefinedParameters'>>).city

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py:19: Failed
_________________________ test_sample_data_class_raise _________________________

    def test_sample_data_class_raise():
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py::test_sample_data_class_include
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0.py::test_sample_data_class_raise
========================= 2 failed, 1 passed in 0.03s ==========================

"""