
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import raw_main
from httpie.manager.__main__ import main as httpie_main
from httpie.status import ExitStatus

def test_invalid_inputs():
    with patch('httpie.core.raw_main', side_effect=Exception("Mocked error for invalid inputs")):
        with pytest.raises(Exception) as excinfo:
            httpie_main()
        assert str(excinfo.value) == "Mocked error for invalid inputs"
