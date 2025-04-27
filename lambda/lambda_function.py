import json
def lamdda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from  our CICD gitbub actions workflow vscode')
    }