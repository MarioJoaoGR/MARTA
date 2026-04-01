
import pytest
from dataclasses_json.undefined import _CatchAllUndefinedParameters, Field

def test_get_default():
    class _SentinelNoDefault:
        pass

    class _CatchAllUndefinedParameters:
        _SentinelNoDefault = _SentinelNoDefault

    catch_all_field = Field(default=_CatchAllUndefinedParameters._SentinelNoDefault)
    
    # Test when there is a default value
    assert _get_default(catch_all_field) == _CatchAllUndefinedParameters._SentinelNoDefault

    # Test when there is no default value but a default factory
    catch_all_field = Field(default_factory=lambda: _CatchAllUndefinedParameters._SentinelNoDefault)
    assert _get_default(catch_all_field) == _CatchAllUndefinedParameters._SentinelNoDefault

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'default_factory' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'init' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'repr' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'hash' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'compare' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'metadata' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:12:22: E1120: No value for argument 'kw_only' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:15:11: E0602: Undefined variable '_get_default' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'default' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'init' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'repr' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'hash' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'compare' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'metadata' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:18:22: E1120: No value for argument 'kw_only' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_default_0_test_edge_cases.py:19:11: E0602: Undefined variable '_get_default' (undefined-variable)


"""