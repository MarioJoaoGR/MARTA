
import pytest
from unittest.mock import patch
import os
import csv
import codecs
import re
from tornado.locale import _translations, _supported_locales, escape

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
            print(f"Unrecognized locale {locale} (path: {os.path.join(directory, path)})")
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
                    print(f"Unrecognized plural indicator {plural} in {path} line {i + 1}")
                    continue
                _translations[locale].setdefault(plural, {})[english] = translation
    _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
    print(f"Supported locales: {sorted(_supported_locales)}")

@pytest.fixture(scope="module")
def load_translations():
    with patch('builtins.__import__', side_effect=lambda name, *args: __import__(name)):
        from translation_loader import load_translations
        return load_translations

# Test for valid input
@pytest.mark.parametrize("directory", ["path/to/valid/translation/directory"])
def test_valid_input(load_translations, directory):
    load_translations(directory)
    assert isinstance(_translations, dict)
    assert len(_translations) > 0
    for locale in _translations:
        assert isinstance(_translations[locale], dict)
        for plural in _translations[locale]:
            assert isinstance(_translations[locale][plural], dict)
            assert len(_translations[locale][plural]) > 0

# Test for edge case with None input
@pytest.mark.parametrize("directory", [None])
def test_edge_case_none(load_translations, directory):
    with pytest.raises(TypeError):
        load_translations(directory)

# Test for invalid input (non-existent directory)
@pytest.mark.parametrize("directory", ["path/to/invalid/translation/directory"])
def test_invalid_input(load_translations, directory):
    with pytest.raises(FileNotFoundError):
        load_translations(directory)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_tornado_locale_load_translations_0.py __________
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_0.py:10: in <module>
    def load_translations(directory: str, encoding: Optional[str] = None) -> None:
E   NameError: name 'Optional' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_locale_load_translations_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""