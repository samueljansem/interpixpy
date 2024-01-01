from inter_pixpy_samueljansem.config import Config
from inter_pixpy_samueljansem.core import AuthManager


class RequestOptions:
    __client_id = None
    __client_secret = None
    __grant_type = None
    __scope = None
    __conta_corrente = None
    __custom_headers = None
    __auth_manager = None

    def __init__(
        self,
        client_id=None,
        client_secret=None,
        grant_type=None,
        scope=None,
        conta_corrente=None,
        custom_headers=None,
    ):
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if grant_type is not None:
            self.grant_type = grant_type
        if scope is not None:
            self.scope = scope
        if conta_corrente is not None:
            self.conta_corrente = conta_corrente
        if custom_headers is not None:
            self.custom_headers = custom_headers

        self.config = Config()
        self.__auth_manager = AuthManager(
            self.client_id, self.client_secret, self.grant_type, self.scope
        )

    def get_headers(self):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "User-Agent": self.config.user_agent,
            "Accept": self.config.mime_json,
        }

        if self.conta_corrente is not None:
            headers["X-Conta-Corrente"] = self.conta_corrente

        if self.custom_headers is not None:
            headers.update(self.custom_headers)

        return headers

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value):
        self.__client_secret = value

    @property
    def grant_type(self):
        return self.__grant_type

    @grant_type.setter
    def grant_type(self, value):
        self.__grant_type = value

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        self.__scope = value

    @property
    def conta_corrente(self):
        return self.__conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, value):
        self.__conta_corrente = value

    @property
    def custom_headers(self):
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        if not isinstance(value, dict):
            raise TypeError("custom_headers must be a dict")
        self.__custom_headers = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        if not isinstance(value, Config):
            raise TypeError("config must be a Config instance")
        self.__config = value

    @property
    def access_token(self):
        return self.__auth_manager.get_access_token()
