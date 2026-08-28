
import pytest
from httpie.output.formatters.headers import HeadersFormatter


def test_custom_configuration_with_format_options():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.enabled is True, "HeadersFormatter enabled should be True if format_options['headers']['sort'] is True"

def test_custom_configuration_without_format_options():
    formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert formatter.enabled is False, "HeadersFormatter enabled should be False if format_options['headers']['sort'] is False"