
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale, ValueError

# Test initialization with specified locale only
def test_init_with_locale():
    text_data = Text(locale='en-US')
    assert hasattr(text_data, '_datafile'), "Attribute '_datafile' not found"
    assert hasattr(text_data, 'locale'), "Attribute 'locale' not found"
    assert text_data.locale == 'en-US', f"Expected locale to be 'en-US', but got {text_data.locale}"

# Test initialization with unsupported locale
def test_init_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='es_ES')

# Test generation of a single random sentence
def test_generate_single_sentence():
    text_data = Text(locale='en-US')
    sentence = text_data.sentence()
    assert isinstance(sentence, str), "Expected a string but got something else"
    assert len(sentence) > 0, "Generated sentence is empty"

# Test generation of multiple random sentences
def test_generate_multiple_sentences():
    text_data = Text(locale='en-US')
    text_content = text_data.text(quantity=3)
    assert isinstance(text_content, str), "Expected a string but got something else"
    sentences = text_content.split('. ')
    assert len(sentences) == 3, f"Expected 3 sentences but got {len(sentences)}"

# Test generation of text with default quantity (5 sentences)
def test_generate_default_quantity():
    text_data = Text(locale='en-US')
    text_content = text_data.text()
    assert isinstance(text_content, str), "Expected a string but got something else"
    sentences = text_content.split('. ')
    assert len(sentences) == 5, f"Expected 5 sentences but got {len(sentences)}"

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
_______ ERROR collecting test_mimesis_providers_text_Text_sentence_1.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_1.py:4: in <module>
    from mimesis.exceptions import UnsupportedLocale, ValueError
E   ImportError: cannot import name 'ValueError' from 'mimesis.exceptions' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/exceptions.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""