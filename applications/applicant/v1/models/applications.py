from orator.orm import has_many

from application import db

class Applications(db.Model):
    __table__ = 'applications'
    __fillable__ = ['status','applicants_id','jobs_id']

    @has_many
    def applicants(self):
        from applications.applicant.v1.models.applicants import Applicants
        return Applicants