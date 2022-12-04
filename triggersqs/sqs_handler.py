from pydantic import BaseModel
import json 
import os

ARN_SOURCE = f'arn:aws:sqs:us-east-1:123456789012:triggersqs_Queue'

class Message(BaseModel):
    command: str
    client_id: str

class SQSHandler():
    def __init__(self, ARN_SOURCE):
        self.ARN_SOURCE = ARN_SOURCE

    def parse_messages(self, event):
        messages = [Message(**json.loads(record['body'])) for record in event.get("Records", []) if record['eventSourceARN'] == self.ARN_SOURCE]
        return messages

def handler_sqs(event):

    sqs_handler = SQSHandler(ARN_SOURCE)
    messages = sqs_handler.parse_messages(event)
    #try:
    for message in messages:
        open('/tmp/' +  "log.txt", 'a+').write(str(message.dict()) + "\n")
    #except Exception as e:
    #    return {"status": f"deu ruim: {str(e)}, message: {ARN_SOURCE}"}


