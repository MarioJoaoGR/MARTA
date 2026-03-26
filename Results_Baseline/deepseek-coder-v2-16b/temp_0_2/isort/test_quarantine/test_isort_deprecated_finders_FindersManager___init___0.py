
# Module: isort.deprecated.finders
import pytest
from config import Config
from base_finder import BaseFinder
from specific_finders import ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder, CustomFinder1, CustomFinder2

# Test using default finders
def test_default_finders():
    config = Config()
    manager = FindersManager(config=config)  # Fixed the instantiation of FindersManager
    assert isinstance(manager.finders[0], ForcedSeparateFinder), "First finder should be ForcedSeparateFinder"
    assert isinstance(manager.finders[1], LocalFinder), "Second finder should be LocalFinder"
    assert isinstance(manager.finders[2], KnownPatternFinder), "Third finder should be KnownPatternFinder"
    assert isinstance(manager.finders[3], PathFinder), "Fourth finder should be PathFinder"
    assert isinstance(manager.finders[4], RequirementsFinder), "Fifth finder should be RequirementsFinder"
    assert isinstance(manager.finders[5], DefaultFinder), "Sixth finder should be DefaultFinder"

# Test using custom finders
def test_custom_finders():
    config = Config()
    manager = FindersManager(config=config, finder_classes=[CustomFinder1, CustomFinder2])  # Fixed the instantiation of FindersManager
    assert isinstance(manager.finders[0], CustomFinder1), "First finder should be CustomFinder1"
    assert isinstance(manager.finders[1], CustomFinder2), "Second finder should be CustomFinder2"

# Test with invalid config
def test_invalid_config():
    with pytest.raises(Exception):
        manager = FindersManager(config=None)  # Fixed the instantiation of FindersManager
        assert False, "Should raise an exception for invalid config"  # This line is unnecessary and should be removed or corrected if needed

# Test with no finder classes provided
def test_no_finder_classes():
    config = Config()
    manager = FindersManager(config=config)  # Fixed the instantiation of FindersManager
    assert len(manager.finders) == 6, "Default finders count should be 6"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_FindersManager___init___0
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:4:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:5:0: E0401: Unable to import 'base_finder' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:6:0: E0401: Unable to import 'specific_finders' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:11:14: E0602: Undefined variable 'FindersManager' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:22:14: E0602: Undefined variable 'FindersManager' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:29:18: E0602: Undefined variable 'FindersManager' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0.py:35:14: E0602: Undefined variable 'FindersManager' (undefined-variable)


"""