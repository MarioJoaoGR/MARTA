
import pytest
from ansible.module_utils.urls import prepare_multipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from io import BytesIO
import os
import mimetypes


def test_prepare_multipart_invalid_input():
    with pytest.raises(TypeError):
        prepare_multipart("not a mapping")

def test_prepare_multipart_missing_filename():
    fields = {
        "file1": {"mime_type": "application/octet-stream"},
        "text_form_field": "value"
    }
    
    with pytest.raises(ValueError):
        prepare_multipart(fields)
