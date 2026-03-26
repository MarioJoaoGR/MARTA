
# Module: Test4DT_tests.test_isort_literal_assignment_0
import ast
from isort.literal import assignment, DEFAULT_CONFIG, type_mapping, LiteralParsingFailure, LiteralSortTypeMismatch, ISortPrettyPrinter, _Config

def test_assignment_sorts_assignments():
    code = "b = 2\na = 1\nc = 3"
    sorted_code = assignment(code, sort_type="assignments", extension="")
    assert sorted_code == 'a = 1\nb = 2\nc = 3'

def test_assignment_sorts_with_specific_extension():
    code = "b = 2\na = 1\nc = 3"
    sorted_code = assignment(code, sort_type="assignments", extension=".py")
    assert sorted_code == 'a = 1\nb = 2\nc = 3'

def test_assignment_with_custom_configuration():
    code = "b = 2\na = 1\nc = 3"
    config = _Config(py_version='3', line_length=80)
    sorted_code = assignment(code, sort_type="assignments", extension="", config=config)
    assert sorted_code == 'a = 1\nb = 2\nc = 3'

def test_assignment_handles_undefined_sort_type():
    code = "b = 2\na = 1\nc = 3"
    try:
        sorted_code = assignment(code, sort_type="undefined", extension="")
    except ValueError as e:
        assert str(e) == 'Trying to sort using an undefined sort_type. Defined sort types are ...'

def test_assignment_parses_and_sorts_literal():
    code = "value = [3, 1, 4]"
    sorted_code = assignment(code, sort_type="list", extension="")
    assert sorted_code == 'value = [1, 3, 4]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_assignment_0
isort/Test4DT_tests/test_isort_literal_assignment_0.py:4:0: E0611: No name '_Config' in module 'isort.literal' (no-name-in-module)


"""