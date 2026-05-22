
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import assert_cant_happen

@pytest.mark.parametrize("exception", [ValueError])
def test_error_handling(exception):
    with patch('httpie.cli.nested_json.parse.assert_cant_happen', side_effect=exception):
        with pytest.raises(ValueError) as exc_info:
            assert_cant_happen()
        assert str(exc_info.value) == 'Unexpected value'
