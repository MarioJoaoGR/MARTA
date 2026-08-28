
import pytest
from ansible.modules.systemd import parse_systemctl_show

# Test case 1: Single-line values only
def test_parse_systemctl_show_single_lines():
    lines = [
        "Description=This is a single line",
        "ExecStart=This is another single line command"
    ]
    expected_output = {
        'Description': 'This is a single line',
        'ExecStart': 'This is another single line command'
    }
    assert parse_systemctl_show(lines) == expected_output

# Test case 2: Multi-line values
def test_parse_systemctl_show_multi_lines():
    lines = [
        "Description={This is a multi-line description}",
        "ExecStart={This is the start command}",
        "AnotherKey=SingleLineValue"
    ]
    expected_output = {
        'Description': 'This is a multi-line description',
        'ExecStart': 'This is the start command',
        'AnotherKey': 'SingleLineValue'
    }