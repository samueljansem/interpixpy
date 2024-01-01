from inter_pixpy_samueljansem.core.pixpy_base import PixPyBase


class Webhook(PixPyBase):
    def create(self, key, payload):
        return self._put(f"/webhook/{key}", payload)

    def find(self, key):
        return self._get(f"/webhook/{key}")

    def delete(self, key):
        return self._delete(f"/webhook/{key}")

    def callbacks(self):
        return self._get("/webhook/callbacks")
