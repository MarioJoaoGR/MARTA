
import pytest
from mimesis.providers.person import PersonProvider

@pytest.fixture(scope="module")
def person_provider():
    return PersonProvider()

def test_surname_default(person_provider):
    surname = person_provider.surname()
    assert isinstance(surname, str)

def test_surname_with_gender(person_provider):
    surname_male = person_provider.surname(gender='male')
    surname_female = person_provider.surname(gender='female')
    assert isinstance(surname_male, str)
    assert isinstance(surname_female, str)

def test_surname_invalid_gender(person_provider):
    with pytest.raises(ValueError):
        person_provider.surname(gender='unknown')

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
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_surname_0.py:3: in <module>
    from mimesis.providers.person import PersonProvider
E   ImportError: cannot import name 'PersonProvider' from 'mimesis.providers.person' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_surname_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.24s ===============================
"""