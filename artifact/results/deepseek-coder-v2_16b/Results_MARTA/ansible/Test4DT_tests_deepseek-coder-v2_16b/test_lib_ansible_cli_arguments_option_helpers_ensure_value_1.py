
import pytest
from ansible.cli.arguments.option_helpers import ensure_value

class FactNamespace:
    def __init__(self, namespace_name):
        self.namespace_name = namespace_name

    def transform(self, name):
        return getattr(self, name, None)

@pytest.fixture
def config():
    return {'api_key': None}


@pytest.fixture
def my_namespace():
    return FactNamespace('config')

def test_ensure_value_in_namespace(my_namespace):
    ensure_value(my_namespace, 'api_key', 'your_secret_key')
    assert my_namespace.transform('api_key') == 'your_secret_key'