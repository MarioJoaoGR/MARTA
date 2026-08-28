
import pytest
from mimesis.builtins.en import USASpecProvider

@pytest.fixture(scope="module")
def provider():
    return USASpecProvider()


def test_valid_input_fedex(provider):
    tracking_number = provider.tracking_number('fedex')
    assert isinstance(tracking_number, str)
    assert len(tracking_number) == 15 or len(tracking_number) == 18
