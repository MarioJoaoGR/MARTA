
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError, _UndefinedParameterAction

class _RaiseUndefinedParameters:
    """
        This action raises UndefinedParameterError if it encounters an undefined
        parameter during initialization.
    """
    
    @staticmethod
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        """
        Handles the initialization of a class from a dictionary by checking for undefined parameters.
        
        Parameters:
            cls (class): The class object to which the dictionary will be passed during initialization.
            kvs (Dict): A dictionary containing key-value pairs where keys are parameter names and values are their corresponding values.
            
        Returns:
            Dict[str, Any]: A dictionary containing only the defined parameters from the input dictionary.
        
        Raises:
            UndefinedParameterError: If any of the provided keys in the dictionary do not match any field of the class, an UndefinedParameterError is raised with a message listing the undefined parameters.
            
        Examples:
            >>> class ExampleClass:
            ...     field1: int
            ...     field2: str
            ... 
            >>> kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
            >>> known_params = handle_from_dict(ExampleClass, kvs)
            >>> print(known_params)    # Output: {'field1': 1, 'field2': 'hello'}
            
        Notes:
            - This function is used to ensure that only the parameters defined in the class are passed during initialization.
            - It uses the `_separate_defined_undefined_kvs` method from `_UndefinedParameterAction` to separate known and unknown parameters based on the class fields.
            - If any parameter is found to be undefined, it raises an `UndefinedParameterError`.
        """
        known, unknown = \
            _UndefinedParameterAction._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
        if len(unknown) > 0:
            raise UndefinedParameterError(
                f"Received undefined initialization arguments {unknown}")
        return known

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.02s =============================
"""