
# Module: isort._vendored.tomli._parser
import pytest
from isort._vendored.tomli._parser import key_value_rule
from isort._vendored.tomli._shared_types import Output, Pos, Key, ParseFloat
from isort._vendored.tomli._exceptions import suffixed_err
from isort._vendored.tomli._flags import Flags

# Test cases for key_value_rule function
def test_key_value_rule_simple():
    src = 'name=John Doe'
    pos = 0
    out = Output()
    header = ('user',)
    parse_float = float
    
    new_pos = key_value_rule(src, pos, out, header, parse_float)
    assert new_pos == len('name=John Doe')
    assert 'user.name' in out.data
    assert out.data['user']['name'] == 'John Doe'

def test_key_value_rule_immutable_namespace():
    src = 'is_frozen=true'
    pos = 0
    out = Output()
    header = ('flags',)
    parse_float = float
    
    with pytest.raises(suffixed_err):
        key_value_rule(src, pos, out, header, parse_float)

def test_key_value_rule_overwrite():
    src = 'age=25'
    pos = 0
    out = Output()
    header = ('user',)
    parse_float = float
    
    key_value_rule(src, pos, out, header, parse_float)
    with pytest.raises(suffixed_err):
        key_value_rule(src, pos, out, header, parse_float)

def test_key_value_rule_recursive_immutable():
    src = 'details=[1, 2, 3]'
    pos = 0
    out = Output()
    header = ('user',)
    parse_float = float
    
    key_value_rule(src, pos, out, header, parse_float)
    assert 'user.details' in out.flags
    assert out.flags['user.details'] == Flags.FROZEN

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_key_value_rule_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:5:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:5:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:6:0: E0401: Unable to import 'isort._vendored.tomli._exceptions' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:6:0: E0611: No name '_exceptions' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:7:0: E0401: Unable to import 'isort._vendored.tomli._flags' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:7:0: E0611: No name '_flags' in module 'isort._vendored.tomli' (no-name-in-module)


"""