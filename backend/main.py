from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message':'Hello Ratnadeep'}

@app.get('/about')
def hello():
    return {'message':'I am From Kolhapur , pursuing B.Tech'}