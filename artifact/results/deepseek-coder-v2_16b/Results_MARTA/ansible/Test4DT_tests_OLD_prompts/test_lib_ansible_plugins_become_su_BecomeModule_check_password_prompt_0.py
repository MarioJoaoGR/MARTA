
import pytest
from unittest.mock import patch
from ansible.plugins.become.su import BecomeModule


def test_invalid_input():
    su_module = BecomeModule()
    with patch('ansible.plugins.become.su.BecomeModule.get_option', return_value=['Password']):
        b_output = b"Please enter the username:"
        result = su_module.check_password_prompt(b_output)
        assert result is False


def test_no_prompts():
    su_module = BecomeModule()
    with patch('ansible.plugins.become.su.BecomeModule.get_option', return_value=['Password']):
        b_output = b"This is a test without any password prompt."
        result = su_module.check_password_prompt(b_output)
        assert result is False