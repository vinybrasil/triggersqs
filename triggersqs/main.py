from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/healthcheck")
def root():
    return {"message": "health check"}

@app.get("/records")
def root():
    try:
        with open('/tmp/' +  "log.txt", 'r') as fp:
            line = fp.readlines()

        lines = [ json.loads(x.replace("\n", "").replace("'", '"')) for x in line]
        b = {}

        for i in range(len(lines)):
            b[f"{i}"] =  lines[i]
        return  {"messages": b}

    except: #when there are no messages
        return {"messages": {}}