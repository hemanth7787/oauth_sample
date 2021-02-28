from django.conf import settings
import requests


class ApiBase():
    """
    Base class for all API access from resource servers
    """
    def __init__(self, token=None):
        self.token = token
        self.API_HOST = settings.R2_API_BASEURL

    def call(self, method, url, data={}):
        headers = {'Authorization': f'Bearer {self.token}'}
        url = self.API_HOST + url,
        return requests.request(method, url, headers=headers, data=data).json()


class R2Api(ApiBase):
    """
    API operation supported on R2 resource server
     ``token`` should be supplied
    """
    def user_list(self):
        """
        List users
        """
        url = "/o/users/"
        return self.call("GET", url)

    def user_create(self, data):
        url = "/o/users/"
        return self.call("POST", url, data)

    def user_detail(self, user_id):
        url = f"/o/users/{user_id}/"
        return self.call("POST", url)

    def group_list(self):
        url = "/o/groups/"
        return self.call("GET", url)
