
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale, TypeError

# Test initialization with a specific locale
def test_init_with_locale():
    text = Text(locale='en-US')
    assert hasattr(text, '_datafile'), "Expected _datafile attribute to be set"
    assert text._datafile == 'text.json', "_datafile should be 'text.json'"

# Test initialization with a specific locale and seed
def test_init_with_locale_and_seed():
    text = Text(locale='es-ES', seed=42)
    assert hasattr(text, '_datafile'), "Expected _datafile attribute to be set"
    assert text._datafile == 'text.json', "_datafile should be 'text.json'"
    assert hasattr(text, 'seed') and text.seed == 42, "Expected seed to be set correctly"

# Test initialization without specifying locale or seed (should raise TypeError)
def test_init_without_parameters():
    with pytest.raises(TypeError):
        Text()

# Test getting a random quote
@pytest.mark.parametrize("locale", ['en-US', 'es-ES'])
def test_quote(locale):
    text = Text(locale=locale)
    quote = text.quote()
    assert isinstance(quote, str), "Expected quote to be a string"
    assert len(quote) > 0, "Expected non-empty quote"

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
_________ ERROR collecting test_mimesis_providers_text_Text_quote_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_quote_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_quote_0.py:4: in <module>
    from mimesis.exceptions import UnsupportedLocale, TypeError
E   ImportError: cannot import name 'TypeError' from 'mimesis.exceptions' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/exceptions.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_quote_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""