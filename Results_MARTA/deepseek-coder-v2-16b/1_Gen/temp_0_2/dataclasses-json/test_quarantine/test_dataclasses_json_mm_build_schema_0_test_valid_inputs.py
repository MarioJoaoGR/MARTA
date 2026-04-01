
import pytest
from dataclasses import dataclass, fields
import typing
from marshmallow import Schema, post_load
from dataclasses_json.mm import build_schema

# Assuming _decode_dataclass, _ExtendedEncoder, and _handle_undefined_parameters_safe are defined in 'your_module'
# from your_module import _decode_dataclass, _ExtendedEncoder, _handle_undefined_parameters_safe

@pytest.fixture
def sample_dataclass():
    @dataclass
    class SampleDataclass:
        name: str
        age: int = 18

    return SampleDataclass

def test_valid_inputs(sample_dataclass):
    schema = build_schema(sample_dataclass, None, True, False)
    
    assert isinstance(schema, Schema)
    assert hasattr(schema, 'Meta')
    assert hasattr(schema, f'make_{sample_dataclass.__name__.lower()}')
    assert hasattr(schema, 'dumps')
    assert hasattr(schema, 'dump')

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

sample_dataclass = <class 'Test4DT_tests.test_dataclasses_json_mm_build_schema_0_test_valid_inputs.sample_dataclass.<locals>.SampleDataclass'>

    def test_valid_inputs(sample_dataclass):
        schema = build_schema(sample_dataclass, None, True, False)
    
>       assert isinstance(schema, Schema)
E       AssertionError: assert False
E        +  where False = isinstance(<class 'abc.SampledataclassSchema'>, Schema)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_valid_inputs.py:23: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_valid_inputs.py::test_valid_inputs
  /opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/marshmallow/fields.py:986: RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.
    super().__init__(**kwargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_valid_inputs.py::test_valid_inputs
========================= 1 failed, 1 warning in 0.03s =========================
"""