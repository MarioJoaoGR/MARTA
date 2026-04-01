
from isort.deprecated.finders import BaseFinder, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder

class FindersManager:
    _default_finders_classes: Sequence[type[BaseFinder]] = (ForcedSeparateFinder,
        LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder,
        DefaultFinder)
    
    def __init__(
        self, config: Config, finder_classes: Iterable[type[BaseFinder]] | None = None
    ) -> None:
        """
        A class for managing a collection of finders that are responsible for locating and processing various resources such as files or patterns.

        Parameters:
            config (Config): An instance of the Config class, which provides configuration settings for the finders.
            finder_classes (Iterable[type[BaseFinder]], optional): An iterable of classes derived from BaseFinder, representing the specific types of finders to be used. If not provided, defaults to a predefined set of finder classes.

        Raises:
            Exception: Any exceptions encountered during the instantiation of individual finders will be raised unless they are caught and handled within the class.

        Returns:
            None

        Examples:
            To create an instance of FindersManager with default finders:
                manager = FindersManager(config=my_config)
            
            To specify custom finder classes:
                custom_finders = [CustomFinder1, CustomFinder2]
                manager = FindersManager(config=my_config, finder_classes=custom_finders)
            
        Notes:
            - The class initializes with a set of default finders if no `finder_classes` are provided.
            - Each finder in the list is instantiated with the given configuration (`config`).
            - If a finder fails to instantiate due to an error, it will be skipped and a message will be printed if verbose mode is enabled.
            - The class maintains a tuple of finders that can be accessed via `self.finders`.
        """
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_FindersManager___init___0_test_valid_input_with_default_finders
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_valid_input_with_default_finders.py:5:30: E0602: Undefined variable 'Sequence' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_valid_input_with_default_finders.py:10:22: E0602: Undefined variable 'Config' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___0_test_valid_input_with_default_finders.py:10:46: E0602: Undefined variable 'Iterable' (undefined-variable)


"""