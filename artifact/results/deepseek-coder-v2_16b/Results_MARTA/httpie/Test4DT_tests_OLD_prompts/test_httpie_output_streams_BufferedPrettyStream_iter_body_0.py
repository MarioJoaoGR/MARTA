
import pytest
from unittest.mock import MagicMock, patch
from httpie.output.streams import BufferedPrettyStream

def test_buffered_pretty_stream_initialization():
    msg = MagicMock()
    conversion = MagicMock()
    process_body = lambda x: x
    
    with pytest.raises(TypeError):
        buffered_pretty_stream = BufferedPrettyStream(msg=msg, conversion=conversion, process_body=process_body)

def test_iter_body_with_text_content():
    msg = MagicMock()
    msg.iter_body.return_value = [b'line1\n', b'line2\n']
    conversion = MagicMock()
    process_body = lambda x: x.decode('utf-8')
    
    with pytest.raises(TypeError):
        buffered_pretty_stream = BufferedPrettyStream(msg=msg, conversion=conversion, process_body=process_body)

def test_iter_body_with_binary_content():
    msg = MagicMock()
    msg.iter_body.return_value = [b'\0' * 10]
    conversion = MagicMock()
    
    with pytest.raises(TypeError):
        buffered_pretty_stream = BufferedPrettyStream(msg=msg, conversion=conversion, process_body=lambda x: x)

def test_iter_body_with_null_characters():
    msg = MagicMock()
    msg.iter_body.return_value = [b'line1\0line2']
    conversion = MagicMock()
    process_body = lambda x: x.decode('utf-8')
    
    with pytest.raises(TypeError):
        buffered_pretty_stream = BufferedPrettyStream(msg=msg, conversion=conversion, process_body=process_body)

def test_iter_body_with_large_content():
    msg = MagicMock()
    msg.iter_body.return_value = [b'a'] * (1024 * 10 + 1)
    conversion = MagicMock()
    process_body = lambda x: x.decode('utf-8') if isinstance(x, bytes) else x
    
    with pytest.raises(TypeError):
        buffered_pretty_stream = BufferedPrettyStream(msg=msg, conversion=conversion, process_body=process_body)
