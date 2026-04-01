
import pytest
from superstring.superstring import SuperStringBase, SuperStringConcatenation

def test_error_case():
    with pytest.raises(TypeError):
        s1 = SuperStringBase('Hello')
