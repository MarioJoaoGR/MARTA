
import pytest
from mimesis.providers import Internet


def test_invalid_input_http_method():
    internet_instance = Internet(seed=42)
    with pytest.raises(TypeError):
        invalid_method = internet_instance.http_method("INVALID")