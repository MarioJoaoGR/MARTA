
import pytest
from ansible.galaxy.api import GalaxyAPI
from urllib.error import URLError
from unittest.mock import patch, MagicMock



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        # Create a GalaxyAPI instance with minimal required parameters but without providing necessary authentication details
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py:9: Failed
_____________________________ test_valid_api_call ______________________________

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f00511ae350>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f0051383440>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f00511ae440>
http_conn_args = {}, host = 'specific-server.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f00511ae830>

    def do_open(self, http_class, req, **http_conn_args):
        """Return an HTTPResponse object for the request, using http_class.
    
        http_class must implement the HTTPConnection API from http.client.
        """
        host = req.host
        if not host:
            raise URLError('no host given')
    
        # will parse host:port
        h = http_class(host, timeout=req.timeout, **http_conn_args)
        h.set_debuglevel(self._debuglevel)
    
        headers = dict(req.unredirected_hdrs)
        headers.update({k: v for k, v in req.headers.items()
                        if k not in headers})
    
        # TODO(jhylton): Should this be redesigned to handle
        # persistent connections?
    
        # We want to make an HTTP/1.1 request, but the addinfourl
        # class isn't prepared to deal with a persistent connection.
        # It will try to read all remaining data from the socket,
        # which will block while the server waits for the next request.
        # So make sure the connection gets closed after the (only)
        # request.
        headers["Connection"] = "close"
        headers = {name.title(): val for name, val in headers.items()}
    
        if req._tunnel_host:
            tunnel_headers = {}
            proxy_auth_hdr = "Proxy-Authorization"
            if proxy_auth_hdr in headers:
                tunnel_headers[proxy_auth_hdr] = headers[proxy_auth_hdr]
                # Proxy-Authorization should not be sent to origin
                # server.
                del headers[proxy_auth_hdr]
            h.set_tunnel(req._tunnel_host, headers=tunnel_headers)
    
        try:
            try:
>               h.request(req.get_method(), req.selector, req.data, headers,
                          encode_chunked=req.has_header('Transfer-encoding'))

/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:1348: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:1303: in request
    self._send_request(method, url, body, headers, encode_chunked)
/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:1349: in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:1298: in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:1058: in _send_output
    self.send(msg)
/opt/conda/envs/test4py_env/lib/python3.10/http/client.py:996: in send
    self.connect()
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:532: in connect
    sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
/opt/conda/envs/test4py_env/lib/python3.10/socket.py:836: in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

host = 'specific-server.com', port = 443, family = 0
type = <SocketKind.SOCK_STREAM: 1>, proto = 0, flags = 0

    def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        """Resolve host and port into list of address info entries.
    
        Translate the host/port argument into a sequence of 5-tuples that contain
        all the necessary arguments for creating a socket connected to that service.
        host is a domain name, a string representation of an IPv4/v6 address or
        None. port is a string service name such as 'http', a numeric port number or
        None. By passing None as the value of host and port, you can pass NULL to
        the underlying C API.
    
        The family, type and proto arguments can be optionally specified in order to
        narrow the list of addresses returned. Passing zero as a value for each of
        these arguments selects the full range of results.
        """
        # We override this function since we want to translate the numeric family
        # and socket type values to enum constants.
        addrlist = []
>       for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
E       socket.gaierror: [Errno -2] Name or service not known

/opt/conda/envs/test4py_env/lib/python3.10/socket.py:967: gaierror

During handling of the above exception, another exception occurred:

