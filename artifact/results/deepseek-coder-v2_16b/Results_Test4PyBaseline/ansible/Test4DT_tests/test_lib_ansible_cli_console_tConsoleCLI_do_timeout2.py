
import pytest
from unittest.mock import patch
from io import StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

# Test case for valid positive integer timeout
def test_timeout_valid_positive_integer(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_timeout('300')
        assert console.task_timeout == 300
        assert str(fake_output.getvalue().strip()) == ''

# Test case for zero timeout
def test_timeout_zero(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_timeout('0')
        assert console.task_timeout == 0
        assert str(fake_output.getvalue().strip()) == ''

# Test case for invalid timeout argument (negative number)
def test_timeout_invalid_argument(console):
    with patch('sys.stdout', new=StringIO()) as fake_output:
        console.do_timeout('-5')
        assert console.task_timeout is None
        expected_error_message = 'The timeout must be greater than or equal to 1, use 0 to disable'