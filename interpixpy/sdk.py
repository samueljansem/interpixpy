from interpixpy.config import RequestOptions
from interpixpy.core import AuthManager
from interpixpy.http import HttpClient
from interpixpy.resources import Cob, Cobv, Pix, Webhook


class SDK:
    def __init__(
        self,
        client_id,
        client_secret,
        grant_type,
        scope,
        cert_path,
        key_path,
    ):
        self.__auth_manager = AuthManager(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            cert_path=cert_path,
            key_path=key_path,
        )
        self.__http_client = HttpClient(
            auth_manager=self.__auth_manager,
            cert_path=cert_path,
            key_path=key_path,
        )
        self.__request_options = RequestOptions()

    def cob(self, request_options=None):
        return Cob(
            request_options or self.__request_options,
            self.__http_client,
        )

    def cobv(self, request_options=None):
        return Cobv(
            request_options or self.__request_options,
            self.__http_client,
        )

    def pix(self, request_options=None):
        return Pix(
            request_options or self.__request_options,
            self.__http_client,
        )

    def webhook(self, request_options=None):
        return Webhook(
            request_options or self.__request_options,
            self.__http_client,
        )
