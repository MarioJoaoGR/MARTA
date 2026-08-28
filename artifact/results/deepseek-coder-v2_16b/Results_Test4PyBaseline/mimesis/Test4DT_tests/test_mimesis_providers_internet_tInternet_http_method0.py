
import pytest
from mimesis.providers.internet import Internet

# Assuming HTTP_METHODS is a predefined list of possible HTTP methods
HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']  # Example methods, adjust as necessary

@pytest.fixture(scope="module")
def internet():
    return Internet()

def test_http_method_default(internet):
    method = internet.http_method()
    assert method in HTTP_METHODS, f"Expected method to be one of {HTTP_METHODS}, but got {method}"

def test_http_method_specific_seed(internet):
    specific_seed_internet = Internet(seed=12345)
    method_with_seed = specific_seed_internet.http_method()