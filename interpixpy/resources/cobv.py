from interpixpy.config import RequestOptions
from interpixpy.core import PixPyBase


class Cobv(PixPyBase):
    def all(
        self,
        *,
        params: dict,
        request_options: RequestOptions = None,
    ):
        return self._get(
            uri="/pix/v2/cobv", params=params, request_options=request_options
        )

    def find(self, *, txid: str, request_options: RequestOptions = None):
        return self._get(
            uri=f"/pix/v2/cobv/{txid}",
            request_options=request_options,
        )

    def create(self, *, payload: dict, request_options: RequestOptions = None):
        if "txid" in payload:
            return self._put(
                uri="/pix/v2/cobv",
                data=payload,
                request_options=request_options,
            )

        return self._post(
            uri="/pix/v2/cobv", data=payload, request_options=request_options
        )

    def update(
        self,
        *,
        txid: str,
        payload: dict,
        request_options: RequestOptions = None,
    ):
        return self._patch(
            uri=f"/pix/v2/cobv/{txid}",
            data=payload,
            request_options=request_options,
        )
