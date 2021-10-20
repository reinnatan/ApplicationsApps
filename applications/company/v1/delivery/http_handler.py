

import jwt
from flask import jsonify, request, Blueprint
from flask_expects_json import expects_json

from application import app
from applications.company.v1.domain.company_request_object import CompanyRequestObject
from applications.company.v1.domain.jobs_request_object import JobsRequestObject
from applications.company.v1.model.companies import Companies
from applications.company.v1.model.jobs import Jobs
from applications.company.v1.schemas.schema_company import schema_create_jobs, schema_create_company, \
    schema_login_company
from applications.helper.authorizations import token_required

API_COMPANY = Blueprint('/v1/company', __name__, url_prefix='/v1/company')

@API_COMPANY.route('/sign-up', methods = ['POST'])
@expects_json(schema_create_company)
def sign_up():

    request_object = CompanyRequestObject.from_dict(request.json)
    companies = Companies.create(
        name=request_object.name,
        email=request_object.email,
        password=request_object.password,
        desc=request_object.desc,
        address=request_object.address,
        website_url=request_object.website_url,
        is_active=request_object.is_active,
        token='',
        expired_token=''
    )

    is_saved = companies.save()
    if is_saved:
        return jsonify(message='Succcess', response=200)
    else:
        return jsonify(message='Failed', response=200)

@API_COMPANY.route('/login', methods = ['POST'])
@expects_json(schema_login_company)
def login():
    import datetime
    request_object = CompanyRequestObject.from_dict(request.json)
    company = Companies.where_raw('email=? and password=?',[request_object.email, request_object.password]).first()
    exp_token_date = datetime.datetime.now() + datetime.timedelta(minutes=15)

    if company:
        jwt_token = jwt.encode({"id": str(company.id), "expired_token":str(exp_token_date), "login_as":"company"}, app.config['SECRET_KEY'], algorithm="HS256")
        company.expired_token = exp_token_date
        company.token = jwt_token
        company.save()

        return jsonify(token=jwt_token, response=200)

    return jsonify(message='Failed, company not found', response=404)

@API_COMPANY.route('/edit-profile/<company_id>', methods = ['PUT'])
def edit_profile(company_id):
    request_object = CompanyRequestObject.from_dict(request.json)
    company = Companies.find(company_id)
    if company:
        company.name=request_object.name
        company.email=request_object.email
        company.password=request_object.password
        company.desc=request_object.desc
        company.address=request_object.address
        company.website_url=request_object.website_url
        company.is_active=request_object.is_active
        is_saved = company.save()
        if is_saved:
            return jsonify(message='Succcess Update', response=200)
        else:
            return jsonify(message='Failed Update', response=200)
    return jsonify(message='Failed Update', response=200)


@API_COMPANY.route('/create-job', methods = ['POST'])
@expects_json(schema_create_jobs)
@token_required
def create_job(current_user):
    import datetime
    request_object = JobsRequestObject.from_dict(request.json)

    company = Companies.find(request_object.company_id)
    if company is None:
        return jsonify(message='Failed Company Not Found', response=400)

    jobs = Jobs.create(
                jobs_title=request_object.job_title,
                jobs_desc=request_object.job_desc,
                min_qualifications=request_object.min_qualifications,
                jobs_level=request_object.job_level,
                jobs_category=request_object.job_category,
                edu_background=request_object.education_required,
                count_vacancy=request_object.count_vacancy,
                companies_id=request_object.company_id,
                expired_post=datetime.datetime.now() + datetime.timedelta(days=7)
                )
    is_save = jobs.save()
    if is_save:
        return jsonify(message='Succcess', response=200)
    else:
        return jsonify(message='Failed', response=400)


@API_COMPANY.route('/edit-job/<job_id>', methods = ['PUT'])
@expects_json(schema_create_jobs)
@token_required
def edit_job(current_user, job_id):
    import datetime
    request_object = JobsRequestObject.from_dict(request.json)

    company = Companies.find(request_object.company_id)
    if company is None:
        return jsonify(message='Failed Company Not Found', response=400)

    jobs = Jobs.find(job_id)
    if jobs:
        jobs.jobs_title=request_object.job_title
        jobs.jobs_desc=request_object.job_desc
        jobs.min_qualifications=request_object.min_qualifications
        jobs.jobs_level=request_object.job_level
        jobs.jobs_category=request_object.job_category
        jobs.edu_background=request_object.education_required
        jobs.count_vacancy=request_object.count_vacancy
        jobs.companies_id=request_object.company_id
        jobs.expired_post=datetime.datetime.now() + datetime.timedelta(days=7)
        is_save = jobs.save()
        if is_save:
            return jsonify(message='Succcess', response=200)
        else:
            return jsonify(message='Failed', response=400)

    return jsonify(message='Failed', response=400)

@API_COMPANY.route('/list-jobs', methods = ['GET'])
@token_required
def list_jobs(current_user):
    from datetime import datetime
    list_jobs = []
    for job in Jobs.all():
        d1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(job.expired_post[:-7], '%Y-%m-%d %H:%M:%S')
        days = abs((d2 - d1).days)
        if days>0:
            list_jobs.append(JobsRequestObject.to_object(job))
    return jsonify(data=list_jobs, response=200)

