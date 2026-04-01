
import os
import pickle
from pathlib import Path
from flutes.fs import cache

def test_invalid_input():
    def test_function():
        return 'This should not be executed.'
    
    @cache(Path('non_existent_file.pkl'), verbose=True)
    def cached_function():
        return test_function()
    
    try:
        result = cached_function()
    except ValueError as e:
        assert str(e) == 'File non_existent_file.pkl does not exist'
