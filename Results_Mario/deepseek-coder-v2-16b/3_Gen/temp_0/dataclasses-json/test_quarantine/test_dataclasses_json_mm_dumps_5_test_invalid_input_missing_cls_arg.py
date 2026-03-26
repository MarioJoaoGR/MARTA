
import pytest
from dataclasses_json import mm  # Assuming this is the correct module to import for Schema and _ExtendedEncoder

class TestSchemaDumps:
    @pytest.mark.parametrize("kwargs", [{}, {'cls': None}])
    def test_invalid_input_missing_cls_arg(self, kwargs):
        schema = mm.Schema()  # Assuming this creates an instance of Schema
        with pytest.raises(TypeError) as excinfo:
            schema.dumps(**kwargs)
        assert "missing a required argument" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________ TestSchemaDumps.test_invalid_input_missing_cls_arg[kwargs0] __________

self = <Test4DT_tests.test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.TestSchemaDumps object at 0x1027dec80>
kwargs = {}

    @pytest.mark.parametrize("kwargs", [{}, {'cls': None}])
    def test_invalid_input_missing_cls_arg(self, kwargs):
        schema = mm.Schema()  # Assuming this creates an instance of Schema
        with pytest.raises(TypeError) as excinfo:
            schema.dumps(**kwargs)
>       assert "missing a required argument" in str(excinfo.value)
E       assert 'missing a required argument' in "Schema.dumps() missing 1 required positional argument: 'obj'"
E        +  where "Schema.dumps() missing 1 required positional argument: 'obj'" = str(TypeError("Schema.dumps() missing 1 required positional argument: 'obj'"))
E        +    where TypeError("Schema.dumps() missing 1 required positional argument: 'obj'") = <ExceptionInfo TypeError("Schema.dumps() missing 1 required positional argument: 'obj'") tblen=1>.value

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.py:11: AssertionError
_________ TestSchemaDumps.test_invalid_input_missing_cls_arg[kwargs1] __________

self = <Test4DT_tests.test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.TestSchemaDumps object at 0x1027dece0>
kwargs = {'cls': None}

    @pytest.mark.parametrize("kwargs", [{}, {'cls': None}])
    def test_invalid_input_missing_cls_arg(self, kwargs):
        schema = mm.Schema()  # Assuming this creates an instance of Schema
        with pytest.raises(TypeError) as excinfo:
            schema.dumps(**kwargs)
>       assert "missing a required argument" in str(excinfo.value)
E       assert 'missing a required argument' in "Schema.dumps() missing 1 required positional argument: 'obj'"
E        +  where "Schema.dumps() missing 1 required positional argument: 'obj'" = str(TypeError("Schema.dumps() missing 1 required positional argument: 'obj'"))
E        +    where TypeError("Schema.dumps() missing 1 required positional argument: 'obj'") = <ExceptionInfo TypeError("Schema.dumps() missing 1 required positional argument: 'obj'") tblen=1>.value

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.py::TestSchemaDumps::test_invalid_input_missing_cls_arg[kwargs0]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_invalid_input_missing_cls_arg.py::TestSchemaDumps::test_invalid_input_missing_cls_arg[kwargs1]
============================== 2 failed in 0.05s ===============================
"""