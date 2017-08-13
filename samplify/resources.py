import urllib
from samplify import api_requestor


class SamplifyResource(object):
    @classmethod
    def get_api_base(cls):
        return None

    @classmethod
    def get_object_url(cls):
        if cls == SamplifyResource:
            raise NotImplementedError('SamplifyResource is an abstract class.')
        return str(urllib.quote_plus(cls.__name__.lower()))

    @classmethod
    def post(cls, data, token=None):
        requestor = api_requestor.ApiRequestor(token=token)
        return requestor.post(cls.get_object_url(), data)


class CreateableResource(SamplifyResource):
    @classmethod
    def create(cls, data, token=None):
        requestor = api_requestor.ApiRequestor(token=token)
        return requestor.post(cls.get_object_url(), data)


class Publication(CreateableResource):
    pass
