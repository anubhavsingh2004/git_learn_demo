import json
import os
from setup_redis import create_redis_cluster


def lambda_handler(event, context):
    query = event.get("queryStringParameters", {}) or {}
    action = query.get("action", "POST")

    headers = event.get("headers", {}) or {}
    if headers.get("x-api-key") != os.environ['XAPI_KEY']:
        return {
            "statusCode": 403,
            "body": "Forbidden: Invalid XAPI Key"
        }

    if action != "POST":
        return {
            "statusCode": 400,
            "body": f"Unsupported action: {action}"
        }

    try:
        result = create_redis_cluster()
        return {
            "statusCode": 200,
            "body": f"Script output: {result}"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
