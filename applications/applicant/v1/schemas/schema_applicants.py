schema_create_applicant = {
    'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'address': {'type': 'string'},
            'phone': {'type':'string'}
        },
    'required': ['name', 'address', 'phone']
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

schema_create_applicantions = {
    'type': 'object',
        'properties': {
            'jobsId': {'type': 'integer'}
        },
    'required': ['jobsId']
}

