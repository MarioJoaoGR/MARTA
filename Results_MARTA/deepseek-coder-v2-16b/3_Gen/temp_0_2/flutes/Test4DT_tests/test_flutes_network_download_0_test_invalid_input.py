
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from flutes.network import download

@pytest.mark.parametrize("url", ["invalid_url"])
def test_invalid_input(url):
    with pytest.raises(Exception):
        download(url)
