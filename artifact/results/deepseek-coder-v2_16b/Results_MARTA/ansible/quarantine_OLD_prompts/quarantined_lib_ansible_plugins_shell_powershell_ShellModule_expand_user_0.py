
import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def setup_shell_module():
    return ShellModule()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py F [100%]

=================================== FAILURES ===================================
______________________ test_ShellModule_expand_user_basic ______________________

setup_shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f0319d993f0>

    def test_ShellModule_expand_user_basic(setup_shell_module):
        with patch('ansible.plugins.shell.powershell.os.path') as mock_os_path:
            mock_os_path.expanduser.return_value = 'C:\\Users\\username\\Documents\\Report.txt'
    
>           result = setup_shell_module.expand_user('~\Documents\Report.txt')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:146: in expand_user
    return self._encode_script(script)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:282: in _encode_script
    encoded_script = to_text(base64.b64encode(script.encode('utf-16-le')), 'utf-8')
/opt/conda/envs/test4py_env/lib/python3.10/encodings/__init__.py:99: in search_function
    mod = __import__('encodings.' + modname, fromlist=_import_tail,
<frozen importlib._bootstrap>:1027: in _find_and_load
    ???
<frozen importlib._bootstrap>:1002: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:945: in _find_spec
    ???
/data/pydeps/marta/_pytest/assertion/rewrite.py:119: in find_spec
    if not self._should_rewrite(name, fn, state):
/data/pydeps/marta/_pytest/assertion/rewrite.py:230: in _should_rewrite
    if fnmatch_ex(pat, fn_path):
/data/pydeps/marta/_pytest/pathlib.py:447: in fnmatch_ex
    return fnmatch.fnmatch(name, pattern)
/opt/conda/envs/test4py_env/lib/python3.10/fnmatch.py:42: in fnmatch
    return fnmatchcase(name, pat)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = <MagicMock name='path.normcase()' id='139651294741744'>
pat = <MagicMock name='path.normcase()' id='139651294741744'>

    def fnmatchcase(name, pat):
        """Test whether FILENAME matches PATTERN, including case.
    
        This is a version of fnmatch() which doesn't case-normalize
        its arguments.
        """
        match = _compile_pattern(pat)
>       return match(name) is not None
E       TypeError: expected string or bytes-like object

/opt/conda/envs/test4py_env/lib/python3.10/fnmatch.py:77: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:14
  /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:14: DeprecationWarning: invalid escape sequence '\D'
    result = setup_shell_module.expand_user('~\Documents\Report.txt')

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py::test_ShellModule_expand_user_basic
========================= 1 failed, 1 warning in 0.46s =========================
"""