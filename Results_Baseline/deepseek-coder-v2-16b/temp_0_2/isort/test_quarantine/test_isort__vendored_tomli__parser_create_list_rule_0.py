
# Module: isort._vendored.tomli._parser
import pytest
from isort._vendored.tomli._parser import create_list_rule
from typing import Tuple, List, Any

# Assuming Output and Flags are defined elsewhere in the module or imported from another module
class OutputMock:
    def __init__(self):
        self.flags = Flags()
        self.data = []

def test_create_list_rule_basic():
    src = "[[example]]\nkey = 'value'"
    pos = 0
    out = OutputMock()
    new_pos, key = create_list_rule(src, pos, out)
    assert key == ('example', 'key')
    assert new_pos == len(src)

def test_create_list_rule_immutable_key():
    src = "[[example]]\nkey = 'value'"
    pos = 0
    out = OutputMock()
    out.flags.set('key', Flags.FROZEN)
    with pytest.raises(suffixed_err, match="Can not mutate immutable namespace key"):
        create_list_rule(src, pos, out)

def test_create_list_rule_overwrite_value():
    src = "[[example]]\nkey = 'value'"
    pos = 0
    out = OutputMock()
    out.data = ['existing_value']
    with pytest.raises(suffixed_err, match="Can not overwrite a value"):
        create_list_rule(src, pos, out)

def test_create_list_rule_nested_structure():
    src = "[[example]]\nkey1 = 'value1'\n[[example.nested]]\nkey2 = 'value2'"
    pos = 0
    out = OutputMock()
    new_pos, key = create_list_rule(src, pos, out)
    assert key == ('example', 'nested')
    assert new_pos == len(src)

def test_create_list_rule_missing_end():
    src = "[[example]]\nkey = 'value'"
    pos = 0
    out = OutputMock()
    with pytest.raises(suffixed_err, match='Expected "]]" at the end of an array declaration'):
        create_list_rule(src, pos, out)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_create_list_rule_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0.py:10:21: E0602: Undefined variable 'Flags' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0.py:25:25: E0602: Undefined variable 'Flags' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0.py:26:23: E0602: Undefined variable 'suffixed_err' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0.py:34:23: E0602: Undefined variable 'suffixed_err' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0.py:49:23: E0602: Undefined variable 'suffixed_err' (undefined-variable)


"""