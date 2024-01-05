from uuid import uuid4

class ServiceMixin:

    @staticmethod
    def generate_id(prefix: str = "misc") -> str:
        uid = str(uuid4()).replace('-','')
        return prefix + "_" + uid
