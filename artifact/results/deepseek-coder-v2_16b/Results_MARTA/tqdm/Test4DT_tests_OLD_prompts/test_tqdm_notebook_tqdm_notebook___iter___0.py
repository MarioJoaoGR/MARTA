
import pytest
from unittest.mock import patch, MagicMock
from tqdm.notebook import tqdm_notebook



def test_invalid_input():
    with patch('tqdm.notebook.display', new=MagicMock()):
        with pytest.raises(ImportError):
            pb = tqdm_notebook(range(10))