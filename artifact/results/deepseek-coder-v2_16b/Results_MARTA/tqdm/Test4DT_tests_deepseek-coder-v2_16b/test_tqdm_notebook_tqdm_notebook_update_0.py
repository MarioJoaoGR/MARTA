
import pytest
from tqdm.notebook import tqdm_notebook
import sys



def test_invalid_input():
    with pytest.raises(ImportError):
        pb = tqdm_notebook()