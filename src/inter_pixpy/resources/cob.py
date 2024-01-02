from inter_pixpy.core import PixPyBase


class Cob(PixPyBase):
    def all(self, request_options=None):
        return self._get("/pix/v2/cob", request_options)

    def find(self, txid, request_options=None):
        return self._get(f"/pix/v2/cob/{txid}", request_options)

    def create(self, payload, request_options=None):
        if "txid" in payload:
            return self._put("/pix/v2/cob", payload, request_options)

        return self._post("/pix/v2/cob", payload, request_options)

    def update(self, txid, payload, request_options=None):
        return self._patch(f"/pix/v2/cob/{txid}", payload, request_options)
