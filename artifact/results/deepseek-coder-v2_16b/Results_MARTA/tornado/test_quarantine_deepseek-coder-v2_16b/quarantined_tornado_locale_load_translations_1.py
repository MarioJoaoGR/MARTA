
import os
import csv
import codecs
from typing import Optional
import pytest
from unittest.mock import patch, MagicMock

# Assuming _translations and _supported_locales are defined somewhere in your codebase
_translations = {}
_supported_locales = frozenset()

def load_translations(directory: str, encoding: Optional[str] = None) -> None:
    """Loads translations from CSV files in a directory."""
    global _translations
    global _supported_locales
    _translations = {}
    for path in os.listdir(directory):
        if not path.endswith(".csv"):
            continue
        locale, extension = path.split(".")
        if not re.match("[a-z]+(_[A-Z]+)?$", locale):
            gen_log.error("Unrecognized locale %r (path: %s)", locale, os.path.join(directory, path))
            continue
        full_path = os.path.join(directory, path)
        if encoding is None:
            with open(full_path, "rb") as bf:
                data = bf.read(len(codecs.BOM_UTF16_LE))
            if data in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
                encoding = "utf-16"
            else:
                encoding = "utf-8-sig"
        with open(full_path, encoding=encoding) as f:
            _translations[locale] = {}
            for i, row in enumerate(csv.reader(f)):
                if not row or len(row) < 2:
                    continue
                row = [escape.to_unicode(c).strip() for c in row]
                english, translation = row[:2]
                if len(row) > 2:
                    plural = row[2] or "unknown"
                else:
                    plural = "unknown"
                if plural not in ("plural", "singular", "unknown"):
                    gen_log.error("Unrecognized plural indicator %r in %s line %d", plural, path, i + 1)
                    continue
                _translations[locale].setdefault(plural, {})[english] = translation
    _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
    gen_log.debug("Supported locales: %s", sorted(_supported_locales))

# Test cases for load_translations function



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_load_translations_basic _________________________

    def test_load_translations_basic():
>       with patch('builtins.open', mock_open(read_data='header,translation\nstring1,"Te amo"\n')):
E       NameError: name 'mock_open' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py:53: NameError
_____________________ test_load_translations_with_encoding _____________________

    def test_load_translations_with_encoding():
>       with patch('builtins.open', mock_open(read_data='header,translation\nstring1,"Te amo"\n')):
E       NameError: name 'mock_open' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py:58: NameError
__________________ test_load_translations_unsupported_locale ___________________

    def test_load_translations_unsupported_locale():
>       with patch('builtins.open', mock_open(read_data='header,translation\nstring1,"Te amo"\n')):
E       NameError: name 'mock_open' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py:63: NameError
____________________ test_load_translations_invalid_plural _____________________

    def test_load_translations_invalid_plural():
>       with patch('builtins.open', mock_open(read_data='header,translation,plural\nstring1,"Te amo","invalid"\n')):
E       NameError: name 'mock_open' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py:69: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py::test_load_translations_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py::test_load_translations_with_encoding
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py::test_load_translations_unsupported_locale
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_1.py::test_load_translations_invalid_plural
============================== 4 failed in 0.11s ===============================
"""