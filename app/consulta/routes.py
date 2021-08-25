from flask import Blueprint
from app.consulta.controllers import ConsultaGet,ConsultaPost
consulta_api = Blueprint('consulta_api',__name__)

#rotas dos consultas
consulta_api.add_url_rule(
         '/consulta', view_func = ConsultaGet.as_view('consulta_get'), methods = ['GET'])

consulta_api.add_url_rule(
         '/consulta', view_func = ConsultaPost.as_view('consulta_create'), methods = ['POST'])