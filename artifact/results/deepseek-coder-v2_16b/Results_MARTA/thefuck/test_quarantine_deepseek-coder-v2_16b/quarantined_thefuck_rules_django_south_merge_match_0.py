
import pytest
from thefuck.rules.django_south_merge import match



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_with_merge __________________________

    def test_valid_case_with_merge():
        command = {'script': 'manage.py migrate --merge', 'output': 'Migration completed successfully'}
>       assert match(command) is True

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'output': 'Migration completed successfully', 'script': 'manage.py migrate --merge'}

    def match(command):
>       return 'manage.py' in command.script and \
               'migrate' in command.script \
               and '--merge: will just attempt the migration' in command.output
E       AttributeError: 'dict' object has no attribute 'script'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/django_south_merge.py:2: AttributeError
_______________________ test_invalid_case_without_merge ________________________

    def test_invalid_case_without_merge():
        command = {'script': 'manage.py migrate', 'output': 'Migration completed successfully'}
>       assert match(command) is False

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'output': 'Migration completed successfully', 'script': 'manage.py migrate'}

    def match(command):
>       return 'manage.py' in command.script and \
               'migrate' in command.script \
               and '--merge: will just attempt the migration' in command.output
E       AttributeError: 'dict' object has no attribute 'script'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/django_south_merge.py:2: AttributeError
______________________ test_error_case_with_fake_initial _______________________

    def test_error_case_with_fake_initial():
        command = {'script': 'manage.py migrate --fake-initial', 'output': 'Migration completed successfully'}
>       assert match(command) is False

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'output': 'Migration completed successfully', 'script': 'manage.py migrate --fake-initial'}

    def match(command):
>       return 'manage.py' in command.script and \
               'migrate' in command.script \
               and '--merge: will just attempt the migration' in command.output
E       AttributeError: 'dict' object has no attribute 'script'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/django_south_merge.py:2: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py::test_valid_case_with_merge
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py::test_invalid_case_without_merge
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_django_south_merge_match_0.py::test_error_case_with_fake_initial
============================== 3 failed in 0.06s ===============================
"""