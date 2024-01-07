from datetime import datetime, timedelta

import requests

from interpixpy.config import Config


class AuthManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

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

        json_response = response.json()

        self.__token_type = json_response["token_type"]
        self.__access_token = json_response["access_token"]
        self.__expires_in = json_response["expires_in"]

        self.__expires_at = datetime.now() + timedelta(
            seconds=self.__expires_in,
        )

    def get_authorization(self) -> str:
        if self.__expires_at < datetime.now():
            self.authenticate()
        return f"{self.__token_type} {self.__access_token}"
