from flask import Blueprint
from app.storage.controllers import FileStorage

storage_api = Blueprint('storage_api',__name__)

storage_api.add_url_rule(
    '/storage/put_url/<string:formato>', 
    view_func=FileStorage.as_view('storage'), 
    methods=['GET'])