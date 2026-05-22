
import unittest.mock as mock
from httpie.uploads import _prepare_file_for_upload, Environment
from io import StringIO

def test_edge_case():
    env = Environment()
    callback = lambda chunk: print(chunk)  # Example callback function that prints each chunk
    
    with mock.patch('httpie.uploads._read_file_with_selectors', return_value=StringIO("test")):
        prepared_file = _prepare_file_for_upload(env, StringIO(), callback, chunked=False)
        assert isinstance(prepared_file, StringIO)
