from fastapi import FastAPI
import uvicorn
import sys
import re
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str ="What is Text Summarization?"

app=FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful!")
    except Exception as e:
        return Response(f"Error occured: {e}")
    
@app.get("/predict",responses={422: {"description": "Validation Error"}})
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

