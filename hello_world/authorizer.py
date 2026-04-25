import os


def handler(event, context):
    token = event.get("authorizationToken", "")
    method_arn = event.get("methodArn", "")

    # Replace with your real token validation logic
    effect = "Allow" if token == os.environ.get("AUTH_TOKEN", "allow") else "Deny"

    return {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": method_arn,
                }
            ],
        },
    }
