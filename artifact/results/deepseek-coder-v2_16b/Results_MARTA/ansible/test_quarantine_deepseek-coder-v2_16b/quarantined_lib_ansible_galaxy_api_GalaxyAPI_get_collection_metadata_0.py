
import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture(scope="module")
def api_client():
    return GalaxyAPI('default_galaxy', 'default_name', 'https://api.ansiblegalaxy.com')



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_get_collection_metadata_success _____________________

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f8779d2a6e0>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f8779ed2bc0>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f8779d2a890>
http_conn_args = {}, host = 'api.ansiblegalaxy.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f8779d2ac80>

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

host = 'api.ansiblegalaxy.com', port = 443, family = 0
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

self = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>
url = 'https://api.ansiblegalaxy.com', args = None, headers = {}, method = 'GET'
auth_required = False
error_context_msg = 'Error when finding available api versions from default_name (https://api.ansiblegalaxy.com)'
cache = True

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

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f8779d2a6e0>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f8779ed2bc0>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f8779d2a890>
http_conn_args = {}, host = 'api.ansiblegalaxy.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f8779d2ac80>

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

self = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>
args = ('namespace', 'name'), kwargs = {}
n_url = 'https://api.ansiblegalaxy.com/api'
error_context_msg = 'Error when finding available api versions from default_name (https://api.ansiblegalaxy.com)'

    def wrapped(self, *args, **kwargs):
        if not self._available_api_versions:
            display.vvvv("Initial connection to galaxy_server: %s" % self.api_server)
    
            # Determine the type of Galaxy server we are talking to. First try it unauthenticated then with Bearer
            # auth for Automation Hub.
            n_url = self.api_server
            error_context_msg = 'Error when finding available api versions from %s (%s)' % (self.name, n_url)
    
            if self.api_server == 'https://galaxy.ansible.com' or self.api_server == 'https://galaxy.ansible.com/':
                n_url = 'https://galaxy.ansible.com/api/'
    
            try:
>               data = self._call_galaxy(n_url, method='GET', error_context_msg=error_context_msg, cache=True)

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/api.py:157: in run_function
    return call_retryable_function()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>
url = 'https://api.ansiblegalaxy.com', args = None, headers = {}, method = 'GET'
auth_required = False
error_context_msg = 'Error when finding available api versions from default_name (https://api.ansiblegalaxy.com)'
cache = True

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
E           ansible.errors.AnsibleError: Unknown error when attempting to call Galaxy at 'https://api.ansiblegalaxy.com': <urlopen error [Errno -2] Name or service not known>

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:384: AnsibleError

During handling of the above exception, another exception occurred:

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f8779d2ab00>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f8779d58640>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f8779d2ae30>
http_conn_args = {}, host = 'api.ansiblegalaxy.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f8779d2b010>

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

host = 'api.ansiblegalaxy.com', port = 443, family = 0
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

self = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>
url = 'https://api.ansiblegalaxy.com/api', args = None, headers = {}
method = 'GET', auth_required = False
error_context_msg = 'Error when finding available api versions from default_name (https://api.ansiblegalaxy.com)'
cache = True

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

self = <ansible.module_utils.urls.CustomHTTPSHandler object at 0x7f8779d2ab00>
http_class = functools.partial(<class 'ansible.module_utils.urls.CustomHTTPSConnection'>, context=<ssl.SSLContext object at 0x7f8779d58640>)
req = <ansible.module_utils.urls.RequestWithMethod object at 0x7f8779d2ae30>
http_conn_args = {}, host = 'api.ansiblegalaxy.com'
h = <ansible.module_utils.urls.CustomHTTPSConnection object at 0x7f8779d2b010>

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

api_client = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>

    def test_get_collection_metadata_success(api_client):
>       metadata = api_client.get_collection_metadata('namespace', 'name')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:94: in wrapped
    data = self._call_galaxy(n_url, method='GET', error_context_msg=error_context_msg, cache=True)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/api.py:157: in run_function
    return call_retryable_function()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>
url = 'https://api.ansiblegalaxy.com/api', args = None, headers = {}
method = 'GET', auth_required = False
error_context_msg = 'Error when finding available api versions from default_name (https://api.ansiblegalaxy.com)'
cache = True

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
E           ansible.errors.AnsibleError: Unknown error when attempting to call Galaxy at 'https://api.ansiblegalaxy.com/api': <urlopen error [Errno -2] Name or service not known>

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/galaxy/api.py:384: AnsibleError
________________ test_get_collection_metadata_invalid_namespace ________________

api_client = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>

    def test_get_collection_metadata_invalid_namespace(api_client):
>       with pytest.raises(GalaxyError) as excinfo:
E       NameError: name 'GalaxyError' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py:16: NameError
__________________ test_get_collection_metadata_invalid_name ___________________

api_client = <default_name "default_name" @ https://api.ansiblegalaxy.com with priority inf>

    def test_get_collection_metadata_invalid_name(api_client):
>       with pytest.raises(GalaxyError) as excinfo:
E       NameError: name 'GalaxyError' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py:21: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py::test_get_collection_metadata_success
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py::test_get_collection_metadata_invalid_namespace
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_galaxy_api_GalaxyAPI_get_collection_metadata_0.py::test_get_collection_metadata_invalid_name
============================== 3 failed in 0.91s ===============================
"""