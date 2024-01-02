from inter_pixpy.config import Config


class RequestOptions:
    __conta_corrente = None
    __custom_headers = None
    __connection_timeout = None
    __max_retries = None

    def __init__(
        self,
        conta_corrente=None,
        connection_timeout=60,
        max_retries=3,
        custom_headers=None,
    ):
        if conta_corrente is not None:
            self.conta_corrente = conta_corrente
        if custom_headers is not None:
            self.custom_headers = custom_headers
        self.connection_timeout = connection_timeout
        self.max_retries = max_retries

        self.config = Config()

    def get_headers(self):
        headers = {
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
    def connection_timeout(self):
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        if not isinstance(value, int):
            raise TypeError("connection_timeout must be a int")
        self.__connection_timeout = value

    @property
    def max_retries(self):
        return self.__max_retries

    @max_retries.setter
    def max_retries(self, value):
        if not isinstance(value, int):
            raise TypeError("max_retries must be a int")
        self.__max_retries = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        if not isinstance(value, Config):
            raise TypeError("config must be a Config instance")
        self.__config = value
