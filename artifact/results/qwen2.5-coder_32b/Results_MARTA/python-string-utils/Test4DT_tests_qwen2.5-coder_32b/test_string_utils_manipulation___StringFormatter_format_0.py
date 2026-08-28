
import pytest
from string_utils.manipulation import __StringFormatter




def test_multiple_sentences():
    formatter = __StringFormatter("this is the first sentence. here is another one!")
    formatted_string = formatter.format()
    assert formatted_string == 'This is the first sentence. Here is another one!'

def test_saxon_genitive_construction():
    formatter = __StringFormatter("The cat's fur was black.")
    formatted_string = formatter.format()
    assert formatted_string == "The cat's fur was black."

