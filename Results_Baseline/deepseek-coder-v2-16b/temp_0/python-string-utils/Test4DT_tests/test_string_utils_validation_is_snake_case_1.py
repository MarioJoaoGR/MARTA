
import re

def test_snake_case():
    assert re.match(r'^[a-z]+(_[a-z]+)*$', "this_is_a_test") is not None

# Run your tests
test_snake_case()
