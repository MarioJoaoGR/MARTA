
from isort.deprecated.finders import ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from typing import Sequence, Iterable, Type
from isort.config import Config
from isort.finder import BaseFinder

class FindersManager:
    _default_finders_classes: Sequence[type[BaseFinder]] = (ForcedSeparateFinder,
        LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder,
        DefaultFinder)
    
    def __init__(
        self, config: Config, finder_classes: Iterable[type[BaseFinder]] | None = None
    ) -> None:
        self.verbose: bool = config.verbose

        if finder_classes is None:
            finder_classes = self._default_finders_classes
        finders: list[BaseFinder] = []
        for finder_cls in finder_classes:
            try:
                finders.append(finder_cls(config))
            except Exception as exception:
                # if one finder fails to instantiate isort can continue using the rest
                if self.verbose:
                    print(
                        f"{finder_cls.__name__} encountered an error ({exception}) during "
                        "instantiation and cannot be used"
                    )
        self.finders: tuple[BaseFinder, ...] = tuple(finders)

    def find(self, module_name: str) -> str | None:
        for finder in self.finders:
            try:
                section = finder.find(module_name)
                if section is not None:
                    return section
            except Exception as exception:
                # isort has to be able to keep trying to identify the correct
                # import section even if one approach fails
                if self.verbose:
                    print(
                        f"{finder.__class__.__name__} encountered an error ({exception}) while "
                        f"trying to identify the {module_name} module"
                    )
        return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_FindersManager_find_1_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_valid_input.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_valid_input.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_valid_input.py:5:0: E0401: Unable to import 'isort.finder' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager_find_1_test_valid_input.py:5:0: E0611: No name 'finder' in module 'isort' (no-name-in-module)


"""