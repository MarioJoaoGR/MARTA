
import pytest
from unittest.mock import patch
from mimesis.providers.person import PersonProvider

@pytest.fixture(scope="function")
def person():
    return PersonProvider()

def test_full_name_default(person):
    with patch('mimesis.providers.person.get_random_item', return_value='John'):
        name = person.name()
        surname = person.surname()
        full_name = person.full_name()
        assert isinstance(full_name, str)
        assert len(full_name.split()) == 2

def test_full_name_specific_gender(person):
    with patch('mimesis.providers.person.get_random_item', side_effect=['John', 'Doe']):
        full_name = person.full_name(gender='Male')
        assert isinstance(full_name, str)
        assert len(full_name.split()) == 2
        assert full_name.split()[0] == 'John'
        assert full_name.split()[1] == 'Doe'

def test_full_name_reverse_order(person):
    with patch('mimesis.providers.person.get_random_item', side_effect=['John', 'Doe']):
        full_name = person.full_name(reverse=True)
        assert isinstance(full_name, str)
        assert len(full_name.split()) == 2
        assert full_name.split()[0] == 'Doe'
        assert full_name.split()[1] == 'John'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_mimesis_providers_person_Person_full_name_2.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_full_name_2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_full_name_2.py:4: in <module>
    from mimesis.providers.person import PersonProvider
E   ImportError: cannot import name 'PersonProvider' from 'mimesis.providers.person' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_full_name_2.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""