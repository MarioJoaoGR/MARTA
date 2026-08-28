
import pytest
from ansible.module_utils import basic
from FacterFactCollector import FacterFactCollector
import subprocess

# Test for valid input scenario
def test_valid_input():
    module = basic.AnsibleModule(argument_spec={})
    facter_path = '/usr/local/bin/facter'
    collector = FacterFactCollector()
    rc, out, err = collector.run_facter(module, facter_path)
    assert rc == 0, f"Expected return code 0 but got {rc}, output: {out}, error: {err}"
    assert out != "", "Expected non-empty output"
    assert err == "", "Expected no errors, but got: " + err

# Test for edge case scenario with empty string as facter_path
def test_edge_case():
    module = basic.AnsibleModule(argument_spec={})
    facter_path = ''
    collector = FacterFactCollector()
    rc, out, err = collector.run_facter(module, facter_path)
    assert rc != 0, "Expected non-zero return code for invalid path"
    assert out == "", "Expected empty output for invalid command"
    assert 'No such file or directory' in err, f"Expected error related to missing file but got: {err}"

# Test for invalid input scenario with non-existent facter_path
def test_invalid_input():
    module = basic.AnsibleModule(argument_spec={})
    facter_path = 'non_existent_path'
    collector = FacterFactCollector()
    rc, out, err = collector.run_facter(module, facter_path)
    assert rc != 0, "Expected non-zero return code for invalid path"
    assert out == "", "Expected empty output for invalid command"
    assert 'No such file or directory' in err, f"Expected error related to missing file but got: {err}"
