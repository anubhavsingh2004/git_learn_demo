import json
import subprocess
import os

def lambda_handler(event, context):
    query = event.get("queryStringParameters", {})
    action = query.get("action", "POST")

    headers = event.get("headers", {})
    if headers.get("x-api-key") != os.environ['XAPI_KEY']:
        return { "statusCode": 403, "body": "Forbidden: Invalid XAPI Key" }

    try:
        if action == "POST":
            result = subprocess.run(["/bin/bash", "/var/task/setup_redis.sh"], capture_output=True, text=True)
            return {
                "statusCode": 200,
                "body": f"Script output: {result.stdout or result.stderr}"
            }
        else:
            return {
                "statusCode": 400,
                "body": f"Unsupported action: {action}"
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
