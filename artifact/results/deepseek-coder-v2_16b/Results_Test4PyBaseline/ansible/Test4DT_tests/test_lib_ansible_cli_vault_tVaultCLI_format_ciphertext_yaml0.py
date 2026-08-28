# Module: ansible.cli.vault
import pytest
from ansible.cli.vault import VaultCLI

# Test cases for the format_ciphertext_yaml method in VaultCLI class
def test_format_ciphertext_yaml_default_indent():
    b_ciphertext = b'test_data'
    expected_output = """!vault |    test_data"""
    assert VaultCLI.format_ciphertext_yaml(b_ciphertext) == expected_output

def test_format_ciphertext_yaml_custom_indent():
    b_ciphertext = b'test_data'
    indent = 20
    expected_output = """!vault |                test_data"""
    assert VaultCLI.format_ciphertext_yaml(b_ciphertext, indent) == expected_output

def test_format_ciphertext_yaml_with_name():
    b_ciphertext = b'test_data'
    name = 'example_var'
    expected_output = """example_var: !vault |    test_data"""
    assert VaultCLI.format_ciphertext_yaml(b_ciphertext, name=name) == expected_output

def test_format_ciphertext_yaml_multiple_lines():
    b_ciphertext = b'line1\nline2'
    expected_output = """!vault |    line1
    line2"""
    assert VaultCLI.format_ciphertext_yaml(b_ciphertext) == expected_output
