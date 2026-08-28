
import pytest
from unittest.mock import MagicMock, patch
from io import BytesIO
from urllib.parse import urlencode
from requests_toolbelt.multipart.encoder import MultipartEncoder
from httpie.uploads import prepare_request_body, RequestDataDict

def test_invalid_input_type():
    with pytest.raises(TypeError):
        prepare_request_body(body=42)  # Invalid input type




