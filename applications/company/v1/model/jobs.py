
from orator.orm import has_many
from application import db

class Jobs(db.Model):
    __table__ = 'jobs'
    __fillable__ = ['jobs_title','jobs_desc','min_qualifications','jobs_level','count_vacancy',
                    'jobs_category','edu_background','companies_id','expired_post']

    @has_many
    def companies(self):
        from applications.company.v1.model.companies import Companies
        return Companies