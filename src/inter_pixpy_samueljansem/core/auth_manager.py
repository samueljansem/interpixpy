import datetime

import requests

from inter_pixpy_samueljansem.config import Config


class AuthManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(
        self, client_id, client_secret, grant_type, scope, cert_path, key_path
    ):
        if not self.initialized:
            self.client_id = client_id
            self.client_secret = client_secret
            self.grant_type = grant_type
            self.scope = scope
            self.cert_path = cert_path
            self.key_path = key_path
            self.__token_type = None
            self.__access_token = None
            self.__expires_in = None
            self.__expires_at = datetime.now()
            self.__config = Config()
            self.initialized = True

    def authenticate(self):
        url = f"{self.__config.api_base_url}/oauth/v2/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type,
            "scope": self.scope,
        }
        headers = {
            "Content-Type": self.__config.mime_form,
            "Accept": self.__config.mime_json,
        }
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            cert=(
                self.cert_path,
                self.key_path,
            ),
        )
        response.raise_for_status()
        response = response.json()

        self.__token_type = response["token_type"]
        self.__access_token = response["access_token"]
        self.__expires_in = response["expires_in"]

        self.__expires_at = datetime.now() + datetime.timedelta(
            seconds=self.__expires_in,
        )

    def get_authorization(self):
        if self.__expires_at < datetime.now():
            self.authenticate()
        return f"{self.__token_type} {self.__access_token}"
