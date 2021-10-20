from orator.orm import belongs_to

from application import db

class Companies(db.Model):
    __table__ = 'companies'
    __fillable__ = ['name','email','password','desc','address','website_url','is_active', 'token',
                    'expired_token']

    @belongs_to
    def jobs(self):
        from applications.company.v1.model.jobs import Jobs
        return Jobs