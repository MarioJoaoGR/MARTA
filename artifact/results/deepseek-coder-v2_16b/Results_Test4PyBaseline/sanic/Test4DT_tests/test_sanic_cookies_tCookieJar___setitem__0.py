# Module: sanic.cookies
import pytest
from sanic import Sanic
from sanic.cookiesclass import CookieJar

# Fixture to create a new instance of the app for each test
@pytest.fixture
def app():
    return Sanic("MyApp")

# Test case to initialize a CookieJar with headers from the request
def test_initialize_cookiejar(app):
    @app.route('/set-cookie')
    async def set_cookie(request):
        cookie_jar = CookieJar(request.headers)
        assert "Set-Cookie" in cookie_jar.headers
        return response.json({}, headers=cookie_jar.headers)
    
    request, client = app.test_client('/set-cookie')
    _, response = client.get("/set-cookie")
    assert response.status == 200
    assert "Set-Cookie" in response.headers

# Test case to add a new cookie to the CookieJar
def test_add_cookie(app):
    @app.route('/add-cookie')
    async def add_cookie(request):
        cookie_jar = CookieJar(request.headers)
        cookie_jar.add_cookie('user', 'user_data')
        assert "Set-Cookie" in cookie_jar.headers
        return response.json({}, headers=cookie_jar.headers)
    
    request, client = app.test_client('/add-cookie')
    _, response = client.get("/add-cookie")
    assert response.status == 200
    assert "Set-Cookie" in response.headers
    assert response.headers["Set-Cookie"] == 'user=user_data; path=/'

# Test case to remove an existing cookie from the CookieJar
def test_remove_cookie(app):
    @app.route('/remove-cookie')
    async def remove_cookie(request):
        headers = {'Set-Cookie': 'user=user_data; path=/'}
        cookie_jar = CookieJar(headers)
        cookie_jar.remove_cookie('user')
        assert "Set-Cookie" not in cookie_jar.headers
        return response.json({}, headers=cookie_jar.headers)
    
    request, client = app.test_client('/remove-cookie')
    _, response = client.get("/remove-cookie")
    assert response.status == 200
    assert "Set-Cookie" not in response.headers
