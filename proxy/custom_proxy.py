from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser
import proxy
import sys


class OntologyTimeMachinePlugin(HttpProxyBasePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.https_intercept = False


    def before_upstream_connection(self, request: HttpParser):
        if request.method == b'CONNECT':
            # Only intercept if interception is enabled
            if self.https_intercept:
                return request
            else:
                return None

        return request
    

    def handle_upstream_chunk(self, chunk: memoryview):
        return chunk


if __name__ == '__main__':

    sys.argv += [
        '--ca-key-file', 'ca-key.pem',
        '--ca-cert-file', 'ca-cert.pem',
        '--ca-signing-key-file', 'ca-signing-key.pem',
    ]
    sys.argv += [
        '--hostname', '0.0.0.0',
        '--port', '8899',
        '--plugins', __name__ + '.OntologyTimeMachinePlugin'
    ]

    proxy.main()