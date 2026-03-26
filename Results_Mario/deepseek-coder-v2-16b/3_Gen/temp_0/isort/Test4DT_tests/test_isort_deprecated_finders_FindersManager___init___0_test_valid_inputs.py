
import pytest
from isort.deprecated.finders import FindersManager, Config, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder

@pytest.fixture
def setup_manager():
    my_config = Config()
    custom_finders = [ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder]
    manager = FindersManager(config=my_config, finder_classes=custom_finders)
    return manager

def test_valid_inputs(setup_manager):
    assert isinstance(setup_manager.finders, tuple), "Finders should be a tuple"
    assert len(setup_manager.finders) == 6, "Expected 6 finders to be instantiated"
