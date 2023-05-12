# main.py
from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('./data/utilization2019.csv')

app = FastAPI()

@app.get('/')
async def root():
    return {'this is a API service for MN healthcare utilization code details'}

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.get("/ccd/{value}")
async def ccode(value):
    print('value: ', value)
    filtered = df[df['age_group_code'] == value]
    if len(filtered) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered.to_json(orient="records")}

@app.get('/ccd/{value}/principal_diagnosis_code/{value2}')
async def ccode2(value, value2):
    filtered = df[df['age_group_code'] == value]
    filtered2 = filtered[filtered['principal_diagnosis_code'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered2.to_json(orient="records")}    