from inter_pixpy_samueljansem.core.pixpy_base import PixPyBase


class Pix(PixPyBase):
    def all(self):
        return self._get("/pix")

    def find(self, e2eid):
        return self._get(f"/pix/{e2eid}")

    def update(self, txid, payload):
        return self._patch(f"/pix/{txid}", payload)

    def refund(self, e2eid, id, payload):
        return self._put(f"/pix/{e2eid}/devolucao/{id}", payload)

    def find_refund(self, e2eid, id):
        return self._get(f"/pix/{e2eid}/devolucao/{id}")
