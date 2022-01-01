import json

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "*",
}


def get_comments(event, context):

    sample_comment = [
        {"name": "Chris", "url": "https://gomakethings.com", "comment": "Hello, world!"}
    ]

    response = {
        "statusCode": 200,
        "body": json.dumps(sample_comment),
        "headers": headers,
    }

    return response


def create_comment(event, context):

    body = json.loads(event["body"])

    comment = {
        "name": body["name"],
        "url": body["url"],
        "comment": body["comment"],
    }

    response = {"statusCode": 200, "body": json.dumps(comment), "headers": headers}

    return response
