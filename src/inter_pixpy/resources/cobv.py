from inter_pixpy.core import PixPyBase


class Cobv(PixPyBase):
    def all(self):
        return self._get("/pix/v2/cobv")

    def find(self, txid):
        return self._get(f"/pix/v2/cobv/{txid}")

    def create(self, payload):
        if "txid" in payload:
            return self._put("/pix/v2/cobv", payload)

        return self._post("/pix/v2/cobv", payload)

    def update(self, txid, payload):
        return self._patch(f"/pix/v2/cobv/{txid}", payload)
