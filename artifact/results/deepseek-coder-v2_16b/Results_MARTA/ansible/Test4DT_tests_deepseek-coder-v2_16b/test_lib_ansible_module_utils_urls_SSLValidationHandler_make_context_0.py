
import pytest
from ansible.module_utils.urls import SSLValidationHandler
import ssl


def test_sslvalidationhandler_default_trust():
    handler = SSLValidationHandler('example.com', 443)
    context = handler.make_context(None, None)
    assert isinstance(context, ssl.SSLContext)