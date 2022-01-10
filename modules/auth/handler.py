import json
import os

import boto3

cidp = boto3.client("cognito-idp")
client_id = os.getenv("COGNITO_CLIENT_ID_USER")


def login(event, context):
    event = json.loads(event["body"])

    response = cidp.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": event["email"],
            "PASSWORD": event["password"],
        },
        ClientId=client_id,
    )

    return {
        "statusCode": "200",
        "body": json.dumps(response),
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        },
    }
