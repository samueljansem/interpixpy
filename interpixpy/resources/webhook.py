from interpixpy.config import RequestOptions
from interpixpy.core import PixPyBase


class Webhook(PixPyBase):
    def create(
        self,
        *,
        key: str,
        payload: dict,
        request_options: RequestOptions = None,
    ):
        return self._put(
            uri=f"/pix/v2/webhook/{key}",
            data=payload,
            request_options=request_options,
        )

    def find(self, *, key: str, request_options: RequestOptions = None):
        return self._get(
            uri=f"/pix/v2/webhook/{key}",
            request_options=request_options,
        )

    def delete(self, *, key: str, request_options: RequestOptions = None):
        return self._delete(
            uri=f"/pix/v2/webhook/{key}",
            request_options=request_options,
        )

    def callbacks(self, *, request_options: RequestOptions = None):
        return self._get(
            uri="/pix/v2/webhook/callbacks", request_options=request_options
        )
