
import pytest
from your_module import append_param  # Replace 'your_module' with the actual module name where append_param is defined

@pytest.fixture
def rule():
    return []

def test_valid_case_single_param(rule):
    append_param(rule, 'example', 'F', False)
    assert rule == ['F', 'example']

def test_valid_case_multiple_params(rule):
    append_param(rule, ['!negated', 'normal'], 'P', True)
    assert rule == ['P', '!negated', 'P', 'normal']

def test_error_case_invalid_input():
    with pytest.raises(ValueError):
        rule = []
        append_param(rule, 123, 'F', False)
