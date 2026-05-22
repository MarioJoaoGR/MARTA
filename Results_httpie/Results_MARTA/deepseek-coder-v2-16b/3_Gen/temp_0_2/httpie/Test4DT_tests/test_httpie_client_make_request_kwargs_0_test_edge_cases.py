
import unittest.mock as mock
from httpie.client import make_request_kwargs, Environment
import argparse
import requests

def test_make_request_kwargs():
    # Create a mock environment and arguments
    env = Environment()
    args = argparse.Namespace(
        method='POST',
        url='https://example.com',
        json={'key': 'value'},
        files=None,
        form=False,
        multipart=False,
        boundary=None,
        headers={},
        auth=None,
        params={},
        chunked=True,
        offline=False,
        data='data'
    )
    
    # Mock the necessary functions and objects
    with mock.patch('httpie.client.json_dict_to_request_body', return_value='mocked_json'):
        with mock.patch('httpie.client.make_default_headers', return_value={'Content-Type': 'application/json'}):
            with mock.patch('httpie.client.finalize_headers', return_value={'Content-Type': 'application/json'}):
                with mock.patch('httpie.client.get_multipart_data_and_content_type', return_value=('mocked_data', 'multipart/form-data')):
                    with mock.patch('httpie.client.prepare_request_body', return_value='prepared_data'):
                        # Call the function and check the result
                        request_kwargs = make_request_kwargs(env, args)
                        assert request_kwargs['method'] == 'post'
                        assert request_kwargs['url'] == 'https://example.com'
                        assert request_kwargs['headers']['Content-Type'] == 'application/json'
                        assert request_kwargs['data'] == 'prepared_data'
                        assert request_kwargs['auth'] is None
                        assert list(request_kwargs['params']) == []
