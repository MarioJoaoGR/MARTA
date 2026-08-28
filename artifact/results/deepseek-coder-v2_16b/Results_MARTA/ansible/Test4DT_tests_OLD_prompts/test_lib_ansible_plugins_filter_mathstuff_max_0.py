
import pytest
from ansible.plugins.filter import mathstuff

# Assuming HAS_MIN_MAX is a condition that checks if the required Jinja2 version is available
HAS_MIN_MAX = True  # Placeholder for actual check

def do_max(environment, a):
    environment['result'] = max(a)

@pytest.mark.skipif(not HAS_MIN_MAX, reason="Requires Jinja2 with min/max support")
def test_max_with_list():
    result = mathstuff.max(environment={'result': None}, a=[1, 2, 3, 4])
    assert result == 4
