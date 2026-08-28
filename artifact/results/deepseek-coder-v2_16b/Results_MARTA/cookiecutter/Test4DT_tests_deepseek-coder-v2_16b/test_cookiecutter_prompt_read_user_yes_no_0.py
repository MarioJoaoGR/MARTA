
import pytest
from cookiecutter.prompt import read_user_yes_no



def test_invalid_inputs():
    with pytest.raises(TypeError):
        read_user_yes_no('Do you like Python?')