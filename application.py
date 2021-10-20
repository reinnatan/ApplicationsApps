from flask import Flask, Blueprint
from flask_orator import Orator



app = Flask(__name__)

app.config['ORATOR_DATABASE'] = app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'sqlite',
        'database': './jobseeker.db'
    }
}

app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'
db = Orator(app)

def create_app():
    from applications.applicant.v1.delivery.http_handler import API_APPLICANTS
    from applications.company.v1.delivery.http_handler import API_COMPANY
    app.register_blueprint(API_APPLICANTS)
    app.register_blueprint(API_COMPANY)
    return app




