
from isort.deprecated.finders import BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from typing import Iterable, Sequence
from unittest.mock import MagicMock
import pytest

class Config:
    def __init__(self, verbose=False):
        self.verbose = verbose

class FindersManager:
    _default_finders_classes: Sequence[type[BaseFinder]] = (ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder)

    def __init__(self, config: Config, finder_classes: Iterable[type[BaseFinder]] | None = None):
        self.verbose: bool = config.verbose

        if finder_classes is None:
            finder_classes = self._default_finders_classes
        finders: list[BaseFinder] = []
        for finder_cls in finder_classes:
            try:
                finders.append(finder_cls(config))
            except Exception as exception:
                if self.verbose:
                    print(f"{finder_cls.__name__} encountered an error ({exception}) during instantiation and cannot be used")
        self.finders: tuple[BaseFinder, ...] = tuple(finders)

def test_invalid_inputs():
    config = Config(verbose=True)
    manager = FindersManager(config=config)
    assert isinstance(manager.verbose, bool)
