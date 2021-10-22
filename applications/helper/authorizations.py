from datetime import datetime

import jwt
from flask import request, jsonify
from six import wraps
from application import app
from applications.company.v1.model.companies import Companies


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            jwt_decode = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            d2 =jwt_decode['expired_token'][:-7]
            d1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')

            difference = d2 - d1
            if difference.total_seconds()/60 > 0:
                if jwt_decode['login_as'] == 'company':
                    current_user = Companies.find(int(jwt_decode['id']))
                    if current_user.token != token:
                        return jsonify({'message': 'token is invalid'})
                else:
                    return jsonify({'message': "you don't have authorization for this features"})
            else:
                return jsonify({'message': 'token is invalid'})

        except Exception as e:
            return jsonify({'message': str(e)})
        return f(current_user, *args, **kwargs)
    return decorator