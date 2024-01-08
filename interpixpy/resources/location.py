from interpixpy.config import RequestOptions
from interpixpy.core import PixPyBase


class Location(PixPyBase):
    def create(self, *, payload: dict, request_options: RequestOptions = None):
        return self._post(
            uri="/pix/v2/loc", data=payload, request_options=request_options
        )

    def all(self, *, params: dict, request_options: RequestOptions = None):
        return self._get(
            uri="/pix/v2/loc", params=params, request_options=request_options
        )

    def find(self, *, id: str, request_options: RequestOptions = None):
        return self._get(
            uri=f"/pix/v2/loc/{id}",
            request_options=request_options,
        )

    def unlink(self, *, id: str, request_options: RequestOptions = None):
        return self._delete(
            uri=f"/pix/v2/loc/{id}",
            request_options=request_options,
        )
