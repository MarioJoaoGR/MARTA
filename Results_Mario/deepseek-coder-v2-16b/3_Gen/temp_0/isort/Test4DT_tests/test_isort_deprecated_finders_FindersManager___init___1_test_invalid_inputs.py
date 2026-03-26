
import pytest
from isort.deprecated.finders import FindersManager, Config, BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder

def test_invalid_inputs():
    class NonFinder: pass
    
    manager = FindersManager(config=Config(), finder_classes=[NonFinder] * 6)
    
    assert len(manager.finders) == 0
