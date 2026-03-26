
# Module: isort.exceptions
import pytest
from isort import UnsupportedSettings

# Test case for the UnsupportedSettings class initialization with a single unsupported setting
def test_unsupported_settings_single():
    try:
        raise UnsupportedSettings({'setting1': {'value': 'some_value', 'source': 'config'}})
    except UnsupportedSettings as e:
        assert str(e) == "isort was provided settings that it doesn't support:\n\n" \
                          "\t- setting1 = some_value  (source: 'config')\n\n" \
                          "For a complete and up-to-date listing of supported settings see: " \
                          "https://pycqa.github.io/isort/docs/configuration/options."

# Test case for the UnsupportedSettings class initialization with multiple unsupported settings
def test_unsupported_settings_multiple():
    try:
        raise UnsupportedSettings({
            'setting1': {'value': 'some_value', 'source': 'config'},
            'setting2': {'value': 'another_value', 'source': 'cli'}
        })
    except UnsupportedSettings as e:
        assert str(e) == "isort was provided settings that it doesn't support:\n\n" \
                          "\t- setting1 = some_value  (source: 'config')\n" \
                          "\t- setting2 = another_value  (source: 'cli')\n\n" \
                          "For a complete and up-to-date listing of supported settings see: " \
                          "https://pycqa.github.io/isort/docs/configuration/options."

# Test case for the UnsupportedSettings class initialization with an empty dictionary (no unsupported settings)
def test_unsupported_settings_empty():
    try:
        raise UnsupportedSettings({})
    except UnsupportedSettings as e:
        assert str(e) == "isort was provided settings that it doesn't support:\n\n" \
                          "For a complete and up-to-date listing of supported settings see: " \
                          "https://pycqa.github.io/isort/docs/configuration/options."

# Test case for the UnsupportedSettings class initialization with an unsupported setting in a different format
def test_unsupported_settings_wrong_format():
    try:
        raise UnsupportedSettings({'setting1': {'value': 'some_value'}})  # Missing 'source' key
    except UnsupportedSettings as e:
        assert str(e) == "isort was provided settings that it doesn't support:\n\n" \
                          "\t- setting1 = some_value  (source: 'unknown')\n\n" \
                          "For a complete and up-to-date listing of supported settings see: " \
                          "https://pycqa.github.io/isort/docs/configuration/options."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_UnsupportedSettings__format_option_0
isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings__format_option_0.py:4:0: E0611: No name 'UnsupportedSettings' in module 'isort' (no-name-in-module)


"""