
import pytest
from ansible.modules.systemd import parse_systemctl_show

# Test scenario 1: Valid input
def test_valid_input():
    lines = [
        "Unit=foo.service",
        "Description={long description}",
        "ExecStart=/bin/bar",
        "ExecStop=/bin/stop"
    ]
    expected_output = {
        'Unit': 'foo.service',
        'Description': 'long description',
        'ExecStart': '/bin/bar',
        'ExecStop': '/bin/stop'
    }
    assert parse_systemctl_show(lines) == expected_output

# Test scenario 2: None input
def test_none_input():
    lines = None
    with pytest.raises(TypeError):
        parse_systemctl_show(lines)

# Test scenario 3: Empty list
def test_empty_list():
    lines = []
    expected_output = {}
    assert parse_systemctl_show(lines) == expected_output

# Test scenario 4: Invalid input format
def test_invalid_input():
    lines = ['Invalid line']
    with pytest.raises(IndexError):
        parse_systemctl_show(lines)
