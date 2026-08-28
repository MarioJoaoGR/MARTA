
# Module: ansible.parsing.mod_args
# test_module_args_parser.py
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.parsing.mod_args import ModuleArgsParser
import pytest
from unittest.mock import patch

def test_normalize_parameters_none():
    parser = ModuleArgsParser()
    action, args = parser._normalize_parameters('copy', 'copy')
    assert action == 'copy'