from mangum import Mangum
from triggersqs.main import app
from triggersqs.sqs_handler import handler_sqs

def event_handler(event, context):
    if event.get("Records"):
        return handler_sqs(event)

    if event.get("httpMethod"):
        asgi_handler = Mangum(app)
        return asgi_handler(event, context)
        
    #other handlers here


def lambda_handler(event, context):
    return event_handler(event, context)