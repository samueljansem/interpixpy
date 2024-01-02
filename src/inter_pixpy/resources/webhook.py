from inter_pixpy.core import PixPyBase


class Webhook(PixPyBase):
    def create(self, key, payload):
        return self._put(f"/pix/v2/webhook/{key}", payload)

    def find(self, key):
        return self._get(f"/pix/v2/webhook/{key}")

    def delete(self, key):
        return self._delete(f"/pix/v2/webhook/{key}")

    def callbacks(self):
        return self._get("/pix/v2/webhook/callbacks")
