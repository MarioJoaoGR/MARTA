
import pytest
from isort.deprecated.finders import FindersManager, Config, BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder

class MockConfig(Config):
    pass

config = MockConfig()
finders_classes = [ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder]
manager = FindersManager(config=config, finder_classes=finders_classes)

def test_valid_inputs():
    assert isinstance(manager.finders, tuple), "Finders should be a tuple"
    assert len(manager.finders) == 6, "Expected 6 finders to be instantiated"
    for finder in manager.finders:
        assert isinstance(finder, BaseFinder), f"Finder {finder.__class__.__name__} is not a subclass of BaseFinder"
