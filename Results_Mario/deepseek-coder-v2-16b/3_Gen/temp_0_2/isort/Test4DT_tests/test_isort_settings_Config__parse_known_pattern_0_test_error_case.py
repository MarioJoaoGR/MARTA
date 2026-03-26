
import pytest
from isort.settings import Config

def test_error_case():
    with pytest.raises(Exception):
        config = Config(settings_file='non_existent_file.ini')