self = <username123 "username123" @ https://specific-server.com with priority inf>
url = 'https://specific-server.com/api', args = None, headers = {}
method = None, auth_required = False, error_context_msg = None, cache = False

    @retry_with_delays_and_condition(
        backoff_iterator=generate_jittered_backoff(retries=6, delay_base=2, delay_threshold=40),
        should_retry_error=is_rate_limit_exception
    )
    def _call_galaxy(self, url, args=None, headers=None, method=None, auth_required=False, error_context_msg=None,
                     cache=False):
        url_info = urlparse(url)
        cache_id = get_cache_id(url)
        query = parse_qs(url_info.query)
        if cache and self._cache:
            server_cache = self._cache.setdefault(cache_id, {})
            iso_datetime_format = '%Y-%m-%dT%H:%M:%SZ'
    
            valid = False
            if url_info.path in server_cache:
                expires = datetime.datetime.strptime(server_cache[url_info.path]['expires'], iso_datetime_format)
                valid = datetime.datetime.utcnow() < expires
    
            is_paginated_url = 'page' in query or 'offset' in query
            if valid and not is_paginated_url:
                # Got a hit on the cache and we aren't getting a paginated response
                path_cache = server_cache[url_info.path]
                if path_cache.get('paginated'):
                    if '/v3/' in url_info.path:
                        res = {'links': {'next': None}}
                    else:
                        res = {'next': None}
    
                    # Technically some v3 paginated APIs return in 'data' but the caller checks the keys for this so
                    # always returning the cache under results is fine.
                    res['results'] = []
                    for result in path_cache['results']:
                        res['results'].append(result)
    
                else:
                    res = path_cache['results']
    
                return res
    
            elif not is_paginated_url:
                # The cache entry had expired or does not exist, start a new blank entry to be filled later.
                expires = datetime.datetime.utcnow()
                expires += datetime.timedelta(days=1)
                server_cache[url_info.path] = {
                    'expires': expires.strftime(iso_datetime_format),
                    'paginated': False,
                }
    
        headers = headers or {}
        self._add_auth_token(headers, url, required=auth_required)
    
        try:
            display.vvvv("Calling Galaxy at %s" % url)
