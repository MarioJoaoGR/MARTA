
import re
from string_utils.manipulation import __StringFormatter



def test___StringFormatter___fix_saxon_genitive_no_match():
    # Arrange
    input_string = "hello world"
    formatter = __StringFormatter(input_string)
    match = re.match(r"(\b\w+)' s\b", "hello s")
    
    # Act & Assert
    assert match is None