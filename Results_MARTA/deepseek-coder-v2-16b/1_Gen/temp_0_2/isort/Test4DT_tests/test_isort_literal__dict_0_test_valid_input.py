
import pytest
from collections import OrderedDict

# Define a sample dictionary and pretty printer class
class MyPrettyPrinter:
    def pformat(self, sorted_dict):
        return ', '.join([f'{k}: {v}' for k, v in sorted_dict.items()])

def _dict(value: dict, printer: 'MyPrettyPrinter') -> str:
    return printer.pformat(dict(sorted(value.items(), key=lambda item: item[1])))

# Define the test function
@pytest.mark.parametrize("value", [{"a": 3, "b": 1, "c": 2}])
def test_valid_input(value):
    printer = MyPrettyPrinter()
    result = _dict(value, printer)
    assert result == 'b: 1, c: 2, a: 3'
