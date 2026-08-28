
import pytest
from tqdm.notebook import tqdm_notebook



def test_invalid_input_error_handling():
    with pytest.raises(ImportError):
        tqdm_notebook(range(-1))  # Negative range should trigger ImportError