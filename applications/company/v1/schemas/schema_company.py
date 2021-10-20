schema_create_jobs = {
    'type': 'object',
        'properties': {
            'jobTitle': {'type': 'string'},
            'jobDesc': {'type': 'string'},
            'minQualifications': {'type':'string'},
            'jobLevel': {'type':'string'},
            'countVacancy':{'type':'integer'},
            'jobCategory': {'type':'string'},
            'eduRequired': {'type':'string'},
            'companyId': {'type':'integer'}
        },
    'required': ['jobTitle', 'jobDesc', 'minQualifications', 'jobLevel', 'jobCategory', 'eduRequired', 'companyId']
}

schema_create_company = {
    'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'password': {'type': 'string'},
            'description': {'type': 'string'},
            'address': {'type':'string'},
            'websiteUrl': {'type':'string'},
            'isActive': {'type':'boolean'}
        },
    'required': ['name', 'email','password', 'description', 'address', 'websiteUrl', 'isActive']
}


schema_login_company = {
    'type': 'object',
        'properties': {
            'email': {'type': 'string'},
            'password': {'type': 'string'}
        },
    'required': ['email','password']
}

