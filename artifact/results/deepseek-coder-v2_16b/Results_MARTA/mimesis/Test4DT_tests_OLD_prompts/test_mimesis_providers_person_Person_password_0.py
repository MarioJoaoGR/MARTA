
import pytest
from unittest.mock import patch, MagicMock
from mimesis.providers.person import Person as MPerson

@pytest.fixture(scope="function")
def person():
    return MPerson()

def test_password_basic(person):
    with patch('mimesis.providers.person.Person._pull', MagicMock(return_value={'data': 'test'})):
        password = person.password(length=8, hashed=False)
        assert len(password) == 8
        assert isinstance(password, str)

        hashed_password = person.password(length=12, hashed=True)
        assert isinstance(hashed_password, str)
        assert len(hashed_password) == 32
