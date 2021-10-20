import datetime

from applications.helper import helper


class JobsRequestObject(object):

    def __init__(self, **kwargs):
        self.job_title = kwargs.get('job_title')
        self.job_desc = kwargs.get('job_desc')
        self.min_qualifications = kwargs.get('min_qualifications')
        self.count_vacancy = kwargs.get('count_vacancy')
        self.job_level = kwargs.get('job_level')
        self.job_category = kwargs.get('job_category')
        self.education_required = kwargs.get('education_required')
        self.company_id = kwargs.get('company_id')


    @classmethod
    def from_dict(cls, adict):
        return JobsRequestObject(**{
            "job_title": helper.get_value('jobTitle', adict, ''),
            "job_desc": helper.get_value('jobDesc', adict, ''),
            "min_qualifications": helper.get_value('minQualifications',adict ,''),
            "count_vacancy" : helper.get_value('countVacancy',adict,0),
            "job_level": helper.get_value('minQualif', adict, ''),
            "job_category": helper.get_value('jobCategory', adict, ''),
            "education_required": helper.get_value('eduRequired', adict, ''),
            "company_id": helper.get_value('companyId', adict, 0)
        })

    @classmethod
    def to_object(cls, jobs_db):
        return {
            "id":jobs_db.id,
            "job_title": jobs_db.jobs_title,
            "job_desc": jobs_db.jobs_desc,
            "min_qualifications": jobs_db.min_qualifications,
            "count_vacancy": jobs_db.count_vacancy,
            "job_level": jobs_db.jobs_level,
            "job_category": jobs_db.jobs_category,
            "education_required": jobs_db.edu_background,
            "company_id": jobs_db.companies_id,
            "created_at": datetime.datetime.strptime(str(jobs_db.created_at._datetime)[:-13],'%Y-%m-%d %H:%M:%S'),
            "updated_at": datetime.datetime.strptime(str(jobs_db.updated_at._datetime)[:-13],'%Y-%m-%d %H:%M:%S'),
            "expired_post": datetime.datetime.strptime(jobs_db.expired_post[:-7],'%Y-%m-%d %H:%M:%S')
        }

