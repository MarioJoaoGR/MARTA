
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys

class TestJsonDictPreservingDuplicateKeys:
    def test_invalid_input(self):
        # Arrange
        items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
        
        try:
            # Act
            json_dict = JsonDictPreservingDuplicateKeys(items)
            
            # Assert
            assert '__hack__' in json_dict, "The dictionary should have the '__hack__' key."
            assert json_dict['__hack__'] == '__hack__', "The value of '__hack__' should be '__hack__'."
        except TypeError as e:
            # Assert
            assert False, f"Unexpected TypeError: {e}"
