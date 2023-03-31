import json
import jwt

def handler(event = None, context = None):
    # TODO implement
    print(event)
    print(context)
    regionId = '--- aws region ----'
    accountId = '---- account number ----'
    apiId = "---- api gateway id -----"
    stage = '---- stage ----'
    try:
        print(type(event))
        print(type(context))
        # event = json.loads(event)
        token = event["authorizationToken"]
        token = token.split()[1]
        print(token)
        tok = jwt.decode(token, 'my-secret-key', 'HS256')
        print(tok)
        return {
            "principalId": "abcdef",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": f"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/PUT/*"
                }
                ]
            },
        }
    except jwt.ExpiredSignatureError as e:
        print(f'ExpiredSignatureError: {e}')
        return {
            "principalId": "abcdef",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": f"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/PUT/*"
                }
                ]
            },
        }
    except jwt.InvalidIssuerError as e:
        print(f'InvalidIssuerError: {e}')
        return {
            "principalId": "abcdef",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": f"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/PUT/*"
                }
                ]
            },
        }
    except jwt.InvalidIssuedAtError as e: 
        print(f'InvalidIssuedAtError: {e}')
        return {
            "principalId": "abcdef",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": f"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/PUT/*"
                }
                ]
            },
        }
    except jwt.exceptions.DecodeError as e: 
        print(f'DecodeError: {e}')
        return {
            "principalId": "abcdef",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": f"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/PUT/*"
                }
                ]
            }
        }

# print(handler())