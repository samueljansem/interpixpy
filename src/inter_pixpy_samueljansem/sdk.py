from inter_pixpy_samueljansem.config.request_options import RequestOptions
from inter_pixpy_samueljansem.http.http_client import HttpClient
from inter_pixpy_samueljansem.resources import Cob, Cobv
from inter_pixpy_samueljansem.resources.pix import Pix
from inter_pixpy_samueljansem.resources.webhook import Webhook


class SDK:
    def __init__(self, request_options=None, http_client=None):
        if http_client is not None and not isinstance(http_client, HttpClient):
            raise TypeError(
                "http_client must be a HttpClient instance",
            )
        if request_options is not None and not isinstance(
            request_options, RequestOptions
        ):
            raise TypeError(
                "request_options must be a RequestOptions instance",
            )

        self.http_client = http_client or HttpClient()
        self.request_options = request_options or RequestOptions()

    def cob(self, request_options=None):
        return Cob(request_options or self.request_options, self.http_client)

    def cobv(self, request_options=None):
        return Cobv(request_options or self.request_options, self.http_client)

    def pix(self, request_options=None):
        return Pix(request_options or self.request_options, self.http_client)

    def webhook(self, request_options=None):
        return Webhook(request_options or self.request_options, self.http_client)

    @property
    def request_options(self):
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if value is not None and not isinstance(value, RequestOptions):
            raise TypeError(
                "request_options must be a RequestOptions instance",
            )
        self.__request_options = value

    @property
    def http_client(self):
        return self.__http_client

    @http_client.setter
    def http_client(self, value):
        if value is not None and not isinstance(value, HttpClient):
            raise TypeError(
                "http_client must be a HttpClient instance",
            )
        self.__http_client = value
