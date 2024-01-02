import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class HttpClient:
    def __init__(self, auth_manager):
        self.__auth_manager = auth_manager

    def request(self, method, url, max_retries=None, **kwargs):
        headers = kwargs.get("headers", {})
        headers["Authorization"] = self.__auth_manager.get_authorization()
        kwargs["headers"] = headers
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        http = requests.Session()
        http.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        with http as session:
            results = session.request(method, url, **kwargs)
            response = {
                "status_code": results.status_code,
                "results": results.json(),
            }

        return response

    def get(
        self,
        url,
        headers,
        data=None,
        params=None,
        timeout=None,
        max_retries=None,
    ):
        return self.request(
            method="GET",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            max_retries=max_retries,
        )

    def post(
        self,
        url,
        headers,
        data=None,
        params=None,
        timeout=None,
        max_retries=None,
    ):
        return self.request(
            method="POST",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            max_retries=max_retries,
        )

    def put(
        self,
        url,
        headers,
        data=None,
        params=None,
        timeout=None,
        max_retries=None,
    ):
        return self.request(
            method="PUT",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            max_retries=max_retries,
        )

    def delete(
        self,
        url,
        headers,
        data=None,
        params=None,
        timeout=None,
        max_retries=None,
    ):
        return self.request(
            method="DELETE",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            max_retries=max_retries,
        )
