from datetime import datetime, timedelta

import requests

from inter_pixpy_samueljansem.config.config import Config


class AuthManager:
    __client_id = None
    __client_secret = None
    __grant_type = "client_credentials"
    __scope = [
        "cob.read",
        "cob.write",
        "cobv.read",
        "cobv.write",
        "pix.read",
        "pix.write",
        "webhook.read",
        "webhook.write",
    ].join(" ")
    __access_token = None
    __token_type = None
    __token_expiration_date = None
    __config = None

    def __init__(self, client_id, client_secret, grant_type, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.scope = scope
        self.token_expiration_date = datetime.now()
        self.config = Config()

    def authenticate(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type,
            "scope": self.scope,
        }
        response = requests.post(
            url=f"{self.config.api_base_url}/oauth/v2/token",
            data=data,
            headers={"Content-Type": self.config.mime_form},
        )
        response.raise_for_status()
        response_data = response.json()
        self.access_token = response_data["access_token"]
        self.token_type = response_data["token_type"]
        self.token_expiration_date = datetime.now() + timedelta(
            seconds=response_data["expires_in"]
        )
        self.scope = response_data["scope"]

    def is_token_expired(self):
        return datetime.now() > self.token_expiration_date

    def get_access_token(self):
        if self.is_token_expired():
            self.authenticate()
        return self.access_token

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
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

    @property
    def token_type(self):
        return self.__token_type

    @token_type.setter
    def token_type(self, value):
        self.__token_type = value

    @property
    def token_expiration_date(self):
        return self.__token_expiration_date

    @token_expiration_date.setter
    def token_expiration_date(self, value):
        self.__token_expiration_date = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        if value is not None and not isinstance(value, Config):
            raise TypeError(
                "config must be a Config instance",
            )
        self.__config = value