>           resp = open_url(to_native(url), data=args, validate_certs=self.validate_certs, headers=headers,
                            method=method, timeout=20, http_agent=user_agent(), follow_redirects='safe')

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:379: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:1535: in open_url
    return Request().open(method, url, data=data, headers=headers, use_proxy=use_proxy,
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:1446: in open
    return urllib_request.urlopen(request, None, timeout)
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:216: in urlopen
    return opener.open(url, data, timeout)
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:519: in open
    response = self._open(req, data)
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:536: in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:496: in _call_chain
    result = func(*args)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:558: in https_open
    return self.do_open(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f00511ae350>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f0051383440>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f00511ae440>
http_conn_args = {}, host = 'specific-server.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f00511ae830>

    def do_open(self, http_class, req, **http_conn_args):
        """Return an HTTPResponse object for the request, using http_class.
    
        http_class must implement the HTTPConnection API from http.client.
        """
        host = req.host
        if not host:
            raise URLError('no host given')
    
        # will parse host:port
        h = http_class(host, timeout=req.timeout, **http_conn_args)
        h.set_debuglevel(self._debuglevel)
    
        headers = dict(req.unredirected_hdrs)
        headers.update({k: v for k, v in req.headers.items()
                        if k not in headers})
    
        # TODO(jhylton): Should this be redesigned to handle
        # persistent connections?
    
        # We want to make an HTTP/1.1 request, but the addinfourl
        # class isn't prepared to deal with a persistent connection.
        # It will try to read all remaining data from the socket,
        # which will block while the server waits for the next request.
        # So make sure the connection gets closed after the (only)
        # request.
        headers["Connection"] = "close"
        headers = {name.title(): val for name, val in headers.items()}
    
        if req._tunnel_host:
            tunnel_headers = {}
            proxy_auth_hdr = "Proxy-Authorization"
            if proxy_auth_hdr in headers:
                tunnel_headers[proxy_auth_hdr] = headers[proxy_auth_hdr]
                # Proxy-Authorization should not be sent to origin
                # server.
                del headers[proxy_auth_hdr]
            h.set_tunnel(req._tunnel_host, headers=tunnel_headers)
    
        try:
            try:
                h.request(req.get_method(), req.selector, req.data, headers,
                          encode_chunked=req.has_header('Transfer-encoding'))
            except OSError as err: # timeout error
>               raise URLError(err)
E               urllib.error.URLError: <urlopen error [Errno -2] Name or service not known>

/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:1351: URLError

During handling of the above exception, another exception occurred:

    def test_valid_api_call():
        # Create a GalaxyAPI instance with valid parameters and mock the open_url function to return a successful response
        api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123')
    
        # Mock the open_url function to return a successful response with valid JSON data
        mock_open_url = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response._content = b'{"results": [{"name": "test"}]}'
        mock_open_url.return_value = mock_response
    
        with patch('ansible.module_utils.urls.open_url', mock_open_url):
>           response = api_client._call_galaxy('https://specific-server.com/api')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/api.py:157: in run_function
    return call_retryable_function()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <username123 "username123" @ https://specific-server.com with priority inf>
url = 'https://specific-server.com/api', args = None, headers = {}
method = None, auth_required = False, error_context_msg = None, cache = False

    @retry_with_delays_and_condition(
        backoff_iterator=generate_jittered_backoff(retries=6, delay_base=2, delay_threshold=40),
        should_retry_error=is_rate_limit_exception
    )
    def _call_galaxy(self, url, args=None, headers=None, method=None, auth_required=False, error_context_msg=None,
                     cache=False):
        url_info = urlparse(url)
        cache_id = get_cache_id(url)
        query = parse_qs(url_info.query)
        if cache and self._cache:
            server_cache = self._cache.setdefault(cache_id, {})
            iso_datetime_format = '%Y-%m-%dT%H:%M:%SZ'
    
            valid = False
            if url_info.path in server_cache:
                expires = datetime.datetime.strptime(server_cache[url_info.path]['expires'], iso_datetime_format)
                valid = datetime.datetime.utcnow() < expires
    
            is_paginated_url = 'page' in query or 'offset' in query
            if valid and not is_paginated_url:
                # Got a hit on the cache and we aren't getting a paginated response
                path_cache = server_cache[url_info.path]
                if path_cache.get('paginated'):
                    if '/v3/' in url_info.path:
                        res = {'links': {'next': None}}
                    else:
                        res = {'next': None}
    
                    # Technically some v3 paginated APIs return in 'data' but the caller checks the keys for this so
                    # always returning the cache under results is fine.
                    res['results'] = []
                    for result in path_cache['results']:
                        res['results'].append(result)
    
                else:
                    res = path_cache['results']
    
                return res
    
            elif not is_paginated_url:
                # The cache entry had expired or does not exist, start a new blank entry to be filled later.
                expires = datetime.datetime.utcnow()
                expires += datetime.timedelta(days=1)
                server_cache[url_info.path] = {
                    'expires': expires.strftime(iso_datetime_format),
                    'paginated': False,
                }
    
        headers = headers or {}
        self._add_auth_token(headers, url, required=auth_required)
    
        try:
            display.vvvv("Calling Galaxy at %s" % url)
            resp = open_url(to_native(url), data=args, validate_certs=self.validate_certs, headers=headers,
                            method=method, timeout=20, http_agent=user_agent(), follow_redirects='safe')
        except HTTPError as e:
            raise GalaxyError(e, error_context_msg)
        except Exception as e:
>           raise AnsibleError("Unknown error when attempting to call Galaxy at '%s': %s" % (url, to_native(e)))
E           ansible.errors.AnsibleError: Unknown error when attempting to call Galaxy at 'https://specific-server.com/api': <urlopen error [Errno -2] Name or service not known>

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:384: AnsibleError
____________________________ test_invalid_api_call _____________________________

self = <username123 "username123" @ https://specific-server.com with priority inf>
url = 'invalid_url', args = None, headers = {}, method = None
auth_required = False, error_context_msg = None, cache = False

    @retry_with_delays_and_condition(
        backoff_iterator=generate_jittered_backoff(retries=6, delay_base=2, delay_threshold=40),
        should_retry_error=is_rate_limit_exception
    )
    def _call_galaxy(self, url, args=None, headers=None, method=None, auth_required=False, error_context_msg=None,
                     cache=False):
        url_info = urlparse(url)
        cache_id = get_cache_id(url)
        query = parse_qs(url_info.query)
        if cache and self._cache:
            server_cache = self._cache.setdefault(cache_id, {})
            iso_datetime_format = '%Y-%m-%dT%H:%M:%SZ'
    
            valid = False
            if url_info.path in server_cache:
                expires = datetime.datetime.strptime(server_cache[url_info.path]['expires'], iso_datetime_format)
                valid = datetime.datetime.utcnow() < expires
    
            is_paginated_url = 'page' in query or 'offset' in query
            if valid and not is_paginated_url:
                # Got a hit on the cache and we aren't getting a paginated response
                path_cache = server_cache[url_info.path]
                if path_cache.get('paginated'):
                    if '/v3/' in url_info.path:
                        res = {'links': {'next': None}}
                    else:
                        res = {'next': None}
    
                    # Technically some v3 paginated APIs return in 'data' but the caller checks the keys for this so
                    # always returning the cache under results is fine.
                    res['results'] = []
                    for result in path_cache['results']:
                        res['results'].append(result)
    
                else:
                    res = path_cache['results']
    
                return res
    
            elif not is_paginated_url:
                # The cache entry had expired or does not exist, start a new blank entry to be filled later.
                expires = datetime.datetime.utcnow()
                expires += datetime.timedelta(days=1)
                server_cache[url_info.path] = {
                    'expires': expires.strftime(iso_datetime_format),
                    'paginated': False,
                }
    
        headers = headers or {}
        self._add_auth_token(headers, url, required=auth_required)
    
        try:
            display.vvvv("Calling Galaxy at %s" % url)
>           resp = open_url(to_native(url), data=args, validate_certs=self.validate_certs, headers=headers,
                            method=method, timeout=20, http_agent=user_agent(), follow_redirects='safe')

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:379: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:1535: in open_url
    return Request().open(method, url, data=data, headers=headers, use_proxy=use_proxy,
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:1422: in open
    request = RequestWithMethod(url, method, data)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/urls.py:758: in __init__
    urllib_request.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:322: in __init__
    self.full_url = url
/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:348: in full_url
    self._parse()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.module_utils.urls.RequestWithMethod object at 0x7f0051a77250>

    def _parse(self):
        self.type, rest = _splittype(self._full_url)
        if self.type is None:
>           raise ValueError("unknown url type: %r" % self.full_url)
E           ValueError: unknown url type: 'invalid_url'

/opt/conda/envs/test4py_env/lib/python3.10/urllib/request.py:377: ValueError

During handling of the above exception, another exception occurred:

    def test_invalid_api_call():
        # Create a GalaxyAPI instance with valid parameters but an invalid URL
        api_client = GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', username='user123')
    
        # Call the _call_galaxy method with an invalid URL that should raise a URLError
        with pytest.raises(URLError) as excinfo:
>           api_client._call_galaxy('invalid_url')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py:35: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/api.py:157: in run_function
    return call_retryable_function()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <username123 "username123" @ https://specific-server.com with priority inf>
url = 'invalid_url', args = None, headers = {}, method = None
auth_required = False, error_context_msg = None, cache = False

    @retry_with_delays_and_condition(
        backoff_iterator=generate_jittered_backoff(retries=6, delay_base=2, delay_threshold=40),
        should_retry_error=is_rate_limit_exception
    )
    def _call_galaxy(self, url, args=None, headers=None, method=None, auth_required=False, error_context_msg=None,
                     cache=False):
        url_info = urlparse(url)
        cache_id = get_cache_id(url)
        query = parse_qs(url_info.query)
        if cache and self._cache:
            server_cache = self._cache.setdefault(cache_id, {})
            iso_datetime_format = '%Y-%m-%dT%H:%M:%SZ'
    
            valid = False
            if url_info.path in server_cache:
                expires = datetime.datetime.strptime(server_cache[url_info.path]['expires'], iso_datetime_format)
                valid = datetime.datetime.utcnow() < expires
    
            is_paginated_url = 'page' in query or 'offset' in query
            if valid and not is_paginated_url:
                # Got a hit on the cache and we aren't getting a paginated response
                path_cache = server_cache[url_info.path]
                if path_cache.get('paginated'):
                    if '/v3/' in url_info.path:
                        res = {'links': {'next': None}}
                    else:
                        res = {'next': None}
    
                    # Technically some v3 paginated APIs return in 'data' but the caller checks the keys for this so
                    # always returning the cache under results is fine.
                    res['results'] = []
                    for result in path_cache['results']:
                        res['results'].append(result)
    
                else:
                    res = path_cache['results']
    
                return res
    
            elif not is_paginated_url:
                # The cache entry had expired or does not exist, start a new blank entry to be filled later.
                expires = datetime.datetime.utcnow()
                expires += datetime.timedelta(days=1)
                server_cache[url_info.path] = {
                    'expires': expires.strftime(iso_datetime_format),
                    'paginated': False,
                }
    
        headers = headers or {}
        self._add_auth_token(headers, url, required=auth_required)
    
        try:
            display.vvvv("Calling Galaxy at %s" % url)
            resp = open_url(to_native(url), data=args, validate_certs=self.validate_certs, headers=headers,
                            method=method, timeout=20, http_agent=user_agent(), follow_redirects='safe')
        except HTTPError as e:
            raise GalaxyError(e, error_context_msg)
        except Exception as e:
>           raise AnsibleError("Unknown error when attempting to call Galaxy at '%s': %s" % (url, to_native(e)))
E           ansible.errors.AnsibleError: Unknown error when attempting to call Galaxy at 'invalid_url': unknown url type: 'invalid_url'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:384: AnsibleError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py::test_error_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py::test_valid_api_call
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI__call_galaxy_0.py::test_invalid_api_call
============================== 3 failed in 0.85s ===============================
"""