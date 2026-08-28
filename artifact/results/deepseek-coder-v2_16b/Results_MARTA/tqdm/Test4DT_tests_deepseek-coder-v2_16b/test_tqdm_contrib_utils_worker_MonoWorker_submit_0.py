
import pytest
from tqdm.contrib.utils_worker import MonoWorker
from concurrent.futures import Future

def test_invalid_input():
    mono_worker = MonoWorker()
    with pytest.raises(TypeError):
        mono_worker.submit()  # No arguments provided, should raise TypeError

