
import pytest
from httpie.output.streams import RawStream, BaseStream
from unittest.mock import patch

def test_valid_input_default_chunk_size():
    with patch('httpie.output.streams.BaseStream.__init__', return_value=None) as mock_init:
        raw_stream = RawStream()
        assert isinstance(raw_stream, RawStream), "Expected an instance of RawStream"
        mock_init.assert_called_once()

def test_valid_input_specified_chunk_size():
    with patch('httpie.output.streams.BaseStream.__init__', return_value=None) as mock_init:
        raw_stream = RawStream(chunk_size=512)
        assert isinstance(raw_stream, RawStream), "Expected an instance of RawStream"
        mock_init.assert_called_once()

def test_invalid_input_none_num_lines():
    with patch('httpie.output.streams.BaseStream.__init__', return_value=None) as mock_init:
        raw_stream = RawStream()
        assert isinstance(raw_stream, RawStream), "Expected an instance of RawStream"
        mock_init.assert_called_once()
