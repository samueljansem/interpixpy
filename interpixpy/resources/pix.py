from interpixpy.config import RequestOptions
from interpixpy.core import PixPyBase


class Pix(PixPyBase):
    def all(self, *, params: dict, request_options: RequestOptions = None):
        return self._get(
            uri="/pix/v2/pix",
            params=params,
            request_options=request_options,
        )

    def find(self, *, e2eid: str, request_options: RequestOptions = None):
        return self._get(
            uri=f"/pix/v2/pix/{e2eid}",
            request_options=request_options,
        )

    def update(
        self,
        *,
        txid: str,
        payload: dict,
        request_options: RequestOptions = None,
    ):
        return self._patch(
            uri=f"/pix/v2/pix/{txid}",
            data=payload,
            request_options=request_options,
        )

    def refund(
        self,
        *,
        e2eid: str,
        id: str,
        payload: dict,
        request_options: RequestOptions = None,
    ):
        return self._put(
            uri=f"/pix/v2/pix/{e2eid}/devolucao/{id}",
            data=payload,
            request_options=request_options,
        )

    def find_refund(
        self, *, e2eid: str, id: str, request_options: RequestOptions = None
    ):
        return self._get(
            uri=f"/pix/v2/pix/{e2eid}/devolucao/{id}",
            request_options=request_options,
        )
