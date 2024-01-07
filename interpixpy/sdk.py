from interpixpy.config import RequestOptions
from interpixpy.core import AuthManager
from interpixpy.http import HttpClient
from interpixpy.resources import Cob, Cobv, Pix, Webhook


class SDK:
    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        scope: str,
        cert_path: str,
        key_path: str,
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

    def cob(self, *, request_options: RequestOptions = None) -> Cob:
        return Cob(
            request_options=request_options or self.__request_options,
            http_client=self.__http_client,
        )

    def cobv(self, *, request_options: RequestOptions = None) -> Cobv:
        return Cobv(
            request_options=request_options or self.__request_options,
            http_client=self.__http_client,
        )

    def pix(self, *, request_options: RequestOptions = None) -> Pix:
        return Pix(
            request_options=request_options or self.__request_options,
            http_client=self.__http_client,
        )

    def webhook(self, *, request_options: RequestOptions = None) -> Webhook:
        return Webhook(
            request_options=request_options or self.__request_options,
            http_client=self.__http_client,
        )
