
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale, TypeError

# Test initialization with specified locale and seed
def test_init_with_locale_and_seed():
    text = Text(locale='en-US', seed=12345)
    assert isinstance(text, Text), "Instance should be of type Text"
    assert text._datafile == 'text.json', "_datafile attribute should be set to 'text.json'"
    assert text._seed == 12345, "_seed attribute should be set to the provided seed"

# Test initialization with specified locale only
def test_init_with_locale():
    text = Text(locale='en-US')
    assert isinstance(text, Text), "Instance should be of type Text"
    assert text._datafile == 'text.json', "_datafile attribute should be set to 'text.json'"
    assert text._seed is None, "_seed attribute should not be provided"

# Test initialization with specified seed only
def test_init_with_seed():
    text = Text(seed=12345)
    assert isinstance(text, Text), "Instance should be of type Text"
    assert text._datafile == 'text.json', "_datafile attribute should be set to 'text.json'"
    assert text._locale is None, "_locale attribute should not be provided"

# Test initialization with unsupported locale
def test_init_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale="es_ES")

# Test getting alphabet in uppercase (default)
def test_alphabet_uppercase():
    text = Text(locale='en-US')
    alpha = text.alphabet()
    assert isinstance(alpha, list), "Alphabet should be a list"
    assert all(isinstance(char, str) and len(char) == 1 for char in alpha), "Each item in the alphabet should be a single character string"

# Test getting alphabet in lowercase
def test_alphabet_lowercase():
    text = Text(locale='en-US')
    alpha = text.alphabet(lower_case=True)
    assert isinstance(alpha, list), "Alphabet should be a list"
    assert all(isinstance(char, str) and len(char) == 1 for char in alpha), "Each item in the alphabet should be a single character string"
    assert all(char.islower() for char in alpha), "All characters in lowercase alphabet should be in lower case"

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
_______ ERROR collecting test_mimesis_providers_text_Text_alphabet_1.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_alphabet_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_alphabet_1.py:4: in <module>
    from mimesis.exceptions import UnsupportedLocale, TypeError
E   ImportError: cannot import name 'TypeError' from 'mimesis.exceptions' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/exceptions.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_alphabet_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.21s ===============================
"""