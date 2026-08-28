
import pytest
from ansible.template.native_helpers import StrictUndefined
from collections.abc import Mapping, Sequence

def is_sequence(data):
    return isinstance(data, Sequence)

def _fail_on_undefined(data):
    """Recursively find an undefined value in a nested data structure
    and properly raise the undefined exception.
    """
    if isinstance(data, Mapping):
        for value in data.values():
            _fail_on_undefined(value)
    elif is_sequence(data):
        for item in data:
            _fail_on_undefined(item)
    else:
        if isinstance(data, StrictUndefined):
            # To actually raise the undefined exception we need to
            # access the undefined object otherwise the exception would
            # be raised on the next access which might not be properly
            # handled.
            # See https://github.com/ansible/ansible/issues/52158
            # and StrictUndefined implementation in upstream Jinja2.
            str(data)

    return data


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers__fail_on_undefined_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_undefined_in_nested_structure ______________________

    def test_undefined_in_nested_structure():
        nested_data = {'dict1': {'key1': 1, 'key2': StrictUndefined()}, 'list1': [0, 1, 2, StrictUndefined()]}
>       with pytest.raises(StrictUndefined):
E       TypeError: expected exception must be a BaseException type, not StrictUndefined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers__fail_on_undefined_1.py:33: TypeError
______________________ test_undefined_in_mixed_structure _______________________

    def test_undefined_in_mixed_structure():
        mixed_data = {'int': 42, 'dict': {'innerKey': StrictUndefined()}, 'list': [1, 2, None, StrictUndefined()]}
>       with pytest.raises(StrictUndefined):
E       TypeError: expected exception must be a BaseException type, not StrictUndefined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers__fail_on_undefined_1.py:38: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers__fail_on_undefined_1.py::test_undefined_in_nested_structure
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_native_helpers__fail_on_undefined_1.py::test_undefined_in_mixed_structure
============================== 2 failed in 0.59s ===============================
"""