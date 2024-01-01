from mangum import Mangum

from fastapi import FastAPI

app = FastAPI()

#home url
@app.get("/")
async def root():
  return "Hello World"

#this would help bind aws lambda to the fast api function
handler = Mangum(app=app)