
from isort.deprecated.finders import BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from typing import Iterable, Sequence

class FindersManager:
    _default_finders_classes: Sequence[type[BaseFinder]] = (ForcedSeparateFinder,
        LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder,
        DefaultFinder)

    def __init__(self, config: 'Config', finder_classes: Iterable[type[BaseFinder]] | None = None) -> None:
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
                    print(f"{finder_cls.__name__} encountered an error ({exception}) during instantiation and cannot be used")
        self.finders: tuple[BaseFinder, ...] = tuple(finders)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.10s =============================
"""