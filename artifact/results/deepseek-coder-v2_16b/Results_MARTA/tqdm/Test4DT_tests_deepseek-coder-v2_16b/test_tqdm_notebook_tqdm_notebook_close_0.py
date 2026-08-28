
import pytest
from tqdm.notebook import tqdm_notebook



def test_invalid_input():
    with pytest.raises(ImportError):
        tqdm_notebook(range(-1))  # This should raise an ImportError due to negative range