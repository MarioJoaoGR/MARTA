
import pytest
from unittest.mock import patch
from mimesis.providers.person import PersonProvider

# Test 1: Instantiate Person with locale and seed
def test_instantiate_person():
    person = PersonProvider(locale='en', seed=42)
    assert hasattr(person, 'surname'), "Person instance should have a surname method"

# Test 2: Generate random surname without specifying gender
def test_generate_random_surname():
    with patch('mimesis.providers.person.PersonProvider._pull') as mock_pull:
        mock_pull.return_value = {'surnames': ['Smith', 'Johnson']}
        person = PersonProvider(locale='en', seed=42)
        surname = person.surname()
        assert surname in ['Smith', 'Johnson'], "Surname should be randomly chosen from available surnames"

# Test 3: Generate random surname specifying gender
def test_generate_surname_by_gender():
    with patch('mimesis.providers.person.PersonProvider._pull') as mock_pull:
        mock_pull.return_value = {'surnames': {'male': ['Smith'], 'female': ['Johnson']}}
        person = PersonProvider(locale='en', seed=42)
        surname_male = person.surname(gender='male')
        surname_female = person.surname(gender='female')
        assert surname_male == 'Smith', "Surname should be chosen from male list"
        assert surname_female == 'Johnson', "Surname should be chosen from female list"

# Test 4: Raise error for unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = PersonProvider(locale='xx', seed=42)

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
______ ERROR collecting test_mimesis_providers_person_Person_surname_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_surname_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_surname_0.py:4: in <module>
    from mimesis.providers.person import PersonProvider
E   ImportError: cannot import name 'PersonProvider' from 'mimesis.providers.person' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_surname_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""