import json
from typing import Any

from item_generator import db_operations


def lambda_handler(event, context) -> dict[str, Any]:
    """
    Lambda function to manipulate item database.
    Input:
        function: str - name of function to call
            "add_random_item": add a random item to the database
            "delete_items": delete all items
            "get_items": get all items
    Output:
        body: Any - response body
    """
    # https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads
    method = event["requestContext"]["http"]["method"]
    status_code = 200

    if method == "GET":
        result = db_operations.get_items()
    elif method == "POST":
        function = json.loads(event["body"])["function"]
        if function == "add_random_item":
            result = db_operations.add_random_item()
        elif function == "delete_items":
            result = db_operations.delete_items()
        else:
            result = f"Unknown function: {function}"
            status_code = 400
    else:
        result = f"Unsupported method: {method}"
        status_code = 400

    return {
        'statusCode': status_code,
        # 'headers': {
            # 'Access-Control-Allow-Headers': '*',
            # 'Access-Control-Allow-Origin': '*',
            # 'Access-Control-Allow-Methods': '*',
            # 'Accept': '*/*',
            # 'Content-Type': 'application/json'
        # },
        'body': result
    }
