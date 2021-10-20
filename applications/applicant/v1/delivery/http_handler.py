import jwt
from flask import jsonify, Blueprint, request
from flask_expects_json import expects_json

from application import app
from applications.applicant.v1.domain.applicant_request_object import ApplicantRequestObject
from applications.applicant.v1.models.applicants import Applicants
from applications.applicant.v1.models.applications import Applications
from applications.applicant.v1.schemas.schema_applicants import schema_create_applicant, schema_create_applicantions
from applications.company.v1.domain.jobs_request_object import JobsRequestObject
from applications.company.v1.model.jobs import Jobs
from applications.company.v1.schemas.schema_company import schema_login_company

API_APPLICANTS = Blueprint('/v1/applicants', __name__, url_prefix='/v1/applicants')

@API_APPLICANTS.route('/sign-up', methods = ['POST'])
@expects_json(schema_create_applicant)
def sign_up():
    request_object = ApplicantRequestObject.from_dict(request.json)
    applicant = Applicants.create(
        name=request_object.name,
        email=request_object.email,
        password=request_object.password,
        address=request_object.address,
        phone=request_object.phone,
        token="",
        expired_token=""
    )

    is_saved = applicant.save()
    if is_saved:
        return jsonify(message='Succcess', response=200)
    else:
        return jsonify(message='Failed', response=200)

@API_APPLICANTS.route('/login', methods = ['POST'])
@expects_json(schema_login_company)
def login():
    import datetime
    request_object = ApplicantRequestObject.from_dict(request.json)
    applicants = Applicants.where_raw('email=? and password=?', [request_object.email, request_object.password]).first()
    exp_token_date = datetime.datetime.now() + datetime.timedelta(minutes=15)

    if applicants:
        jwt_token = jwt.encode({"id": str(applicants.id), "expired_token": str(exp_token_date), "login_as":'applicant'}, app.config['SECRET_KEY'],
                               algorithm="HS256")
        applicants.expired_token = exp_token_date
        applicants.token = jwt_token
        applicants.save()
        return jsonify(token=jwt_token, response=200)
    return jsonify(message='Failed, user not found', response=404)

@API_APPLICANTS.route('/jobs-detail/<id_jobs>', methods = ['GET'])
def jobs_detail(id_jobs):
    job = Jobs.find(id_jobs)
    if job:
        jobs_response = JobsRequestObject.to_object(job)
        return jsonify(message='Succcess', data=jobs_response, response=200)
    return jsonify(message='Jobs id not found', response=400)

@API_APPLICANTS.route('/apply-applications/<id_applicants>', methods = ['PUT'])
@expects_json(schema_create_applicantions)
def apply_applications(id_applicants):
    try:
        applicants_id = int(id_applicants)
        jobs_id = int(request.json["jobsId"])
    except Exception:
        return jsonify(message='Failed', response=400)

    applications = Applications.where_raw('applicants_id=? and jobs_id=?', [applicants_id,  jobs_id]).first()
    if applications is None:
        create_applications = Applications.create(
            applicants_id=applicants_id,
            jobs_id=jobs_id,
            status='Applied'
        )
        is_save = create_applications.save()
        if is_save:
            return jsonify(message='Succcess', response=200)

    return jsonify(message='Failed', response=400)