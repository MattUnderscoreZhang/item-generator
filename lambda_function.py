from typing import Any

from item_generator import db_operations


def lambda_handler(event, context) -> dict[str, Any]:
    """
    Lambda function to manipulate item database.
    Input:
        function: str - name of function to call
            "add_random_item": add a random item to the database
            "clear_database": clear the database
    Output:
        body: Any - response body
    """
    function = event["function"]
    if function == "add_random_item":
        result = db_operations.add_random_item()
    elif function == "clear_database":
        result = db_operations.clear_database()
    elif function == "get_items":
        result = db_operations.get_items()
    else:
        result = f"Unknown function: {function}"
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Accept': '*/*',
            'Content-Type': 'application/json'
        },
        'body': result
    }
