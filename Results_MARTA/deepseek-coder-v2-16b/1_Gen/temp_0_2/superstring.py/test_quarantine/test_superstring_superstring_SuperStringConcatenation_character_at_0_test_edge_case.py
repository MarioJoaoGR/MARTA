
import pytest
from superstring.superstring import SuperStringBase, SuperStringConcatenation

@pytest.fixture
def setup_concat():
    left_str = SuperStringBase("Hello")
    right_str = SuperStringBase("World")
    return SuperStringConcatenation(left_str, right_str)

def test_character_at_index_0(setup_concat):
    assert setup_concat.character_at(0) == 'H'

def test_character_at_index_beyond_left_length(setup_concat):
    with pytest.raises(IndexError):
        setup_concat.character_at(5)

def test_character_at_index_within_right_bounds(setup_concat):
    assert setup_concat.character_at(5) == 'W'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test_character_at_index_0 __________________

    @pytest.fixture
    def setup_concat():
>       left_str = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py:7: TypeError
_________ ERROR at setup of test_character_at_index_beyond_left_length _________

    @pytest.fixture
    def setup_concat():
>       left_str = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py:7: TypeError
________ ERROR at setup of test_character_at_index_within_right_bounds _________

    @pytest.fixture
    def setup_concat():
>       left_str = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py::test_character_at_index_0
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py::test_character_at_index_beyond_left_length
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py::test_character_at_index_within_right_bounds
============================== 3 errors in 0.05s ===============================
"""