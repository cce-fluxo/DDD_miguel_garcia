from flask import Blueprint
from app.senhaesqueci.controllers import SenhaMail, SenhaNova
senhaesqueci_api = Blueprint('senhaesqueci_api',__name__)


senhaesqueci_api.add_url_rule(
         '/send_mail/reset', view_func = SenhaMail.as_view('mail_reset'), methods = ['POST'])

senhaesqueci_api.add_url_rule(
         '/reset/<string:token>', view_func = SenhaNova.as_view('reset'), methods = ['PATCH'])