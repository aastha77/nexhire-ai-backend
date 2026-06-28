from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(

CORSMiddleware,

allow_origins=[

"http://localhost:3000"

],

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"],

)

# CORS FIX

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)





class JobRequest(BaseModel):

    description:str





@app.get("/")

def home():

    return {

        "status":"NexHire AI Online"

    }







@app.post("/search")

def search(job:JobRequest):


    df = pd.read_csv(

        "output/ranked_candidates.csv"

    )


    results = df.head(10).to_dict(

        orient="records"

    )


    return {


        "query":job.description,


        "candidates":results


    }