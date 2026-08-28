
import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro

@pytest.mark.parametrize("platform_info, expected", [
    ({'platform_dist_result': ['Ubuntu', '18.04']}, ('Ubuntu', '18.04')),
    ({'osrelease_content': 'ID=Debian\nVERSION_ID="9"'}, ('Debian', '9')),
    ({}, ('', '')),
])
def test_get_linux_distro(platform_info, expected):
    result = _get_linux_distro(platform_info)
    assert result == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery__get_linux_distro_0.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
_______________ test_get_linux_distro[platform_info0-expected0] ________________

platform_info = {'platform_dist_result': ['Ubuntu', '18.04']}
expected = ('Ubuntu', '18.04')

    @pytest.mark.parametrize("platform_info, expected", [
        ({'platform_dist_result': ['Ubuntu', '18.04']}, ('Ubuntu', '18.04')),
        ({'osrelease_content': 'ID=Debian\nVERSION_ID="9"'}, ('Debian', '9')),
        ({}, ('', '')),
    ])
    def test_get_linux_distro(platform_info, expected):
        result = _get_linux_distro(platform_info)
>       assert result == expected
E       AssertionError: assert ('', '') == ('Ubuntu', '18.04')
E         
E         At index 0 diff: '' != 'Ubuntu'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery__get_linux_distro_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery__get_linux_distro_0.py::test_get_linux_distro[platform_info0-expected0]
========================= 1 failed, 2 passed in 0.30s ==========================
"""