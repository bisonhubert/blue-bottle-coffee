import json
import requests

from ..constants import BASE_URL, LANGUAGE_CODE_JPN, LANGUAGE_CODE_US

class Client(object):

    def __init__(self, **kwargs):
        self.server = BASE_URL.strip('/')
        self.model = kwargs.get('model')

    def _url(self):
        url = "{}/{}.json".format(self.server, self.model)
        return url

    def get_response(self):
        response = requests.get(self._url())
        if response.ok:
            return response
        return None # TODO (Bison): return customer exception

    def get_content(self):
        response = self.get_response()
        if response:
            return json.loads(self.get_response().content)
        return None # TODO (Bison): return customer exception


class CountryClient(Client):

    def __init__(self, **kwargs):
        self.server = BASE_URL.strip('/')
        self.model = kwargs.get('model')
        self.language_code = kwargs.get('language_code')

    def _url(self):
        url = "{}/{}/{}.json".format(self.server, self.language_code, self.model)
        return url
