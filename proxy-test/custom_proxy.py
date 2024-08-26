from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser
from proxy.common.utils import tls_interception_enabled
import proxy
import sys
from pprint import pprint


class OntologyTimeMachinePlugin(HttpProxyBasePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def do_intercept(self, _request: HttpParser) -> bool: 
        """By default returns True (only) when necessary flags 
        for TLS interception are passed. 

        When TLS interception is enabled, plugins can still disable 
        TLS interception by returning False explicitly.  This hook 
        will allow you to run proxy instance with TLS interception 
        flags BUT only conditionally enable interception for 
        certain requests. 
        """ 

        print(f'Do intercept triggered: {vars(_request)}')
#        if _request._is_https_tunnel:
#            return False
        if _request.host == b'example.org':
            return True
        if _request.host == b'www.example.org':
            return False
        else: 
            return True


if __name__ == '__main__':

    sys.argv += [
        '--ca-key-file', 'ca-key.pem',
        '--ca-cert-file', 'ca-cert.pem',
        '--ca-signing-key-file', 'ca-signing-key.pem',
    ]
    sys.argv += [
        '--hostname', '0.0.0.0',
        '--port', '8899',
        '--log-level', 'e',
#        '--basic-auth', 'user:pass',
        '--plugins', __name__ + '.OntologyTimeMachinePlugin'
    ]

    proxy.main()
