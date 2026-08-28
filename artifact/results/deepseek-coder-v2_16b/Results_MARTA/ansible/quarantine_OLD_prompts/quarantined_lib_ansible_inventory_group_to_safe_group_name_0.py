
import pytest
from unittest.mock import patch
from ansible.inventory.group import C

def to_safe_group_name(name, replacer="_", force=False, silent=False):
    warn = ''
    if name:  # when deserializing we might not have name yet
        invalid_chars = C.INVALID_VARIABLE_NAMES.findall(name)
        if invalid_chars:
            msg = 'invalid character(s) "%s" in group name (%s)' % (to_text(set(invalid_chars)), to_text(name))
            if C.TRANSFORM_INVALID_GROUP_CHARS not in ('never', 'ignore') or force:
                name = C.INVALID_VARIABLE_NAMES.sub(replacer, name)
                if not (silent or C.TRANSFORM_INVALID_GROUP_CHARS == 'silently'):
                    display.vvvv('Replacing ' + msg)
                    warn = 'Invalid characters were found in group names and automatically replaced, use -vvvv to see details'
            else:
                if C.TRANSFORM_INVALID_GROUP_CHARS == 'never':
                    display.vvvv('Not replacing %s' % msg)
                    warn = 'Invalid characters were found in group names but not replaced, use -vvvv to see details'

    if warn:
        display.warning(warn)

    return name

@pytest.mark.parametrize("name, expected", [
    ("my-group_name", "my_group_name"),
    ("my-group!name", "my_group_!name"),
    ("my-group!name", "my_group_!name", True),
    ("my-group!name", "my_group_!name", True, True)
])
def test_to_safe_group_name(name, expected, force=False, silent=False):
    with patch('ansible.inventory.group.C.INVALID_VARIABLE_NAMES', lambda: set(['!'])):
        result = to_safe_group_name(name, replacer="_", force=force, silent=silent)
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_lib_ansible_inventory_group_to_safe_group_name_0.py ___
test_lib_ansible_inventory_group_to_safe_group_name_0.py::test_to_safe_group_name: in "parametrize" the number of names (2):
  ['name', 'expected']
must be equal to the number of values (3):
  ('my-group!name', 'my_group_!name', True)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.51s ===============================
"""