import jwt
import json

# define the payload data for the JWT token
def handler(event=None, context=None):
    payload = {
        'user_id': '123',
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    # define the secret key to sign the JWT token
    secret_key = 'my-secret-key'

    # generate the JWT token
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')

    print(jwt_token)
    return {
        'statusCode': 200,
        'token': json.dumps(jwt_token)
    }