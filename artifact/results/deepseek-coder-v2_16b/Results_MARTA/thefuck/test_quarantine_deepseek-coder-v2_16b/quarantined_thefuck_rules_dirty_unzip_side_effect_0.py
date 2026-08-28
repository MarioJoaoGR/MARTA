
import pytest
import zipfile
import os
from thefuck.rules.dirty_unzip import side_effect, _zip_file



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        old_cmd = {'script_parts': ['unzip', 'example.zip']}
        command = {'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}
    
        with pytest.raises(FileNotFoundError):
>           side_effect(old_cmd, command)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:46: in side_effect
    with zipfile.ZipFile(_zip_file(old_cmd), 'r') as archive:
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
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with pytest.raises(TypeError):
>           side_effect(None, None)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:46: in side_effect
    with zipfile.ZipFile(_zip_file(old_cmd), 'r') as archive:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = None

    def _zip_file(command):
        # unzip works that way:
        # unzip [-flags] file[.zip] [file(s) ...] [-x file(s) ...]
        #                ^          ^ files to unzip from the archive
        #                archive to unzip
>       for c in command.script_parts[1:]:
E       AttributeError: 'NoneType' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:20: AttributeError
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        old_cmd = {'script_parts': ['unzip', 'nonexistent.zip']}
        command = {'script_parts': ['unzip', '-r', 'archive.zip', '/path/to/extract']}
    
        with pytest.raises(FileNotFoundError):
>           side_effect(old_cmd, command)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/dirty_unzip.py:46: in side_effect
    with zipfile.ZipFile(_zip_file(old_cmd), 'r') as archive:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', 'nonexistent.zip']}

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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_side_effect_0.py::test_error_handling
========================= 3 failed, 1 warning in 0.16s =========================
"""