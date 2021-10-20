from orator.orm import belongs_to

from application import db



class Applicants(db.Model):
    __table__ = 'applicants'
    __fillable__ = ['name','email','password','address','phone','token','expired_token']

    @belongs_to
    def applicantions(self):
        from applications.applicant.v1.models.applications import Applications
        return Applications