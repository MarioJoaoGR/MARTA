
import configparser
from unittest.mock import patch, MagicMock
import pytest

def _config_from_ini(paths):
    parser = configparser.ConfigParser()
    parser.read(paths)

    flags = {
        "changelog_capitalize",
        "changelog_scope",
        "check_build_status",
        "commit_version_number",
        "patch_without_tag",
        "major_on_zero",
        "remove_dist",
        "upload_to_pypi",
        "upload_to_release",
    }

    config = {}
    for key, _ in parser.items("semantic_release"):
        if key in flags:
            config[key] = parser.getboolean("semantic_release", key)
        else:
            config[key] = parser.get("semantic_release", key)

    return config


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

self = <configparser.ConfigParser object at 0x7fe7e1a7de70>
section = 'semantic_release', raw = False, vars = None

    def items(self, section=_UNSET, raw=False, vars=None):
        """Return a list of (name, value) tuples for each option in a section.
    
        All % interpolations are expanded in the return values, based on the
        defaults passed into the constructor, unless the optional argument
        `raw` is true.  Additional substitutions may be provided using the
        `vars` argument, which must be a dictionary whose contents overrides
        any pre-existing defaults.
    
        The section DEFAULT is special.
        """
        if section is _UNSET:
            return super().items()
        d = self._defaults.copy()
        try:
>           d.update(self._sections[section])
E           KeyError: 'semantic_release'

/opt/conda/envs/test4py_env/lib/python3.10/configparser.py:848: KeyError

During handling of the above exception, another exception occurred:

    def test_valid_inputs():
        mock_data = {
            "path/to/file1.ini": {"changelog_capitalize": True, "check_build_status": False},
            "path/to/file2.ini": {"patch_without_tag": True, "major_on_zero": False}
        }
    
        with patch('configparser.ConfigParser.read', return_value=None):
            with patch('configparser.ConfigParser.getboolean', side_effect=lambda section, key: mock_data[section][key]):
                with patch('configparser.ConfigParser.get', side_effect=lambda section, key: str(mock_data[section][key])):
>                   result = _config_from_ini(["path/to/file1.ini", "path/to/file2.ini"])

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py:23: in _config_from_ini
    for key, _ in parser.items("semantic_release"):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <configparser.ConfigParser object at 0x7fe7e1a7de70>
section = 'semantic_release', raw = False, vars = None

    def items(self, section=_UNSET, raw=False, vars=None):
        """Return a list of (name, value) tuples for each option in a section.
    
        All % interpolations are expanded in the return values, based on the
        defaults passed into the constructor, unless the optional argument
        `raw` is true.  Additional substitutions may be provided using the
        `vars` argument, which must be a dictionary whose contents overrides
        any pre-existing defaults.
    
        The section DEFAULT is special.
        """
        if section is _UNSET:
            return super().items()
        d = self._defaults.copy()
        try:
            d.update(self._sections[section])
        except KeyError:
            if section != self.default_section:
>               raise NoSectionError(section)
E               configparser.NoSectionError: No section: 'semantic_release'

/opt/conda/envs/test4py_env/lib/python3.10/configparser.py:851: NoSectionError
_____________________________ test_invalid_inputs ______________________________

self = <configparser.ConfigParser object at 0x7fe7e1a9bc40>
section = 'semantic_release', raw = False, vars = None

    def items(self, section=_UNSET, raw=False, vars=None):
        """Return a list of (name, value) tuples for each option in a section.
    
        All % interpolations are expanded in the return values, based on the
        defaults passed into the constructor, unless the optional argument
        `raw` is true.  Additional substitutions may be provided using the
        `vars` argument, which must be a dictionary whose contents overrides
        any pre-existing defaults.
    
        The section DEFAULT is special.
        """
        if section is _UNSET:
            return super().items()
        d = self._defaults.copy()
        try:
>           d.update(self._sections[section])
E           KeyError: 'semantic_release'

/opt/conda/envs/test4py_env/lib/python3.10/configparser.py:848: KeyError

During handling of the above exception, another exception occurred:

    def test_invalid_inputs():
        mock_data = {
            "path/to/nonexistent.ini": {"changelog_capitalize": True, "check_build_status": False},
            "path/to/malformed.ini": None  # Malformed INI file
        }
    
        with patch('configparser.ConfigParser.read', side_effect=FileNotFoundError):
            with pytest.raises(FileNotFoundError):
                _config_from_ini(["path/to/nonexistent.ini"])
    
        with patch('configparser.ConfigParser.read', return_value=None):
            with pytest.raises(configparser.MissingSectionHeaderError):
>               _config_from_ini(["path/to/malformed.ini"])

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py:23: in _config_from_ini
    for key, _ in parser.items("semantic_release"):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <configparser.ConfigParser object at 0x7fe7e1a9bc40>
section = 'semantic_release', raw = False, vars = None

    def items(self, section=_UNSET, raw=False, vars=None):
        """Return a list of (name, value) tuples for each option in a section.
    
        All % interpolations are expanded in the return values, based on the
        defaults passed into the constructor, unless the optional argument
        `raw` is true.  Additional substitutions may be provided using the
        `vars` argument, which must be a dictionary whose contents overrides
        any pre-existing defaults.
    
        The section DEFAULT is special.
        """
        if section is _UNSET:
            return super().items()
        d = self._defaults.copy()
        try:
            d.update(self._sections[section])
        except KeyError:
            if section != self.default_section:
>               raise NoSectionError(section)
E               configparser.NoSectionError: No section: 'semantic_release'

/opt/conda/envs/test4py_env/lib/python3.10/configparser.py:851: NoSectionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_settings__config_from_ini_0.py::test_invalid_inputs
============================== 2 failed in 0.10s ===============================
"""