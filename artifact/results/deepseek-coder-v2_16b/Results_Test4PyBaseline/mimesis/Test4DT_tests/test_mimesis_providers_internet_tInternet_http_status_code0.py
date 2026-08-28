
import pytest
from mimesis.providers.internet import Internet

# Assuming HTTP_STATUS_CODES is a predefined list of HTTP status codes
HTTP_STATUS_CODES = [200, 404, 500, 301, 302]

@pytest.fixture(scope="module")
def internet():
    return Internet()

def test_http_status_code_default(internet):
    status_code = internet.http_status_code()
    assert status_code in HTTP_STATUS_CODES, f"Expected one of {HTTP_STATUS_CODES}, but got {status_code}"

@pytest.fixture(params=[None, 12345])
def seed_param(request):
    return request.param

def test_http_status_code_with_seed_param(internet, seed_param):
    internet = Internet(seed=seed_param)
    status_code = internet.http_status_code()