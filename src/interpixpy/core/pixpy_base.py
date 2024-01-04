from json.encoder import JSONEncoder

from interpixpy.config.config import Config
from interpixpy.config.request_options import RequestOptions
from interpixpy.http.http_client import HttpClient


class PixPyBase:
    def __init__(self, request_options, http_client):
        if not isinstance(request_options, RequestOptions):
            raise TypeError(
                "request_options must be a RequestOptions instance",
            )

        if not isinstance(http_client, HttpClient):
            raise TypeError(
                "http_client must be a HttpClient instance",
            )

        self.__request_options = request_options
        self.__http_client = http_client
        self.__config = Config()

    def __check_request_options(self, request_options):
        if request_options is not None and not isinstance(
            request_options,
            RequestOptions,
        ):
            raise TypeError(
                "request_options must be a RequestOptions instance",
            )

        if request_options is None:
            request_options = self.request_options

        return request_options

    def __check_headers(self, request_options, extra_header=None):
        headers = self.request_options.get_headers()

        if request_options is not None:
            headers = request_options.get_headers()

        if extra_header is not None:
            headers.update(extra_header)

        return headers

    def _get(self, uri, params, request_options=None):
        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options)

        return self.http_client.get(
            url=self.config.api_base_url + uri,
            params=params,
            headers=headers,
            timeout=request_options.connection_timeout,
            max_retries=request_options.max_retries,
        )

    def _post(self, uri, data=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-Type": self.config.mime_json}
        )

        return self.http_client.post(
            url=self.config.api_base_url + uri,
            data=data,
            headers=headers,
            timeout=request_options.connection_timeout,
            max_retries=request_options.max_retries,
        )

    def _patch(self, uri, data=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-Type": self.config.mime_json}
        )

        return self.http_client.patch(
            url=self.config.api_base_url + uri,
            data=data,
            headers=headers,
            timeout=request_options.connection_timeout,
            max_retries=request_options.max_retries,
        )

    def _put(self, uri, data=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(
            request_options, {"Content-Type": self.config.mime_json}
        )

        return self.http_client.put(
            url=self.config.api_base_url + uri,
            data=data,
            headers=headers,
            timeout=request_options.connection_timeout,
            max_retries=request_options.max_retries,
        )

    def _delete(self, uri, request_options=None):
        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options)

        return self.http_client.delete(
            url=self.config.api_base_url + uri,
            headers=headers,
            timeout=request_options.connection_timeout,
            max_retries=request_options.max_retries,
        )

    @property
    def request_options(self):
        return self.__request_options

    @property
    def config(self):
        return self.__config

    @property
    def http_client(self):
        return self.__http_client
