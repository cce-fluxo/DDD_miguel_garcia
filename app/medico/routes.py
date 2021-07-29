from app.medico.controllers import MedicosCreate, MedicosDetails, MedicoLogin
from flask import Blueprint




medico_api = Blueprint ('medico_api', __name__)

medico_api.add_url_rule(

    '/medico/create', view_func=MedicosCreate.as_view('medico_create'), methods = ['GET', 'POST']

)
medico_api.add_url_rule(

    '/medico/details/<int:id>', view_func=MedicosDetails.as_view('medico_details'), methods = ['GET', 'PUT', 'PATCH', 'DELETE']

)
medico_api.add_url_rule(

    '/medico/login', view_func=MedicoLogin.as_view('medico_login'), methods = ['POST']

)