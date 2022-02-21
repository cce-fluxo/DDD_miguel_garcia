from flask import Blueprint
from app.storages.controllers import FileStorage

storage_api = Blueprint('storage_api',__name__)

storage_api.add_url_rule(
    '/storage/put_url/<string:formato>', 
    view_func=FileStorage.as_view('put_url'), 
    methods=['GET'])