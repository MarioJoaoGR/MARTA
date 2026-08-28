
import pytest
from httpie.cli.requestitems import RequestItems, RequestHeadersDict, RequestDataDict, RequestJSONDataDict, RequestFilesDict, RequestQueryParamsDict, MultipartRequestDataDict
from unittest.mock import patch

def test_valid_inputs():
    request = RequestItems()
    assert isinstance(request.headers, RequestHeadersDict)
    assert isinstance(request.data, RequestJSONDataDict)

def test_form_based_request():
    request = RequestItems(as_form=True)
    assert isinstance(request.headers, RequestHeadersDict)
    assert isinstance(request.data, RequestDataDict)
