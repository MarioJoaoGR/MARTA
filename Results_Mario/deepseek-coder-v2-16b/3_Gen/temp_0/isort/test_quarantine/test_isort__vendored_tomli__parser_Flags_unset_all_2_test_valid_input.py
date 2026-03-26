
from isort._vendored.tomli._parser import Flags
from typing import Dict, List

class Flags:
    """Flags that map to parsed keys/namespaces."""
    
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self) -> None:
        self._flags: Dict[str, dict] = {}

    def unset_all(self, key: List[str]) -> None:
        """Unsets all flags in the nested dictionary corresponding to the given key.
        
        This function iterates through the keys of the provided `key` argument, traversing 
        the nested dictionary structure within `self._flags`. If a key is not found at any level, 
        it returns immediately without making any changes. Otherwise, it removes the last key in the sequence.
        
        Parameters:
            key (List[str]): A list of strings representing the path to the flags to be unset. The last string in this list will be removed if present.
        
        Returns:
            None
        
        Example:
            >>> flags = Flags()
            >>> flags._flags['a'] = {'nested': {}}
            >>> flags.unset_all(['a'])  # Removes the nested dictionary at 'a'
            
            If 'a' does not exist, no changes are made to `self._flags`.
        """
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return
            cont = cont[k]["nested"]
        cont.pop(key[-1], None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_Flags_unset_all_2_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2_test_valid_input.py:5:0: E0102: class already defined line 2 (function-redefined)


"""