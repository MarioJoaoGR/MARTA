
from isort._vendored.tomli._parser import coord_repr

def test_valid_input():
    assert coord_repr("hello\nworld", 5) == "line 2, column 1"
    assert coord_repr("hello\nworld", 6) == "line 2, column 2"
    assert coord_repr("hello\nworld", 7) == "line 2, column 3"
    assert coord_repr("hello\nworld", 100) == "end of document"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_coord_repr_2_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_coord_repr_2_test_valid_input.py:2:0: E0611: No name 'coord_repr' in module 'isort._vendored.tomli._parser' (no-name-in-module)


"""