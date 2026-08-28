
import pytest
from apimd.loader import gen_api
from os.path import isdir, join
from os import mkdir
from typing import Sequence

# Ensure the 'docs' directory exists for testing
if not isdir('docs'):
    mkdir('docs')

def test_gen_api_with_table_of_contents():
    """Test gen_api with table of contents."""
    root_names = {'Package One': 'package1'}
    
    # Call the function
    generated_docs = gen_api(root_names, toc=True)
    
    # Assert that one file is created in the 'docs' directory
    assert len(generated_docs) == 1





