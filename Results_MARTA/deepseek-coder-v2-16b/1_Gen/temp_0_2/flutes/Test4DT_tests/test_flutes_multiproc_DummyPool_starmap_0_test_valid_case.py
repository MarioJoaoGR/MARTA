
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_case():
    # Arrange
    pool = DummyPool(processes=0, initializer=lambda: None, initargs=(), maxtasksperchild=None, context=None)
    
    # Act & Assert
    assert isinstance(pool, DummyPool)
