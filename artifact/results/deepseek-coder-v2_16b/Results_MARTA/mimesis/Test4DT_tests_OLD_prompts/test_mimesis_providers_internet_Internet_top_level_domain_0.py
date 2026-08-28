
import pytest
from unittest.mock import patch
from mimesis.providers.internet import Internet, TLDType

@pytest.fixture(scope="function")
def internet_instance():
    return Internet()


def test_edge_case_none(internet_instance):
    with patch('mimesis.providers.internet.Internet._validate_enum', return_value=None):
        with pytest.raises(KeyError):
            internet_instance.top_level_domain()