
import os
import pytest
from tornado import locale
from unittest.mock import patch

def load_gettext_translations(directory: str, domain: str) -> None:
    """Loads translations from `gettext`'s locale tree."""
    global _translations
    global _supported_locales
    global _use_gettext
    _translations = {}
    for lang in os.listdir(directory):
        if lang.startswith("."):
            continue  # skip .svn, etc
        if os.path.isfile(os.path.join(directory, lang)):
            continue
        try:
            os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
            _translations[lang] = gettext.translation(
                domain, directory, languages=[lang]
            )
        except Exception as e:
            gen_log.error("Cannot load translation for '%s': %s", lang, str(e))
            continue
    _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
    _use_gettext = True
    gen_log.debug("Supported locales: %s", sorted(_supported_locales))



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

directory = '/tmp/en/LC_MESSAGES', domain = 'mydomain'

    def load_gettext_translations(directory: str, domain: str) -> None:
        """Loads translations from `gettext`'s locale tree."""
        global _translations
        global _supported_locales
        global _use_gettext
        _translations = {}
        for lang in os.listdir(directory):
            if lang.startswith("."):
                continue  # skip .svn, etc
            if os.path.isfile(os.path.join(directory, lang)):
                continue
            try:
                os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
>               _translations[lang] = gettext.translation(
                    domain, directory, languages=[lang]
                )
E               NameError: name 'gettext' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:20: NameError

During handling of the above exception, another exception occurred:

    def test_valid_input():
        """Test that translations are loaded correctly for a valid input."""
        with patch('os.listdir', return_value=['en']):
            with patch('os.path.isfile', return_value=False):
                with patch('os.stat'):
>                   load_gettext_translations('/tmp/en/LC_MESSAGES', 'mydomain')

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:35: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

directory = '/tmp/en/LC_MESSAGES', domain = 'mydomain'

    def load_gettext_translations(directory: str, domain: str) -> None:
        """Loads translations from `gettext`'s locale tree."""
        global _translations
        global _supported_locales
        global _use_gettext
        _translations = {}
        for lang in os.listdir(directory):
            if lang.startswith("."):
                continue  # skip .svn, etc
            if os.path.isfile(os.path.join(directory, lang)):
                continue
            try:
                os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
                _translations[lang] = gettext.translation(
                    domain, directory, languages=[lang]
                )
            except Exception as e:
>               gen_log.error("Cannot load translation for '%s': %s", lang, str(e))
E               NameError: name 'gen_log' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:24: NameError
_______________________________ test_none_input ________________________________

    def test_none_input():
        """Test that translations are not loaded when given None inputs."""
        with patch('os.listdir', return_value=[]):
>           load_gettext_translations(None, None)

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

directory = None, domain = None

    def load_gettext_translations(directory: str, domain: str) -> None:
        """Loads translations from `gettext`'s locale tree."""
        global _translations
        global _supported_locales
        global _use_gettext
        _translations = {}
        for lang in os.listdir(directory):
            if lang.startswith("."):
                continue  # skip .svn, etc
            if os.path.isfile(os.path.join(directory, lang)):
                continue
            try:
                os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
                _translations[lang] = gettext.translation(
                    domain, directory, languages=[lang]
                )
            except Exception as e:
                gen_log.error("Cannot load translation for '%s': %s", lang, str(e))
                continue
>       _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
E       NameError: name '_default_locale' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:26: NameError
____________________________ test_invalid_directory ____________________________

    def test_invalid_directory():
        """Test that an error is logged when the directory does not exist."""
        with patch('os.listdir', return_value=['en']):
            with patch('os.path.isfile', return_value=True):  # Simulate a file instead of a directory
                with pytest.raises(FileNotFoundError):
>                   load_gettext_translations('/nonexistent/directory', 'mydomain')

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

directory = '/nonexistent/directory', domain = 'mydomain'

    def load_gettext_translations(directory: str, domain: str) -> None:
        """Loads translations from `gettext`'s locale tree."""
        global _translations
        global _supported_locales
        global _use_gettext
        _translations = {}
        for lang in os.listdir(directory):
            if lang.startswith("."):
                continue  # skip .svn, etc
            if os.path.isfile(os.path.join(directory, lang)):
                continue
            try:
                os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
                _translations[lang] = gettext.translation(
                    domain, directory, languages=[lang]
                )
            except Exception as e:
                gen_log.error("Cannot load translation for '%s': %s", lang, str(e))
                continue
>       _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
E       NameError: name '_default_locale' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py:26: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_gettext_translations_0.py::test_invalid_directory
============================== 3 failed in 0.11s ===============================
"""