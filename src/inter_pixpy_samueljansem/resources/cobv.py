from inter_pixpy_samueljansem.core.pixpy_base import PixPyBase


class Cobv(PixPyBase):
    def all(self):
        return self._get("/cobv")

    def find(self, txid):
        return self._get(f"/cobv/{txid}")

    def create(self, payload):
        if "txid" in payload:
            return self._put("/cobv", payload)

        return self._post("/cobv", payload)

    def update(self, txid, payload):
        return self._patch(f"/cobv/{txid}", payload)
