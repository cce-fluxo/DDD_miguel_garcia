from flask.views import MethodView
from app.storage import storage
import uuid

class FileStorage(MethodView):
    def get (self, formato):
        file_key = f'{uuid.uuid4().hex}.{formato}'

        url = storage.put_url(file_key=file_key)

        return {'url': url,
                'nome': file_key}, 201