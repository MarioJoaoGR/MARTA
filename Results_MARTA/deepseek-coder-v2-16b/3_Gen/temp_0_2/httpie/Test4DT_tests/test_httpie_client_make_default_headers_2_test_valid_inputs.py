
import argparse
from unittest import TestCase, mock
from httpie.client import make_default_headers, HTTPHeadersDict

class TestMakeDefaultHeaders(TestCase):
    def test_valid_inputs(self):
        # Create a namespace object to simulate command-line arguments
        args = argparse.Namespace(json=True, data=False, form=False, files=False)

        with mock.patch('httpie.client.DEFAULT_UA', 'test_ua'):
            with mock.patch('httpie.client.JSON_ACCEPT', 'application/json'):
                with mock.patch('httpie.client.JSON_CONTENT_TYPE', 'application/json'):
                    headers = make_default_headers(args)

        expected_headers = HTTPHeadersDict({
            'User-Agent': 'test_ua',
            'Accept': 'application/json'
        })

        if args.json or (not args.form and not args.files):
            expected_headers['Content-Type'] = 'application/json'

        self.assertEqual(headers, expected_headers)
