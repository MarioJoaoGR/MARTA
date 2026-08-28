
import pytest
from thefuck.rules.dirty_unzip import _zip_file

@pytest.mark.parametrize("command, expected", [
    ({'script_parts': ['unzip', 'example.zip']}, 'example.zip'),
    ({'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}, 'archive.zip'),
    ({'script_parts': ['unzip', '-l', 'example']}, 'example.zip')
])
def test_zip_file(command, expected):
    assert _zip_file(command) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_zip_file[command0-example.zip] ______________________

command = {'script_parts': ['unzip', 'example.zip']}, expected = 'example.zip'

    @pytest.mark.parametrize("command, expected", [
        ({'script_parts': ['unzip', 'example.zip']}, 'example.zip'),
        ({'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}, 'archive.zip'),
        ({'script_parts': ['unzip', '-l', 'example']}, 'example.zip')
    ])
    def test_zip_file(command, expected):
>       assert _zip_file(command) == expected

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', 'example.zip']}

    def _zip_file(command):
        # unzip works that way:
        # unzip [-flags] file[.zip] [file(s) ...] [-x file(s) ...]
        #                ^          ^ files to unzip from the archive
        #                archive to unzip
>       for c in command.script_parts[1:]:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:20: AttributeError
_____________________ test_zip_file[command1-archive.zip] ______________________

command = {'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}
expected = 'archive.zip'

    @pytest.mark.parametrize("command, expected", [
        ({'script_parts': ['unzip', 'example.zip']}, 'example.zip'),
        ({'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}, 'archive.zip'),
        ({'script_parts': ['unzip', '-l', 'example']}, 'example.zip')
    ])
    def test_zip_file(command, expected):
>       assert _zip_file(command) == expected

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}

    def _zip_file(command):
        # unzip works that way:
        # unzip [-flags] file[.zip] [file(s) ...] [-x file(s) ...]
        #                ^          ^ files to unzip from the archive
        #                archive to unzip
>       for c in command.script_parts[1:]:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:20: AttributeError
_____________________ test_zip_file[command2-example.zip] ______________________

command = {'script_parts': ['unzip', '-l', 'example']}, expected = 'example.zip'

    @pytest.mark.parametrize("command, expected", [
        ({'script_parts': ['unzip', 'example.zip']}, 'example.zip'),
        ({'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}, 'archive.zip'),
        ({'script_parts': ['unzip', '-l', 'example']}, 'example.zip')
    ])
    def test_zip_file(command, expected):
>       assert _zip_file(command) == expected

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', '-l', 'example']}

    def _zip_file(command):
        # unzip works that way:
        # unzip [-flags] file[.zip] [file(s) ...] [-x file(s) ...]
        #                ^          ^ files to unzip from the archive
        #                archive to unzip
>       for c in command.script_parts[1:]:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:20: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py::test_zip_file[command0-example.zip]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py::test_zip_file[command1-archive.zip]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip__zip_file_0.py::test_zip_file[command2-example.zip]
========================= 3 failed, 1 warning in 0.17s =========================
"""