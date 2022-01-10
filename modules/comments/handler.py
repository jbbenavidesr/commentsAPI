import json

from database.database import Comment, SessionLocal

session = SessionLocal()

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "*",
}


def get_comments(event, context):

    comments = session.query(Comment)

    response = {
        "statusCode": 200,
        "body": json.dumps(
            [
                {
                    "name": comment.name,
                    "url": comment.url,
                    "comment": comment.Comment,
                    "email": comment.email,
                }
                for comment in comments
            ]
        ),
        "headers": headers,
    }

    return response


def create_comment(event, context):

    body = json.loads(event["body"])

    comment = {
        "name": body["name"],
        "url": body["url"],
        "Comment": body["comment"],
        "key": body["key"],
    }

    Comment.create(session, **comment)

    response = {"statusCode": 200, "body": json.dumps(comment), "headers": headers}

    return response
