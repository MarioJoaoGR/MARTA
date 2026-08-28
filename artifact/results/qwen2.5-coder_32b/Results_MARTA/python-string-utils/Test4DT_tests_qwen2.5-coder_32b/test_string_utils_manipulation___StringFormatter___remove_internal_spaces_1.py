
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError





def test___StringFormatter___init_with_valid_string():
    # Arrange & Act
    formatter = __StringFormatter("hello world")
    
    # Assert
    assert formatter.input_string == "hello world"

def test___StringFormatter___init_with_invalid_type():
    # Arrange & Act & Assert
    try:
        __StringFormatter(123)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "int"'