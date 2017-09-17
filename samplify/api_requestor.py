import requests
import samplify
import urlparse
from samplify import version


def build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))


class ApiRequestor(object):
    def __init__(self, token=None, api_base=None, api_version=None):
        self.api_base = api_base or samplify.api_base
        self.api_version = api_version or samplify.api_version
        self.token = token or samplify.token

    def get_api_base(self):
        return '%s/%s' % (self.api_base, self.api_version)

    def get_request_headers(self, token):
        user_agent = 'Samplify/%s PythonBindings/%s' % (self.api_version, version.VERSION,)
        headers = {
            'User-Agent': user_agent
        }

        if token is not None:
            headers['Authorization'] = 'Token %s' % (token,)

        if self.api_version is not None:
            headers['Samplify-Version'] = self.api_version

        return headers

    def get(self, path):
        return requests.get('%s%s' % (self.get_api_base(), path),
                            headers=self.get_request_headers(self.token))

    def post(self, path, data=None):
        return requests.post('%s%s' % (self.get_api_base(), path),
                             json=data,
                             headers=self.get_request_headers(self.token))

    def put(self, path, data=None):
        return requests.put('%s%s' % (self.get_api_base(), path),
                            json=data,
                            headers=self.get_request_headers(self.token))
