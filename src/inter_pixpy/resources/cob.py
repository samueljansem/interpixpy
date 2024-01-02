from inter_pixpy.core import PixPyBase


class Cob(PixPyBase):
    def all(self, request_options=None):
        return self._get("/cob", request_options)

    def find(self, txid, request_options=None):
        return self._get(f"/cob/{txid}", request_options)

    def create(self, payload, request_options=None):
        if "txid" in payload:
            return self._put("/cob", payload, request_options)

        return self._post("/cob", payload, request_options)

    def update(self, txid, payload, request_options=None):
        return self._patch(f"/cob/{txid}", payload, request_options)
