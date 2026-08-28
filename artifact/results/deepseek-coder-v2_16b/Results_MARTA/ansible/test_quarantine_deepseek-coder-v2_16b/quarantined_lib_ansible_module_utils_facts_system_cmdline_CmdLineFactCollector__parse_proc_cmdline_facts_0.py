
import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        collector = CmdLineFactCollector()
        data = 'arg1=value1 arg2 arg3=value3'
        result = collector._parse_proc_cmdline_facts(data)
>       assert result == {'arg1': 'value1', 'arg2': True, 'arg3': ['value3']}
E       AssertionError: assert {'arg1': 'val...g3': 'value3'} == {'arg1': 'val...': ['value3']}
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'arg3': 'value3'} != {'arg3': ['value3']}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py:9: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        collector = CmdLineFactCollector()
        data = None
        with pytest.raises(TypeError):
>           collector._parse_proc_cmdline_facts(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/system/cmdline.py:50: in _parse_proc_cmdline_facts
    for piece in shlex.split(data, posix=False):
/opt/conda/envs/test4py_env/lib/python3.10/shlex.py:315: in split
    return list(lex)
/opt/conda/envs/test4py_env/lib/python3.10/shlex.py:300: in __next__
    token = self.get_token()
/opt/conda/envs/test4py_env/lib/python3.10/shlex.py:109: in get_token
    raw = self.read_token()
/opt/conda/envs/test4py_env/lib/python3.10/shlex.py:140: in read_token
    nextchar = self.instream.read(1)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7fdf76c75a50>, size = 1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/marta/_pytest/capture.py:208: OSError
=============================== warnings summary ===============================
test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py::test_none_input
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/system/cmdline.py:50: DeprecationWarning: Passing None for 's' to shlex.split() is deprecated.
    for piece in shlex.split(data, posix=False):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_0.py::test_none_input
========================= 2 failed, 1 warning in 0.38s =========================
"""