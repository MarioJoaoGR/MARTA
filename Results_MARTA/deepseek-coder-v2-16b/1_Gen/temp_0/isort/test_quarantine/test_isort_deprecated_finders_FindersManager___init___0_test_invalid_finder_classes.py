
from isort.deprecated.finders import (
    ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
)

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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:7:30: E0602: Undefined variable 'Sequence' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:7:44: E0602: Undefined variable 'BaseFinder' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:9:31: E0602: Undefined variable 'Config' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:9:55: E0602: Undefined variable 'Iterable' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:9:69: E0602: Undefined variable 'BaseFinder' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:14:22: E0602: Undefined variable 'BaseFinder' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_invalid_finder_classes.py:21:28: E0602: Undefined variable 'BaseFinder' (undefined-variable)


"""