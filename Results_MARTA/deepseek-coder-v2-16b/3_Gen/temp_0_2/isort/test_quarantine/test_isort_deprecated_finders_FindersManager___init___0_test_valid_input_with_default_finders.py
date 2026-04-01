
import pytest
from isort.deprecated.finders import FindersManager, BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from unittest.mock import MagicMock

@pytest.fixture
def config():
    mock_config = MagicMock()
    mock_config.verbose = True
    return mock_config

@pytest.fixture
def finder_classes():
    return [ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder]

def test_valid_input_with_default_finders(config, finder_classes):
    manager = FindersManager(config=config, finder_classes=finder_classes)
    assert isinstance(manager.finders[0], ForcedSeparateFinder)
    assert isinstance(manager.finders[1], LocalFinder)
    assert isinstance(manager.finders[2], KnownPatternFinder)
    assert isinstance(manager.finders[3], PathFinder)
    assert isinstance(manager.finders[4], RequirementsFinder)
    assert isinstance(manager.finders[5], DefaultFinder)
