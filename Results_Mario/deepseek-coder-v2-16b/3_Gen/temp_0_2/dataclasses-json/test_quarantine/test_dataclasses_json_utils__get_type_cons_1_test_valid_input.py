
import pytest
from dataclasses_json.utils import _get_type_cons
from typing import List, Union

# Mocking the version info for testing purposes
@pytest.fixture(params=[3, 6], ids=["Python 3.x", "Python 3.6"])
def mock_version_info(request):
    class MockVersionInfo:
        minor = request.param

    return MockVersionInfo()

# Test function using the mocked version info
def test_get_type_cons(mock_version_info):
    # Test for Python 3.x where __origin__ is available but not always defined
    cons = _get_type_cons(List[int])
    assert cons == list

    # Test for Python 3.6 specifically, where __extra__ should be used if __origin__ is not available
    class MockType:
        def __init__(self, extra=None, origin=None):
            self.__extra__ = extra
            self.__origin__ = origin

    # Test when __origin__ is available but __extra__ is not
    type_obj = MockType(origin=list)
    assert _get_type_cons(type_obj) == list

    # Test when neither __origin__ nor __extra__ are available, should return the type itself
    type_obj = MockType()
    assert _get_type_cons(type_obj) == type_obj

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_1_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_get_type_cons[Python 3.x] ________________________

mock_version_info = <Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.mock_version_info.<locals>.MockVersionInfo object at 0x105cbd3c0>

    def test_get_type_cons(mock_version_info):
        # Test for Python 3.x where __origin__ is available but not always defined
        cons = _get_type_cons(List[int])
        assert cons == list
    
        # Test for Python 3.6 specifically, where __extra__ should be used if __origin__ is not available
        class MockType:
            def __init__(self, extra=None, origin=None):
                self.__extra__ = extra
                self.__origin__ = origin
    
        # Test when __origin__ is available but __extra__ is not
        type_obj = MockType(origin=list)
        assert _get_type_cons(type_obj) == list
    
        # Test when neither __origin__ nor __extra__ are available, should return the type itself
        type_obj = MockType()
>       assert _get_type_cons(type_obj) == type_obj
E       assert None == <Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.test_get_type_cons.<locals>.MockType object at 0x105cbd330>
E        +  where None = _get_type_cons(<Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.test_get_type_cons.<locals>.MockType object at 0x105cbd330>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_1_test_valid_input.py:32: AssertionError
________________________ test_get_type_cons[Python 3.6] ________________________

mock_version_info = <Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.mock_version_info.<locals>.MockVersionInfo object at 0x105cbf4f0>

    def test_get_type_cons(mock_version_info):
        # Test for Python 3.x where __origin__ is available but not always defined
        cons = _get_type_cons(List[int])
        assert cons == list
    
        # Test for Python 3.6 specifically, where __extra__ should be used if __origin__ is not available
        class MockType:
            def __init__(self, extra=None, origin=None):
                self.__extra__ = extra
                self.__origin__ = origin
    
        # Test when __origin__ is available but __extra__ is not
        type_obj = MockType(origin=list)
        assert _get_type_cons(type_obj) == list
    
        # Test when neither __origin__ nor __extra__ are available, should return the type itself
        type_obj = MockType()
>       assert _get_type_cons(type_obj) == type_obj
E       assert None == <Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.test_get_type_cons.<locals>.MockType object at 0x105cbfdf0>
E        +  where None = _get_type_cons(<Test4DT_tests.test_dataclasses_json_utils__get_type_cons_1_test_valid_input.test_get_type_cons.<locals>.MockType object at 0x105cbfdf0>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_1_test_valid_input.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_1_test_valid_input.py::test_get_type_cons[Python 3.x]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_1_test_valid_input.py::test_get_type_cons[Python 3.6]
============================== 2 failed in 0.04s ===============================
"""