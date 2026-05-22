
import pytest
from unittest.mock import patch
from httpie.models import RequestsMessageKind

class OutputOptions:
    """
    A class representing options for outputting different parts of a requests message.

    Attributes:
        kind (RequestsMessageKind): The type of the request message, which determines the format or content of the message.
        headers (bool): A flag indicating whether to include headers in the output.
        body (bool): A flag indicating whether to include the body of the message in the output.
        meta (bool, optional): A flag indicating whether to include metadata in the output. Defaults to False.

    Methods:
        any(): Returns a boolean value indicating if any part of the message is included in the output.

    Examples:
        >>> options = OutputOptions(kind=RequestsMessageKind.JSON, headers=True, body=False, meta=True)
        >>> print(options.any())  # True, because both headers and meta are set to True
        >>> other_options = OutputOptions(kind=RequestsMessageKind.TEXT, headers=False, body=False, meta=False)
        >>> print(other_options.any())  # False, none of the options are set to True
    """
    def __init__(self, kind: RequestsMessageKind, headers: bool, body: bool, meta: bool = False):
        self.kind = kind
        self.headers = headers
        self.body = body
        self.meta = meta

    def any(self):
        return (
            self.headers
            or self.body
            or self.meta
        )

def test_invalid_inputs():
    with patch('httpie.models.RequestsMessageKind', new=type('RequestsMessageKind', (), {'JSON': 'MockedJSON'})) as MockedKind:
        options = OutputOptions(kind=MockedKind.JSON, headers=True, body=False, meta=True)
        assert options.any() == True
        
        other_options = OutputOptions(kind=MockedKind.JSON, headers=False, body=False, meta=False)
        assert other_options.any() == False
