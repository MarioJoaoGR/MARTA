
import os
import io
import pytest

def read_utf8_file(path, encoding='utf-8'):
    if not os.access(path, os.R_OK):
        return None
    with io.open(path, 'r', encoding=encoding) as fd:
        content = fd.read()
    return content

@pytest.fixture(params=[
    ('/path/to/valid_file.txt', True),
    ('/path/to/nonexistent_file.txt', False),
    ('/path/to/valid_file.txt', 'latin1')
])
def file_and_encoding(request):
    path, encoding = request.param
    return path, encoding

def test_read_utf8_file(tmp_path, file_and_encoding):
    path, expected_encoding = file_and_encoding
    if not os.path.exists(path):
        pytest.skip("File does not exist")
    
    content = read_utf8_file(path, encoding=expected_encoding)
    if expected_encoding == 'latin1':
        assert content is None, "Expected None for invalid encoding"
    else:
        assert isinstance(content, str), "Content should be a string"
        assert len(content) > 0, "Content should not be empty"

if __name__ == "__main__":
    pytest.main()
