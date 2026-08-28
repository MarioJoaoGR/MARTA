
import pytest
from tornado.auth import OpenIdMixin
from tornado.web import RequestHandler, Application

class TestGetAxArg(object):
    def setup_method(self):
        self.ax_ns = "ax"
        class MyRequestHandler(OpenIdMixin, RequestHandler):
            def get(self):
                uri = self.get_argument('uri')
                result = get_ax_arg(uri)
                self.write(result)
        
        self.app = Application([('/myhandler', MyRequestHandler)])
    
    @pytest.mark.parametrize("uri, expected", [
        ('example@example.com', 'openid.ax.value.email'),
        ('unknown@example.com', '')
    ])
    def test_get_ax_arg(self, uri, expected):
        with pytest.raises(Exception) as e_info:
            response = self.app.fetch('/myhandler?uri={}'.format(uri))
            assert response.body.decode() == expected
