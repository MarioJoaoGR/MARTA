
import pytest
from isort.deprecated.finders import FindersManager, Config, BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder

class MockConfig(Config):
    pass

config = MockConfig()
manager = FindersManager(config=config, finder_classes=[ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder])

def test_valid_inputs():
    assert isinstance(manager.finders, tuple)
    assert all(isinstance(finder, BaseFinder) for finder in manager.finders)
