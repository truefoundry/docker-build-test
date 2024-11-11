from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os

pipe = pipeline(model="unsloth/Llama-3.2-1B")

app = FastAPI()

class RequestModel(BaseModel):
   input: str

@app.post("/infer")
def get_response(request: RequestModel):
   prompt = request.input
   response = pipe(prompt)
   return response