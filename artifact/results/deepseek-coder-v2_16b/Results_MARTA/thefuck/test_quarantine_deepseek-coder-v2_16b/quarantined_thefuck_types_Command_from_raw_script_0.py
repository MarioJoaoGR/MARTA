
import pytest
from thefuck.types import Command
from thefuck.exceptions import EmptyCommand

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_types_Command_from_raw_script_0.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        try:
>           cmd = Command.from_raw_script([''])

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_types_Command_from_raw_script_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'thefuck.types.Command'>, raw_script = ['']

    @classmethod
    def from_raw_script(cls, raw_script):
        """Creates instance of `Command` from a list of script parts.
    
        :type raw_script: [basestring]
        :rtype: Command
        :raises: EmptyCommand
    
        """
        script = format_raw_script(raw_script)
        if not script:
>           raise EmptyCommand
E           thefuck.exceptions.EmptyCommand

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:79: EmptyCommand

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        try:
            cmd = Command.from_raw_script([''])
        except EmptyCommand as e:
>           assert str(e) == "Empty command"
E           AssertionError: assert '' == 'Empty command'
E             
E             - Empty command

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_types_Command_from_raw_script_0.py:10: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_types_Command_from_raw_script_0.py::test_invalid_input
========================= 1 failed, 1 warning in 0.24s =========================
"""