import datetime

from applications.helper import helper


class ApplicantRequestObject(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.address = kwargs.get('address')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    @classmethod
    def from_dict(cls, adict):
        return ApplicantRequestObject(**{
            "name": helper.get_value('name', adict, ''),
            "email": helper.get_value('email', adict, ''),
            "password": helper.get_value('password', adict, ''),
            "address": helper.get_value('address', adict, ''),
            "phone": helper.get_value('phone',adict ,'')
        })

    @classmethod
    def to_object(cls, jobs_db):
        return {
            "id":jobs_db.id,
            "name": jobs_db.jobs_title,
            "email": jobs_db.jobs_title.email,
            "password": jobs_db.jobs_title.password,
            "address": jobs_db.jobs_desc,
            "phone": jobs_db.min_qualifications,
            "token": jobs_db.count_vacancy,
            "created_at": datetime.datetime.strptime(str(jobs_db.created_at._datetime)[:-13],'%Y-%m-%d %H:%M:%S'),
            "updated_at": datetime.datetime.strptime(str(jobs_db.updated_at._datetime)[:-13],'%Y-%m-%d %H:%M:%S'),
            "expired_token": datetime.datetime.strptime(jobs_db.expired_token[:-7],'%Y-%m-%d %H:%M:%S')
        }