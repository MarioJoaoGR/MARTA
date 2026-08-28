
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_runas_options

@pytest.fixture(scope="module")
def parser():
    parser = argparse.ArgumentParser()
    add_runas_options(parser)
    return parser

# Scenario 1: test_valid_inputs
def test_valid_inputs(parser):
    args = parser.parse_args(["--become", "--become-method=sudo", "--become-user=root"])
    assert args.become is True
    assert args.become_method == "sudo"
    assert args.become_user == "root"

# Scenario 2: test_edge_cases
def test_edge_cases(parser):
    # Test with None values
    args = parser.parse_args(["--become", "--become-method=None", "--become-user="])
    assert args.become is True
    assert args.become_method is None
    assert args.become_user == ""
    
    # Test without any arguments
    args = parser.parse_args([])
    assert args.become is False
    assert args.become_method is None
    assert args.become_user is None

# Scenario 3: test_invalid_inputs
def test_invalid_inputs(parser):
    with pytest.raises(SystemExit) as e:
        parser.parse_args(["--become=invalid", "--become-method=sudo", "--become-user=root"])
    assert str(e.value) == "usage: script.py [-h] [--become] [--become-method BECOME_METHOD] [--become-user BECOME_USER]"
    
    with pytest.raises(SystemExit) as e:
        parser.parse_args(["--become=True", "--become-method=invalid", "--become-user=root"])
    assert str(e.value) == "usage: script.py [-h] [--become] [--become-method BECOME_METHOD] [--become-user BECOME_USER]"
    
    with pytest.raises(SystemExit) as e:
        parser.parse_args(["--become=True", "--become-method=sudo", "--become-user=invalid"])
    assert str(e.value) == "usage: script.py [-h] [--become] [--become-method BECOME_METHOD] [--become-user BECOME_USER]"
