
import pytest
from httpie.output.streams import PrettyStream
from unittest.mock import patch

def test_pretty_stream_initialization():
    conversion = object()
    formatting = object()
    with pytest.raises(TypeError):
        pretty_stream = PrettyStream(conversion=conversion, formatting=formatting)

