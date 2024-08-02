from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser
from proxy.common.utils import tls_interception_enabled
import proxy
import sys


class RequestPlugin(HttpProxyBasePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def handle_client_request(self, request: HttpParser):
        print(f'Request _url: {request._url}')
        print(f'Request.method: {request.method}')
        print(f'Request protocol: {request.protocol}')
        print(f'Request host: {request.host}')
        print(f'Request path: {request.path}')

        print(f'Request properties: {vars(request)}')

        return request


if __name__ == '__main__':

    sys.argv += [
        '--ca-key-file', 'ca-key.pem',
        '--ca-cert-file', 'ca-cert.pem',
        '--ca-signing-key-file', 'ca-signing-key.pem',
    ]
    sys.argv += [
        '--hostname', '0.0.0.0',
        '--port', '8899',
        '--plugins', __name__ + '.RequestPlugin'
    ]

    proxy.main()