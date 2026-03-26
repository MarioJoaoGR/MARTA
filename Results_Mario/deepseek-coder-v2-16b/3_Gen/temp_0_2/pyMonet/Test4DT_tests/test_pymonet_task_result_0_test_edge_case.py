
import pytest
from unittest.mock import Mock

def reject_example(arg):
    return 'Rejected: ' + str(arg)

def resolve_example(arg):
    return 'Resolved: ' + str(arg)

fn = lambda x: x * 2

def result(reject, resolve):
    return lambda arg: reject(arg) if arg is None or arg == '' else resolve(fn(arg))

# Test cases for edge cases
@pytest.mark.parametrize("input_value, expected", [
    (None, 'Rejected: None'),
    ('', 'Rejected: '),
    (0, 'Resolved: 0'),
    (1, 'Resolved: 2'),
    (-1, 'Resolved: -2')
])
def test_edge_case(input_value, expected):
    reject = Mock(side_effect=reject_example)
    resolve = Mock(side_effect=resolve_example)
    
    forked_result = result(reject, resolve)
    assert forked_result(input_value) == expected
