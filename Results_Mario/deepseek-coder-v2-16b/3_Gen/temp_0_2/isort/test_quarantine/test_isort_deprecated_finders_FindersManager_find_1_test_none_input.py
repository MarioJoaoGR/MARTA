
from isort.deprecated.finders import ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from typing import Iterable, Sequence
from isort import Config
from isort.finders import BaseFinder

class FindersManager:
    _default_finders_classes: Sequence[type[BaseFinder]] = (ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder)

    def __init__(self, config: Config, finder_classes: Iterable[type[BaseFinder]] | None = None) -> None:
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

    def find(self, module_name: str) -> str | None:
        for finder in self.finders:
            try:
                section = finder.find(module_name)
                if section is not None:
                    return section
            except Exception as exception:
                if self.verbose:
                    print(f"{finder.__class__.__name__} encountered an error ({exception}) while trying to identify the {module_name} module")
        return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_FindersManager_find_1_test_none_input
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_none_input.py:5:0: E0401: Unable to import 'isort.finders' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_none_input.py:5:0: E0611: No name 'finders' in module 'isort' (no-name-in-module)


"""