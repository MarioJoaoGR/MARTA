
class NestedDict:
    """
    A class to handle nested dictionaries with the ability to create and access nested structures.

    Attributes:
        dict (dict): The main dictionary that holds the nested structure.

    Methods:
        get_or_create_nest(key, *, access_lists=True) -> dict: Retrieves or creates a nested dictionary for the given key sequence.
            Parameters:
                key (list of str): A list of keys representing the path to the desired nested structure.
                access_lists (bool, optional): If True and encounters a list during traversal, accesses the last element of the list; defaults to True.
            Returns:
                dict: The final nested dictionary or the last accessed element if it's a list when `access_lists` is True.
            Raises:
                KeyError: If there is no nest behind the given key sequence.

    Examples:
        >>> nd = NestedDict()
        >>> nd.get_or_create_nest(['a', 'b', 'c'])
        {}
        >>> nd.dict['a'] = {'b': {}}
        >>> nd.get_or_create_nest(['a', 'b', 'c'])
        {}
        >>> nd.dict['x'] = [1, 2, 3]
        >>> nd.get_or_create_nest(['x'], access_lists=False)
        3
    """
    def __init__(self) -> None:
        # The parsed content of the TOML document
        self.dict: Dict[str, Any] = {}

    def get_or_create_nest(
        self,
        key: List[str],
        *,
        access_lists: bool = True,
    ) -> dict:
        cont: Any = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
                raise KeyError("There is no nest behind this key")
        return cont

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_cases
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_cases.py:32:19: E0602: Undefined variable 'Dict' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_cases.py:32:29: E0602: Undefined variable 'Any' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_cases.py:36:13: E0602: Undefined variable 'List' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_cases.py:40:14: E0602: Undefined variable 'Any' (undefined-variable)


"""