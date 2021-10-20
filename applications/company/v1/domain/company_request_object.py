from applications.helper import helper

class CompanyRequestObject(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.desc = kwargs.get('desc')
        self.address = kwargs.get('address')
        self.website_url = kwargs.get('website_url')
        self.is_active = kwargs.get('is_active')


    @classmethod
    def from_dict(cls, adict):
        return CompanyRequestObject(**{
            "name": helper.get_value('name', adict, None),
            "email": helper.get_value('email', adict, None),
            "password": helper.get_value('password', adict, None),
            "desc": helper.get_value('description', adict, ''),
            "address": helper.get_value('address', adict, ''),
            "website_url": helper.get_value('websiteUrl', adict, None),
            "is_active": helper.get_value('isActive', adict, False),
        })
