import json, re

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from samplify import api_requestor


def camelcase_to_dashcase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


class SamplifyResource(object):
    @classmethod
    def get_api_base(cls):
        return None

    @classmethod
    def get_object_url(cls):
        if cls == SamplifyResource:
            raise NotImplementedError('SamplifyResource is an abstract class.')
        return '/%s/' % str(quote_plus(camelcase_to_dashcase(cls.__name__)))


class CreateableResource(SamplifyResource):
    @classmethod
    def create(cls, data, token=None):
        requestor = api_requestor.ApiRequestor(token=token)
        return json.loads(requestor.post(cls.get_object_url(), data).content)


class RetrieveableResource(SamplifyResource):
    @classmethod
    def get(cls, oid, token=None):
        url = "%s%s/" % (cls.get_object_url(), oid)
        requestor = api_requestor.ApiRequestor(token=token)
        return json.loads(requestor.get(url).content)


class ListableResource(SamplifyResource):
    @classmethod
    def list(cls, token=None):
        requestor = api_requestor.ApiRequestor(token=token)
        return json.loads(requestor.get(cls.get_object_url()).content)


class UpdateableResource(SamplifyResource):
    @classmethod
    def update(cls, oid, token=None, **params):
        url = "%s%s/" % (cls.get_object_url(), oid)
        requestor = api_requestor.ApiRequestor(token=token)
        return json.loads(requestor.put(url, params).content)


class Publications(CreateableResource,
                   UpdateableResource,
                   ListableResource,
                   RetrieveableResource):
    pass


class Watchlists(CreateableResource,
                 UpdateableResource,
                 ListableResource,
                 RetrieveableResource):
    pass


class SamWatchlists(CreateableResource,
                    UpdateableResource,
                    ListableResource,
                    RetrieveableResource):
    pass


class SlackUsers(RetrieveableResource):
    pass


class SlackTeams(RetrieveableResource):
    pass
