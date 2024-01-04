from interpixpy.core import PixPyBase


class Pix(PixPyBase):
    def all(self):
        return self._get("/pix/v2/pix")

    def find(self, e2eid):
        return self._get(f"/pix/v2/pix/{e2eid}")

    def update(self, txid, payload):
        return self._patch(f"/pix/v2/pix/{txid}", payload)

    def refund(self, e2eid, id, payload):
        return self._put(f"/pix/v2/pix/{e2eid}/devolucao/{id}", payload)

    def find_refund(self, e2eid, id):
        return self._get(f"/pix/v2/pix/{e2eid}/devolucao/{id}")
