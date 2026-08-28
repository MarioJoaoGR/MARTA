
# test_tqdm_notebook_tqdm_notebook_display_0.py
import pytest
from tqdm.notebook import tqdm_notebook
import time



def test_invalid_input():
    with pytest.raises(ImportError):
        for i in tqdm_notebook(range(10)):
            raise ImportError("Mocked ImportError for testing purposes")